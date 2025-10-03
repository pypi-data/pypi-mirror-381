"""
OpenAI Whisper provider (local and API)
"""

from typing import Dict, Any, List
import logging

from auretrix.providers.base import BaseProvider
from auretrix.exceptions import ProviderError
from auretrix.utils import get_audio_duration

logger = logging.getLogger(__name__)


class WhisperProvider(BaseProvider):
    """OpenAI Whisper provider"""
    
    def __init__(self, api_key: str = None, use_local: bool = True, model: str = 'base', **kwargs):
        """
        Initialize Whisper provider
        
        Args:
            api_key: OpenAI API key (for API mode)
            use_local: Use local Whisper model if True
            model: Model size ('tiny', 'base', 'small', 'medium', 'large')
        """
        super().__init__(api_key, **kwargs)
        self.use_local = use_local
        self.model_name = model
        self.model = None
        
        if use_local:
            self._init_local_model()
    
    def _init_local_model(self):
        """Initialize local Whisper model"""
        try:
            import whisper
            logger.info(f"Loading Whisper model: {self.model_name}")
            self.model = whisper.load_model(self.model_name)
        except ImportError:
            raise ProviderError(
                "Whisper not installed. Install with: pip install openai-whisper"
            )
        except Exception as e:
            raise ProviderError(f"Failed to load Whisper model: {e}")
    
    def transcribe(self, audio_source: str, language: str = None, **kwargs) -> Dict[str, Any]:
        """Transcribe audio using Whisper"""
        
        if self.use_local:
            return self._transcribe_local(audio_source, language, **kwargs)
        else:
            return self._transcribe_api(audio_source, language, **kwargs)
    
    def _transcribe_local(self, audio_path: str, language: str = None, **kwargs) -> Dict[str, Any]:
        """Transcribe using local Whisper model"""
        if not self.model:
            self._init_local_model()
        
        try:
            # Extract language code (e.g., 'hi-IN' -> 'hi')
            lang_code = language.split('-')[0] if language else None
            
            result = self.model.transcribe(
                audio_path,
                language=lang_code,
                **kwargs
            )
            
            # Format response
            words = []
            if 'segments' in result:
                for segment in result['segments']:
                    if 'words' in segment:
                        words.extend(segment['words'])
            
            return {
                'text': result['text'].strip(),
                'confidence': None,  # Whisper doesn't provide confidence
                'words': words,
                'duration': get_audio_duration(audio_path),
                'metadata': {
                    'language': result.get('language'),
                    'segments': result.get('segments', [])
                }
            }
        
        except Exception as e:
            raise ProviderError(f"Whisper transcription failed: {e}")
    
    def _transcribe_api(self, audio_path: str, language: str = None, **kwargs) -> Dict[str, Any]:
        """Transcribe using OpenAI Whisper API"""
        if not self.api_key:
            raise ProviderError("OpenAI API key required for API mode")
        
        try:
            import openai
            openai.api_key = self.api_key
            
            with open(audio_path, 'rb') as audio_file:
                response = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file,
                    language=language.split('-')[0] if language else None,
                    **kwargs
                )
            
            return {
                'text': response['text'].strip(),
                'confidence': None,
                'words': [],
                'duration': get_audio_duration(audio_path),
                'metadata': {}
            }
        
        except Exception as e:
            raise ProviderError(f"Whisper API failed: {e}")
    
    def get_supported_languages(self) -> List[str]:
        """Whisper supports 99+ languages"""
        return [
            'en', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa', 'or', 'as', 'ur',
            'es', 'fr', 'de', 'zh', 'ja', 'ko', 'ar', 'ru', 'pt', 'it', 'nl', 'pl', 'tr',
            'vi', 'th', 'id', 'sv', 'da', 'no', 'fi', 'cs', 'ro', 'el', 'he', 'hu'
        ]
    
    def get_cost_estimate(self, duration_seconds: float) -> float:
        """
        Whisper API costs $0.006 per minute
        Local model is free
        """
        if self.use_local:
            return 0.0
        
        minutes = duration_seconds / 60
        return minutes * 0.006