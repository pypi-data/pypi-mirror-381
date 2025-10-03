"""
Auretrix - Unified Speech Recognition Library
Simplify speech-to-text with multiple providers and auto-fallback
"""

__version__ = "0.1.0"
__author__ = "Auretrix AI"
__license__ = "MIT"

from auretrix.speech import SpeechRecognizer
from auretrix.transcribe import transcribe_audio, transcribe_file
from auretrix.languages import SUPPORTED_LANGUAGES, INDIAN_LANGUAGES
from auretrix.exceptions import (
    AuretrixError,
    TranscriptionError,
    ProviderError,
    AudioError
)

__all__ = [
    "SpeechRecognizer",
    "transcribe_audio",
    "transcribe_file",
    "SUPPORTED_LANGUAGES",
    "INDIAN_LANGUAGES",
    "AuretrixError",
    "TranscriptionError",
    "ProviderError",
    "AudioError"
]