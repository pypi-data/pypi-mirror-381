"""
Custom exceptions for Auretrix
"""


class AuretrixError(Exception):
    """Base exception for all Auretrix errors"""
    pass


class TranscriptionError(AuretrixError):
    """Error during transcription process"""
    pass


class ProviderError(AuretrixError):
    """Provider-specific errors"""
    pass


class AudioError(AuretrixError):
    """Audio file or format errors"""
    pass


class LanguageNotSupportedError(AuretrixError):
    """Language not supported by provider"""
    pass


class APIKeyError(AuretrixError):
    """Missing or invalid API key"""
    pass


class RateLimitError(AuretrixError):
    """API rate limit exceeded"""
    pass


class AudioTooLongError(AudioError):
    """Audio file exceeds maximum duration"""
    pass


class InvalidAudioFormatError(AudioError):
    """Unsupported audio format"""
    pass