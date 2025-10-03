"""
Azure Cognitive Services Speech provider
"""

from typing import Dict, Any, List
import logging
import os

from auretrix.providers.base import BaseProvider
from auretrix.exceptions import ProviderError, APIKeyError
from auretrix.utils import get_audio_duration

logger = logging.getLogger(__name__)


class AzureProvider(BaseProvider):
    """Azure Cognitive Services Speech provider"""
    
    def __init__(self, api_key: str = None, region: str = None, **kwargs):
        """
        Initialize Azure Speech provider
        
        Args:
            api_key: Azure Speech API key
            region: Azure region (e.g., 'eastus', 'westeurope')
            **kwargs: Additional configuration
        """
        super().__init__(api_key, **kwargs)
        
        self.region = region or os.getenv('AZURE_SPEECH_REGION')
        
        if not self.api_key:
            raise APIKeyError(
                "Azure Speech API key required. "
                "Set AZURE_SPEECH_KEY environment variable or pass api_key parameter"
            )
        
        if not self.region:
            raise APIKeyError(
                "Azure region required. "
                "Set AZURE_SPEECH_REGION environment variable or pass region parameter"
            )
        
        self.speech_config = None
        self._init_config()
    
    def _init_config(self):
        """Initialize Azure Speech configuration"""
        try:
            import azure.cognitiveservices.speech as speechsdk
            
            self.speech_config = speechsdk.SpeechConfig(
                subscription=self.api_key,
                region=self.region
            )
            
            # Set default properties
            self.speech_config.speech_recognition_language = "en-US"
            self.speech_config.enable_dictation()
            
            logger.info(f"Azure Speech initialized for region: {self.region}")
            
        except ImportError:
            raise ProviderError(
                "Azure Speech SDK not installed. "
                "Install with: pip install azure-cognitiveservices-speech"
            )
        except Exception as e:
            raise ProviderError(f"Azure Speech initialization failed: {e}")
    
    def transcribe(self, audio_source: str, language: str = 'en-US', **kwargs) -> Dict[str, Any]:
        """
        Transcribe audio using Azure Speech
        
        Args:
            audio_source: Path to audio file
            language: Language code (e.g., 'hi-IN', 'en-US')
            **kwargs: Additional parameters
        
        Returns:
            Transcription result dictionary
        """
        if not self.speech_config:
            self._init_config()
        
        try:
            import azure.cognitiveservices.speech as speechsdk
            
            # Set language
            self.speech_config.speech_recognition_language = language
            
            # Configure audio input
            audio_config = speechsdk.audio.AudioConfig(filename=audio_source)
            
            # Create speech recognizer
            speech_recognizer = speechsdk.SpeechRecognizer(
                speech_config=self.speech_config,
                audio_config=audio_config
            )
            
            # Collect results
            all_results = []
            done = False
            
            def stop_cb(evt):
                nonlocal done
                done = True
            
            def recognized_cb(evt):
                if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                    all_results.append(evt.result)
            
            # Connect callbacks
            speech_recognizer.recognized.connect(recognized_cb)
            speech_recognizer.session_stopped.connect(stop_cb)
            speech_recognizer.canceled.connect(stop_cb)
            
            # Start continuous recognition
            speech_recognizer.start_continuous_recognition()
            
            # Wait for completion
            import time
            while not done:
                time.sleep(0.5)
            
            speech_recognizer.stop_continuous_recognition()
            
            # Process results
            if not all_results:
                return {
                    'text': '',
                    'confidence': 0.0,
                    'words': [],
                    'duration': get_audio_duration(audio_source),
                    'metadata': {}
                }
            
            # Combine transcripts
            full_text = ' '.join([result.text for result in all_results])
            
            # Calculate average confidence
            confidences = []
            all_words = []
            
            for result in all_results:
                # Extract detailed results if available
                if hasattr(result, 'json'):
                    import json
                    details = json.loads(result.json)
                    
                    if 'NBest' in details and details['NBest']:
                        best = details['NBest'][0]
                        confidences.append(best.get('Confidence', 0))
                        
                        # Extract words
                        if 'Words' in best:
                            for word_info in best['Words']:
                                all_words.append({
                                    'word': word_info['Word'],
                                    'start': word_info['Offset'] / 10000000.0,  # Convert to seconds
                                    'end': (word_info['Offset'] + word_info['Duration']) / 10000000.0,
                                    'confidence': word_info.get('Confidence', 0)
                                })
            
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0
            
            return {
                'text': full_text.strip(),
                'confidence': avg_confidence,
                'words': all_words,
                'duration': get_audio_duration(audio_source),
                'metadata': {
                    'language': language,
                    'region': self.region
                }
            }
        
        except Exception as e:
            raise ProviderError(f"Azure Speech transcription failed: {e}")
    
    def transcribe_streaming(self, audio_stream, language: str = 'en-US', **kwargs):
        """
        Real-time streaming transcription (future feature)
        
        Args:
            audio_stream: Audio stream object
            language: Language code
            **kwargs: Additional parameters
        """
        # TODO: Implement streaming support
        raise NotImplementedError("Streaming support coming soon!")
    
    def get_supported_languages(self) -> List[str]:
        """Get supported language codes for Azure"""
        return [
            'en-US', 'en-GB', 'en-IN', 'en-AU', 'en-CA', 'en-NZ', 'en-IE',
            'hi-IN', 'bn-IN', 'te-IN', 'mr-IN', 'ta-IN', 'gu-IN', 'kn-IN', 'ml-IN', 'pa-IN', 'ur-IN',
            'es-ES', 'es-MX', 'es-AR', 'es-CO', 'es-US',
            'fr-FR', 'fr-CA', 'de-DE', 'it-IT', 'pt-BR', 'pt-PT',
            'zh-CN', 'zh-TW', 'zh-HK', 'ja-JP', 'ko-KR',
            'ar-SA', 'ar-AE', 'ar-EG', 'ar-KW', 'ar-QA',
            'ru-RU', 'nl-NL', 'pl-PL', 'tr-TR', 'vi-VN', 'th-TH', 'id-ID',
            'sv-SE', 'da-DK', 'no-NO', 'fi-FI', 'cs-CZ', 'ro-RO',
            'el-GR', 'he-IL', 'hu-HU', 'uk-UA', 'bg-BG', 'hr-HR',
            'sk-SK', 'sl-SI', 'et-EE', 'lv-LV', 'lt-LT', 'sr-RS',
            'ca-ES', 'fa-IR', 'ms-MY', 'sw-KE', 'zu-ZA', 'af-ZA'
        ]
    
    def get_cost_estimate(self, duration_seconds: float) -> float:
        """
        Azure Speech-to-Text pricing:
        - Standard: $1.00 per audio hour
        - Custom: $1.40 per audio hour
        """
        hours = duration_seconds / 3600
        
        # Using standard pricing
        return hours * 1.00