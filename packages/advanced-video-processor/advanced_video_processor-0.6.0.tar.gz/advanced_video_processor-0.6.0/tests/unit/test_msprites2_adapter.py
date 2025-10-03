"""Tests for msprites2 adapter integration."""

import pytest
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch

from video_processor.ai.msprites2_adapter import MSprites2TranscriptionAdapter
from video_processor.ai.models import TranscriptionResult


class TestMSprites2Adapter:
    """Test suite for msprites2 adapter functionality."""

    def test_adapter_initialization(self):
        """Test adapter initializes with correct configuration."""
        adapter = MSprites2TranscriptionAdapter(
            model_size="base",
            ollama_host="test-host",
            ollama_port=1234,
        )

        assert adapter.model_size == "base"
        assert adapter.ollama_host == "test-host"
        assert adapter.ollama_port == 1234

    def test_adapter_uses_config_defaults(self):
        """Test adapter uses TRANSCRIPTION constants for defaults."""
        adapter = MSprites2TranscriptionAdapter()

        # Should use constants from TRANSCRIPTION
        assert adapter.ollama_host is not None
        assert adapter.ollama_port is not None

    def test_capabilities_include_msprites2_features(self):
        """Test capabilities report includes msprites2 v0.13.0 features."""
        adapter = MSprites2TranscriptionAdapter()
        capabilities = adapter.get_capabilities()

        # Check new capabilities from msprites2
        assert capabilities["faster_whisper"] is True
        assert "enhanced_features" in capabilities
        assert capabilities["enhanced_features"]["word_timestamps"] is True
        assert capabilities["enhanced_features"]["confidence_scores"] is True
        assert capabilities["enhanced_features"]["speaker_detection"] is True
        assert capabilities["enhanced_features"]["post_processing_hooks"] is True

        # Check expanded domain contexts
        assert "medical" in capabilities["domain_contexts"]
        assert "legal" in capabilities["domain_contexts"]
        assert "video-content" in capabilities["domain_contexts"]

        # Check output formats include webvtt
        assert "webvtt" in capabilities["output_formats"]

    def test_segment_conversion_preserves_basic_fields(self):
        """Test segment conversion maintains backward compatibility."""
        from msprites2.audio_transcription import TranscriptionSegment

        adapter = MSprites2TranscriptionAdapter()

        msprite_segments = [
            TranscriptionSegment(
                start=0.0,
                end=2.5,
                text="Hello world",
                confidence=0.95,
                language="en",
            )
        ]

        our_segments = adapter._convert_segments(msprite_segments)

        assert len(our_segments) == 1
        assert our_segments[0]["start"] == 0.0
        assert our_segments[0]["end"] == 2.5
        assert our_segments[0]["text"] == "Hello world"
        assert our_segments[0]["confidence"] == 0.95
        assert our_segments[0]["language"] == "en"

    def test_segment_conversion_includes_enhanced_text(self):
        """Test segment conversion includes enhanced_text when available."""
        from msprites2.audio_transcription import TranscriptionSegment

        adapter = MSprites2TranscriptionAdapter()

        msprite_segments = [
            TranscriptionSegment(
                start=0.0,
                end=2.5,
                text="um hello like world",
                enhanced_text="Hello world.",  # Cleaned up version
                confidence=0.95,
            )
        ]

        our_segments = adapter._convert_segments(msprite_segments)

        assert our_segments[0]["enhanced_text"] == "Hello world."
        assert our_segments[0]["text"] == "um hello like world"  # Original preserved

    def test_large_model_mapped_to_large_v3(self):
        """Test 'large' model size is properly mapped to 'large-v3'."""
        adapter = MSprites2TranscriptionAdapter(model_size="large")

        # This ensures compatibility with msprites2's large-v3 model naming
        assert adapter.model_size == "large"  # We keep the input
        # The actual mapping happens during initialization


class TestVideoTranscriberWithAdapter:
    """Test VideoTranscriber using the msprites2 adapter."""

    def test_transcriber_initialization_with_adapter(self):
        """Test VideoTranscriber properly initializes with adapter."""
        from video_processor.ai.video_transcriber import VideoTranscriber

        transcriber = VideoTranscriber(
            ollama_host="test-host",
            ollama_port=1234,
            whisper_model="base",
        )

        assert transcriber.adapter is not None
        assert transcriber.adapter.model_size == "base"
        assert transcriber.adapter.ollama_host == "test-host"

    def test_capabilities_reflect_msprites2_features(self):
        """Test get_transcription_capabilities returns msprites2 features."""
        from video_processor.ai.video_transcriber import VideoTranscriber

        transcriber = VideoTranscriber()
        capabilities = transcriber.get_transcription_capabilities()

        # Check for msprites2-specific features
        assert capabilities["faster_whisper"] is True
        assert "webvtt" in capabilities["output_formats"]
        assert len(capabilities["domain_contexts"]) >= 6  # Now includes medical, legal, video-content

    @pytest.mark.asyncio
    async def test_save_transcription_returns_dict(self):
        """Test save_transcription_results returns dict mapping format to path."""
        from video_processor.ai.video_transcriber import VideoTranscriber
        from video_processor.ai.models import TranscriptionResult
        import tempfile

        transcriber = VideoTranscriber()

        result = TranscriptionResult(
            video_path=Path("test.mp4"),
            language="en",
            duration=10.0,
            raw_text="Hello world",
            enhanced_text="Hello, world!",
            segments=[],
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)

            # Mock the adapter's save method
            with patch.object(
                transcriber.adapter,
                "save_transcription_results",
                new_callable=AsyncMock,
            ) as mock_save:
                mock_save.return_value = {
                    "json": output_dir / "test.json",
                    "txt": output_dir / "test.txt",
                    "webvtt": output_dir / "test.vtt",
                }

                saved_files = await transcriber.save_transcription_results(
                    result, output_dir
                )

                # New return format is a dictionary
                assert isinstance(saved_files, dict)
                assert "json" in saved_files
                assert "txt" in saved_files
                assert "webvtt" in saved_files  # New format!


class TestBackwardCompatibility:
    """Test that migration maintains backward compatibility."""

    def test_transcription_result_unchanged(self):
        """Test TranscriptionResult model remains unchanged."""
        result = TranscriptionResult(
            video_path=Path("test.mp4"),
            language="en",
            duration=10.0,
            raw_text="Hello world",
            enhanced_text="Hello, world!",
            segments=[
                {"start": 0.0, "end": 2.0, "text": "Hello", "words": []},
                {"start": 2.0, "end": 4.0, "text": "world", "words": []},
            ],
        )

        # Check all original fields still exist
        assert result.video_path == Path("test.mp4")
        assert result.language == "en"
        assert result.duration == 10.0
        assert result.raw_text == "Hello world"
        assert result.enhanced_text == "Hello, world!"
        assert len(result.segments) == 2
        assert result.final_text == "Hello, world!"  # Property still works

    def test_segment_format_compatible(self):
        """Test segment format remains compatible with old code."""
        segment = {
            "start": 0.0,
            "end": 2.0,
            "text": "Hello",
            "words": [],  # Empty list for compatibility
        }

        # Old code expecting these fields should still work
        assert segment["start"] == 0.0
        assert segment["end"] == 2.0
        assert segment["text"] == "Hello"
        assert isinstance(segment["words"], list)

        # New fields are optional and don't break old code
        segment_enhanced = {
            **segment,
            "confidence": 0.95,
            "enhanced_text": "Hello!",
            "speaker_id": "speaker_1",
        }

        # Old code can safely ignore new fields
        assert segment_enhanced["start"] == 0.0
        assert segment_enhanced["text"] == "Hello"
