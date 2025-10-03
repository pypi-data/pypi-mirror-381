"""Main video transcription orchestrator."""

import logging
from pathlib import Path
from typing import Any, Optional

from ..exceptions import VideoProcessorError
from .models import TranscriptionResult
from .msprites2_adapter import MSprites2TranscriptionAdapter

logger = logging.getLogger(__name__)


class VideoTranscriber:
    """
    Main transcription class that orchestrates the speech-to-text pipeline.

    Now powered by msprites2 v0.13.0 for superior performance and features:
    - faster-whisper for 2-3x speed improvement
    - Built-in Ollama text enhancement
    - Word-level timestamps and confidence scores
    - Multi-format output (JSON, TXT, WebVTT)
    - Post-processing hooks

    Maintains full backward compatibility with existing code.
    """

    def __init__(
        self,
        ollama_host: Optional[str] = None,
        ollama_port: Optional[int] = None,
        whisper_model: str = "base",
    ) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Use msprites2 adapter for all transcription operations
        self.adapter = MSprites2TranscriptionAdapter(
            model_size=whisper_model,
            ollama_host=ollama_host,
            ollama_port=ollama_port,
        )

    async def transcribe_video(
        self,
        video_path: Path,
        whisper_model: str = "base",
        enhance_with_ollama: bool = True,
        domain_context: str = "general",
        language: Optional[str] = None,
    ) -> Optional[TranscriptionResult]:
        """
        Complete video transcription pipeline.

        Now powered by msprites2 for superior performance and features.

        Args:
            video_path: Path to video file
            whisper_model: Whisper model size to use (now supports faster-whisper)
            enhance_with_ollama: Whether to enhance with Ollama
            domain_context: Context for enhancement (general, technical, educational, medical, legal, video-content)
            language: Force specific language (None for auto-detect)

        Returns:
            TranscriptionResult or None if failed
        """
        try:
            logger.info(f"🎬 Processing video: {video_path.name}")
            logger.info(f"   Model: {whisper_model}, Enhancement: {enhance_with_ollama}, Context: {domain_context}")

            # Use msprites2 adapter for transcription
            # The adapter handles initialization, transcription, and enhancement
            result = await self.adapter.transcribe_video(
                video_path=video_path,
                enhance_with_ollama=enhance_with_ollama,
                domain_context=domain_context,
                language=language,
            )

            if not result:
                raise VideoProcessorError("Transcription failed - no result returned")

            logger.info(f"✓ Transcription complete: {len(result.segments)} segments, {result.duration:.1f}s")
            if result.enhanced_text:
                logger.info(f"✓ Enhanced with Ollama ({domain_context} context)")

            return result

        except Exception as e:
            logger.error(f"Transcription pipeline failed: {e}")
            raise VideoProcessorError(f"Transcription failed: {e}") from e

    async def save_transcription_results(
        self,
        result: TranscriptionResult,
        output_dir: Path,
        formats: Optional[list[str]] = None,
    ) -> dict[str, Path]:
        """
        Save transcription results in multiple formats.

        Now supports WebVTT format in addition to JSON and TXT!

        Args:
            result: TranscriptionResult to save
            output_dir: Output directory
            formats: List of formats (json, txt, webvtt). None = use config

        Returns:
            Dictionary mapping format to file path
        """
        return await self.adapter.save_transcription_results(
            result=result,
            output_dir=output_dir,
            formats=formats,
        )

    def get_transcription_capabilities(self) -> dict[str, Any]:
        """
        Get information about available transcription capabilities.

        Returns enhanced capabilities from msprites2 adapter.
        """
        return self.adapter.get_capabilities()
