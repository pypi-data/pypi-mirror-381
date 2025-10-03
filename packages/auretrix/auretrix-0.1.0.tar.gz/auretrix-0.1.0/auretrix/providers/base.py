"""
Base provider interface
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseProvider(ABC):
    """Base class for all speech recognition providers"""
    
    def __init__(self, api_key: str = None, **kwargs):
        self.api_key = api_key
        self.config = kwargs
    
    @abstractmethod
    def transcribe(self, audio_source: str, language: str, **kwargs) -> Dict[str, Any]:
        """
        Transcribe audio to text
        
        Args:
            audio_source: Path to audio file or audio data
            language: Language code
            **kwargs: Provider-specific parameters
        
        Returns:
            Dictionary containing:
                - text: Transcribed text
                - confidence: Confidence score (0-1)
                - words: List of word-level data (optional)
                - duration: Audio duration in seconds
                - metadata: Additional provider-specific data
        """
        pass
    
    @abstractmethod
    def get_supported_languages(self) -> List[str]:
        """Return list of supported language codes"""
        pass
    
    def validate_language(self, language: str) -> bool:
        """Check if language is supported"""
        return language in self.get_supported_languages()
    
    def get_cost_estimate(self, duration_seconds: float) -> float:
        """
        Estimate transcription cost in USD
        
        Args:
            duration_seconds: Audio duration
        
        Returns:
            Estimated cost in USD
        """
        return 0.0  # Override in subclasses