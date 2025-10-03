"""
msprites2 Integration Adapter

Provides a compatibility layer between our existing transcription API
and the new msprites2 v0.13.0 library. Maintains backward compatibility
while leveraging msprites2's superior performance and features.
"""

import logging
from pathlib import Path
from typing import Any, Optional

from msprites2 import AudioTranscriber
from msprites2.audio_transcription import TranscriptionSegment as MSpriteSegment
from msprites2.enhancers import OllamaTextEnhancer

from ..constants import TRANSCRIPTION
from .models import TranscriptionResult

logger = logging.getLogger(__name__)


class MSprites2TranscriptionAdapter:
    """
    Adapter that wraps msprites2 AudioTranscriber with our configuration.

    This adapter:
    - Maintains our existing TranscriptionResult API
    - Uses our TRANSCRIPTION constants for configuration
    - Provides the same interface as our original WhisperClient
    - Adds msprites2's advanced features (word timestamps, confidence, etc.)
    """

    def __init__(
        self,
        model_size: str = "base",
        ollama_host: Optional[str] = None,
        ollama_port: Optional[int] = None,
    ):
        """Initialize adapter with msprites2 components.

        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
            ollama_host: Ollama server host (uses TRANSCRIPTION config if None)
            ollama_port: Ollama server port (uses TRANSCRIPTION config if None)
        """
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.model_size = model_size

        # Use our configuration if not specified
        if ollama_host is None:
            ollama_host = TRANSCRIPTION["ollama"]["default_host"]
        if ollama_port is None:
            ollama_port = TRANSCRIPTION["ollama"]["default_port"]

        self.ollama_host = ollama_host
        self.ollama_port = ollama_port

        # Initialize msprites2 components
        self._transcriber: Optional[AudioTranscriber] = None
        self._enhancer: Optional[OllamaTextEnhancer] = None
        self._initialized = False

    async def initialize(self, enable_enhancement: bool = True) -> bool:
        """Initialize msprites2 components.

        Args:
            enable_enhancement: Whether to enable Ollama text enhancement

        Returns:
            True if initialization successful
        """
        try:
            self.logger.info(f"Initializing msprites2 with model: {self.model_size}")

            # Create enhancer if enabled
            if enable_enhancement:
                try:
                    # Map model size to large-v3 if it's "large"
                    model_size = "large-v3" if self.model_size == "large" else self.model_size

                    self._enhancer = OllamaTextEnhancer(
                        host=self.ollama_host,
                        port=self.ollama_port,
                        model=TRANSCRIPTION["ollama"]["preferred_models"][0],  # Use first preferred model
                    )

                    # Add our domain-specific contexts
                    self._enhancer.add_custom_context(
                        "video-content",
                        "Clean up this video content transcript. "
                        "Fix grammar, remove filler words (um, uh, like), add proper punctuation. "
                        "Keep it natural and conversational:\n\n{text}"
                    )

                    self.logger.info(f"✓ Ollama enhancer initialized: {self.ollama_host}:{self.ollama_port}")
                except Exception as e:
                    self.logger.warning(f"Ollama enhancer initialization failed: {e}")
                    self._enhancer = None

            # Map model size to msprites2 format
            model_size = "large-v3" if self.model_size == "large" else self.model_size

            # Create transcriber with optional enhancer
            self._transcriber = AudioTranscriber(
                model_size=model_size,  # type: ignore
                device="auto",  # Auto-detect CPU/CUDA
                compute_type="int8",  # Efficient for CPU
                enhancer=self._enhancer
            )

            self._initialized = True
            self.logger.info(f"✓ msprites2 initialized successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to initialize msprites2: {e}")
            return False

    async def transcribe_video(
        self,
        video_path: Path,
        enhance_with_ollama: bool = True,
        domain_context: str = "general",
        language: Optional[str] = None,
    ) -> Optional[TranscriptionResult]:
        """
        Transcribe video using msprites2.

        Maintains compatibility with our existing API while using
        msprites2's enhanced transcription pipeline.

        Args:
            video_path: Path to video file
            enhance_with_ollama: Whether to enhance with Ollama
            domain_context: Domain context (general, technical, educational, video-content)
            language: Force specific language (None for auto-detect)

        Returns:
            TranscriptionResult or None if failed
        """
        if not self._initialized or not self._transcriber:
            if not await self.initialize(enable_enhancement=enhance_with_ollama):
                return None

        try:
            self.logger.info(f"Transcribing video: {video_path.name}")

            # Use enhanced transcription if enhancer is available
            if enhance_with_ollama and self._enhancer:
                self.logger.info(f"Using enhanced transcription with context: {domain_context}")

                segments, enhanced_text = await self._transcriber.transcribe_enhanced(
                    video_path=str(video_path),
                    context=domain_context,
                    language=language,
                    beam_size=5,  # Good balance of speed/quality
                    vad_filter=True,  # Filter silence
                )

                # Convert msprites2 segments to our format
                our_segments = self._convert_segments(segments)
                raw_text = " ".join([seg.text for seg in segments])

                # Calculate duration
                duration = max([seg.end for seg in segments]) if segments else 0.0

                # Detect language from first segment
                detected_language = segments[0].language if segments and segments[0].language else "en"

                result = TranscriptionResult(
                    video_path=video_path,
                    language=detected_language,
                    duration=duration,
                    raw_text=raw_text,
                    enhanced_text=enhanced_text,
                    segments=our_segments,
                )

                self.logger.info(f"✓ Enhanced transcription complete: {len(segments)} segments")
                return result

            else:
                # Basic transcription without enhancement
                self.logger.info("Using basic transcription (no enhancement)")

                segments = self._transcriber.transcribe(
                    video_path=str(video_path),
                    language=language,
                    beam_size=5,
                    vad_filter=True,
                )

                # Convert and create result
                our_segments = self._convert_segments(segments)
                raw_text = " ".join([seg.text for seg in segments])
                duration = max([seg.end for seg in segments]) if segments else 0.0
                detected_language = segments[0].language if segments and segments[0].language else "en"

                result = TranscriptionResult(
                    video_path=video_path,
                    language=detected_language,
                    duration=duration,
                    raw_text=raw_text,
                    enhanced_text=None,
                    segments=our_segments,
                )

                self.logger.info(f"✓ Basic transcription complete: {len(segments)} segments")
                return result

        except Exception as e:
            self.logger.error(f"Transcription failed: {e}")
            return None

    def _convert_segments(self, msprite_segments: list[MSpriteSegment]) -> list[dict[str, Any]]:
        """
        Convert msprites2 segments to our format.

        This maintains backward compatibility while preserving
        the enhanced metadata from msprites2.

        Args:
            msprite_segments: List of msprites2 TranscriptionSegment objects

        Returns:
            List of segment dictionaries in our format
        """
        our_segments = []

        for seg in msprite_segments:
            segment_dict = {
                "start": seg.start,
                "end": seg.end,
                "text": seg.text.strip(),
                "words": [],  # Compatibility field
            }

            # Add enhanced fields if available (new in msprites2 v0.13.0)
            if seg.enhanced_text:
                segment_dict["enhanced_text"] = seg.enhanced_text

            if seg.confidence is not None:
                segment_dict["confidence"] = seg.confidence

            if seg.speaker_id:
                segment_dict["speaker_id"] = seg.speaker_id

            if seg.language:
                segment_dict["language"] = seg.language

            # Convert word timestamps if available
            if seg.words:
                segment_dict["words"] = [
                    {
                        "word": w.word,
                        "start": w.start,
                        "end": w.end,
                        "probability": w.probability,
                    }
                    for w in seg.words
                ]

            # Add metadata if available
            if seg.metadata:
                segment_dict["metadata"] = seg.metadata

            our_segments.append(segment_dict)

        return our_segments

    def get_capabilities(self) -> dict[str, Any]:
        """Get transcription capabilities."""
        return {
            "whisper_available": True,  # msprites2 uses faster-whisper
            "faster_whisper": True,  # New capability!
            "supported_models": ["tiny", "base", "small", "medium", "large-v3"],
            "audio_formats": ["mp4", "avi", "mov", "mkv", "webm", "mp3", "wav"],
            "ollama_support": self._enhancer is not None,
            "output_formats": ["json", "txt", "webvtt"],  # Now includes webvtt!
            "domain_contexts": ["general", "technical", "educational", "medical", "legal", "video-content"],
            "enhanced_features": {
                "word_timestamps": True,
                "confidence_scores": True,
                "speaker_detection": True,
                "post_processing_hooks": True,
                "multi_format_output": True,
            },
        }

    async def save_transcription_results(
        self,
        result: TranscriptionResult,
        output_dir: Path,
        formats: Optional[list[str]] = None,
    ) -> dict[str, Path]:
        """
        Save transcription results using msprites2's multi-format output.

        Args:
            result: TranscriptionResult to save
            output_dir: Output directory
            formats: List of formats to save (json, txt, webvtt). None = all enabled formats

        Returns:
            Dictionary mapping format to file path
        """
        if not self._transcriber:
            raise RuntimeError("Transcriber not initialized")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Determine which formats to save based on configuration
        if formats is None:
            formats = []
            if TRANSCRIPTION["output"]["generate_json"]:
                formats.append("json")
            if TRANSCRIPTION["output"]["generate_text"]:
                formats.append("txt")
            if TRANSCRIPTION["output"]["generate_vtt"]:
                formats.append("webvtt")

        # Convert our segments back to msprites2 format for saving
        msprite_segments = [
            MSpriteSegment(
                start=seg["start"],
                end=seg["end"],
                text=seg["text"],
                enhanced_text=seg.get("enhanced_text"),
                confidence=seg.get("confidence"),
                speaker_id=seg.get("speaker_id"),
                language=seg.get("language"),
            )
            for seg in result.segments
        ]

        # Use msprites2's multi-format save
        base_name = result.video_path.stem
        self._transcriber.save_all_formats(
            segments=msprite_segments,
            enhanced_text=result.enhanced_text,
            output_dir=str(output_dir),
            base_name=base_name,
            formats=formats,
        )

        # Return paths to saved files
        saved_files = {}
        for fmt in formats:
            ext = "vtt" if fmt == "webvtt" else fmt
            file_path = output_dir / f"{base_name}.{ext}"
            if file_path.exists():
                saved_files[fmt] = file_path

        self.logger.info(f"✓ Saved {len(saved_files)} format(s): {list(saved_files.keys())}")
        return saved_files
