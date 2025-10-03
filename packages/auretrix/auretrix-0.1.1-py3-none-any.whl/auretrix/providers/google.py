"""
Google Cloud Speech-to-Text provider
"""

from typing import Dict, Any, List
import logging

from auretrix.providers.base import BaseProvider
from auretrix.exceptions import ProviderError, APIKeyError
from auretrix.utils import get_audio_duration

logger = logging.getLogger(__name__)


class GoogleProvider(BaseProvider):
    """Google Cloud Speech-to-Text provider"""
    
    def __init__(self, api_key: str = None, **kwargs):
        """
        Initialize Google Speech provider
        
        Args:
            api_key: Google Cloud API key or credentials file path
            **kwargs: Additional configuration
        """
        super().__init__(api_key, **kwargs)
        self.client = None
        self._init_client()
    
    def _init_client(self):
        """Initialize Google Speech client"""
        try:
            from google.cloud import speech
            
            # If api_key is a file path to credentials
            if self.api_key:
                import os
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.api_key
            
            self.client = speech.SpeechClient()
            logger.info("Google Speech client initialized")
            
        except ImportError:
            raise ProviderError(
                "Google Cloud Speech not installed. "
                "Install with: pip install google-cloud-speech"
            )
        except Exception as e:
            logger.warning(f"Google Speech initialization failed: {e}")
            # Don't raise error here, will fail on transcribe if needed
    
    def transcribe(self, audio_source: str, language: str = 'en-US', **kwargs) -> Dict[str, Any]:
        """
        Transcribe audio using Google Speech-to-Text
        
        Args:
            audio_source: Path to audio file
            language: Language code (e.g., 'hi-IN', 'en-US')
            **kwargs: Additional parameters (enable_word_time_offsets, etc.)
        
        Returns:
            Transcription result dictionary
        """
        if not self.client:
            raise ProviderError("Google Speech client not initialized")
        
        try:
            from google.cloud import speech
            
            # Read audio file
            with open(audio_source, 'rb') as audio_file:
                content = audio_file.read()
            
            audio = speech.RecognitionAudio(content=content)
            
            # Configure recognition
            config = speech.RecognitionConfig(
                encoding=self._get_encoding(audio_source),
                sample_rate_hertz=16000,  # Default, adjust if needed
                language_code=language,
                enable_automatic_punctuation=True,
                enable_word_time_offsets=kwargs.get('enable_word_time_offsets', True),
                model=kwargs.get('model', 'default'),
                use_enhanced=kwargs.get('use_enhanced', True),
            )
            
            # Perform transcription
            response = self.client.recognize(config=config, audio=audio)
            
            # Process results
            if not response.results:
                return {
                    'text': '',
                    'confidence': 0.0,
                    'words': [],
                    'duration': get_audio_duration(audio_source),
                    'metadata': {}
                }
            
            # Combine all results
            full_transcript = []
            all_words = []
            total_confidence = 0
            
            for result in response.results:
                alternative = result.alternatives[0]
                full_transcript.append(alternative.transcript)
                total_confidence += alternative.confidence
                
                # Extract word-level timestamps
                if hasattr(alternative, 'words'):
                    for word_info in alternative.words:
                        all_words.append({
                            'word': word_info.word,
                            'start': word_info.start_time.total_seconds(),
                            'end': word_info.end_time.total_seconds(),
                            'confidence': getattr(word_info, 'confidence', None)
                        })
            
            avg_confidence = total_confidence / len(response.results) if response.results else 0
            
            return {
                'text': ' '.join(full_transcript).strip(),
                'confidence': avg_confidence,
                'words': all_words,
                'duration': get_audio_duration(audio_source),
                'metadata': {
                    'language': language,
                    'model': config.model
                }
            }
        
        except Exception as e:
            raise ProviderError(f"Google Speech transcription failed: {e}")
    
    def _get_encoding(self, audio_path: str):
        """Detect audio encoding from file extension"""
        from google.cloud import speech
        
        extension = audio_path.lower().split('.')[-1]
        
        encoding_map = {
            'wav': speech.RecognitionConfig.AudioEncoding.LINEAR16,
            'flac': speech.RecognitionConfig.AudioEncoding.FLAC,
            'mp3': speech.RecognitionConfig.AudioEncoding.MP3,
            'ogg': speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
            'm4a': speech.RecognitionConfig.AudioEncoding.MP3,
            'webm': speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        }
        
        return encoding_map.get(extension, speech.RecognitionConfig.AudioEncoding.LINEAR16)
    
    def get_supported_languages(self) -> List[str]:
        """Get supported language codes"""
        return [
            'en-US', 'en-GB', 'en-IN', 'en-AU',
            'hi-IN', 'bn-IN', 'te-IN', 'mr-IN', 'ta-IN', 'gu-IN', 'kn-IN', 'ml-IN', 'pa-IN', 'ur-IN',
            'es-ES', 'es-US', 'fr-FR', 'de-DE', 'zh-CN', 'zh-TW',
            'ja-JP', 'ko-KR', 'ar-SA', 'ru-RU', 'pt-BR', 'pt-PT',
            'it-IT', 'nl-NL', 'pl-PL', 'tr-TR', 'vi-VN', 'th-TH', 'id-ID',
            'sv-SE', 'da-DK', 'no-NO', 'fi-FI', 'cs-CZ', 'ro-RO',
            'el-GR', 'he-IL', 'hu-HU', 'uk-UA', 'bg-BG', 'hr-HR',
            'sk-SK', 'sl-SI', 'et-EE', 'lv-LV', 'lt-LT'
        ]
    
    def get_cost_estimate(self, duration_seconds: float) -> float:
        """
        Google Speech-to-Text pricing:
        - Standard: $0.006/15 seconds ($0.024/minute)
        - Enhanced: $0.009/15 seconds ($0.036/minute)
        """
        minutes = duration_seconds / 60
        
        # Using standard model pricing
        if self.config.get('use_enhanced', False):
            return minutes * 0.036
        else:
            return minutes * 0.024