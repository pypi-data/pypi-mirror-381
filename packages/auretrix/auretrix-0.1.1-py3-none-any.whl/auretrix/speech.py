"""
Core SpeechRecognizer class with multi-provider support
"""

import os
from typing import Optional, Dict, List, Any
from pathlib import Path
import logging

from auretrix.providers import (
    WhisperProvider,
    GoogleProvider,
    AssemblyAIProvider,
    AzureProvider
)
from auretrix.exceptions import ProviderError, TranscriptionError
from auretrix.utils import validate_audio_file, get_audio_duration

logger = logging.getLogger(__name__)


class SpeechRecognizer:
    """
    Unified speech recognition interface with auto-fallback support
    
    Example:
        >>> recognizer = SpeechRecognizer(
        ...     providers=['whisper', 'google'],
        ...     auto_fallback=True
        ... )
        >>> result = recognizer.recognize('audio.mp3', language='hi-IN')
        >>> print(result['text'])
    """
    
    PROVIDER_MAP = {
        'whisper': WhisperProvider,
        'google': GoogleProvider,
        'assemblyai': AssemblyAIProvider,
        'azure': AzureProvider
    }
    
    def __init__(
        self,
        providers: Optional[List[str]] = None,
        auto_fallback: bool = True,
        api_keys: Optional[Dict[str, str]] = None,
        optimize_cost: bool = True,
        **kwargs
    ):
        """
        Initialize SpeechRecognizer
        
        Args:
            providers: List of provider names in priority order
            auto_fallback: Auto switch to next provider on failure
            api_keys: Dictionary of API keys for providers
            optimize_cost: Choose cheapest provider first
            **kwargs: Additional provider-specific configuration
        """
        self.providers = providers or ['whisper', 'google']
        self.auto_fallback = auto_fallback
        self.optimize_cost = optimize_cost
        self.api_keys = api_keys or {}
        self.config = kwargs
        
        # Load API keys from environment if not provided
        self._load_env_keys()
        
        # Initialize provider instances
        self._provider_instances = {}
        self._init_providers()
    
    def _load_env_keys(self):
        """Load API keys from environment variables"""
        env_keys = {
            'google': 'GOOGLE_SPEECH_API_KEY',
            'assemblyai': 'ASSEMBLYAI_API_KEY',
            'azure': 'AZURE_SPEECH_KEY'
        }
        
        for provider, env_var in env_keys.items():
            if provider not in self.api_keys:
                key = os.getenv(env_var)
                if key:
                    self.api_keys[provider] = key
    
    def _init_providers(self):
        """Initialize provider instances"""
        for provider_name in self.providers:
            if provider_name not in self.PROVIDER_MAP:
                logger.warning(f"Unknown provider: {provider_name}")
                continue
            
            try:
                provider_class = self.PROVIDER_MAP[provider_name]
                api_key = self.api_keys.get(provider_name)
                
                self._provider_instances[provider_name] = provider_class(
                    api_key=api_key,
                    **self.config
                )
                logger.info(f"Initialized provider: {provider_name}")
            except Exception as e:
                logger.error(f"Failed to initialize {provider_name}: {e}")
    
    def recognize(
        self,
        audio_source: str,
        language: str = 'en-US',
        **kwargs
    ) -> Dict[str, Any]:
        """
        Recognize speech from audio file
        
        Args:
            audio_source: Path to audio file or audio data
            language: Language code (e.g., 'hi-IN', 'en-US')
            **kwargs: Additional recognition parameters
        
        Returns:
            Dictionary with transcription results
        """
        # Validate audio file
        if isinstance(audio_source, str):
            validate_audio_file(audio_source)
        
        # Get provider order (optimize by cost if enabled)
        provider_order = self._get_provider_order(audio_source, language)
        
        last_error = None
        for provider_name in provider_order:
            provider = self._provider_instances.get(provider_name)
            if not provider:
                continue
            
            try:
                logger.info(f"Trying provider: {provider_name}")
                result = provider.transcribe(audio_source, language, **kwargs)
                
                return {
                    'text': result['text'],
                    'language': language,
                    'provider': provider_name,
                    'confidence': result.get('confidence'),
                    'words': result.get('words'),
                    'duration': result.get('duration'),
                    'metadata': result.get('metadata', {})
                }
            
            except Exception as e:
                last_error = e
                logger.warning(f"{provider_name} failed: {e}")
                
                if not self.auto_fallback:
                    raise ProviderError(
                        f"{provider_name} failed and auto_fallback is disabled"
                    ) from e
                
                continue
        
        # All providers failed
        raise TranscriptionError(
            f"All providers failed. Last error: {last_error}"
        ) from last_error
    
    def _get_provider_order(
        self,
        audio_source: str,
        language: str
    ) -> List[str]:
        """Determine optimal provider order"""
        if not self.optimize_cost:
            return self.providers
        
        # Cost optimization logic
        try:
            duration = get_audio_duration(audio_source)
            
            # Whisper is free/cheap for shorter audio
            if duration < 300:  # 5 minutes
                order = ['whisper'] + [p for p in self.providers if p != 'whisper']
            else:
                # For longer audio, use cloud providers
                order = [p for p in self.providers if p != 'whisper'] + ['whisper']
            
            return order
        except Exception:
            return self.providers
    
    def recognize_stream(
        self,
        audio_stream,
        language: str = 'en-US',
        **kwargs
    ):
        """
        Real-time streaming recognition (future feature)
        """
        raise NotImplementedError("Streaming support coming soon!")
    
    def get_supported_languages(self, provider: Optional[str] = None) -> List[str]:
        """Get supported languages for a provider or all providers"""
        if provider:
            instance = self._provider_instances.get(provider)
            return instance.get_supported_languages() if instance else []
        
        # Return union of all provider languages
        all_langs = set()
        for instance in self._provider_instances.values():
            all_langs.update(instance.get_supported_languages())
        return sorted(list(all_langs))