"""
AssemblyAI provider
"""

from typing import Dict, Any, List
import time
import logging

from auretrix.providers.base import BaseProvider
from auretrix.exceptions import ProviderError, APIKeyError
from auretrix.utils import get_audio_duration

logger = logging.getLogger(__name__)


class AssemblyAIProvider(BaseProvider):
    """AssemblyAI transcription provider"""
    
    def __init__(self, api_key: str = None, **kwargs):
        """
        Initialize AssemblyAI provider
        
        Args:
            api_key: AssemblyAI API key
            **kwargs: Additional configuration
        """
        super().__init__(api_key, **kwargs)
        
        if not self.api_key:
            raise APIKeyError(
                "AssemblyAI API key required. "
                "Get it from: https://www.assemblyai.com/"
            )
        
        self.base_url = "https://api.assemblyai.com/v2"
        self.headers = {
            "authorization": self.api_key,
            "content-type": "application/json"
        }
    
    def transcribe(self, audio_source: str, language: str = 'en', **kwargs) -> Dict[str, Any]:
        """
        Transcribe audio using AssemblyAI
        
        Args:
            audio_source: Path to audio file
            language: Language code (AssemblyAI uses 2-letter codes)
            **kwargs: Additional parameters
        
        Returns:
            Transcription result dictionary
        """
        try:
            import requests
        except ImportError:
            raise ProviderError("requests library required. Install with: pip install requests")
        
        try:
            # Extract 2-letter language code (hi-IN -> hi)
            lang_code = language.split('-')[0] if '-' in language else language
            
            # Step 1: Upload audio file
            upload_url = self._upload_file(audio_source, requests)
            
            # Step 2: Create transcription job
            transcript_id = self._create_transcript(
                upload_url,
                lang_code,
                requests,
                **kwargs
            )
            
            # Step 3: Poll for completion
            transcript_data = self._poll_transcript(transcript_id, requests)
            
            # Step 4: Format response
            return self._format_response(transcript_data, audio_source)
        
        except Exception as e:
            raise ProviderError(f"AssemblyAI transcription failed: {e}")
    
    def _upload_file(self, audio_path: str, requests) -> str:
        """Upload audio file to AssemblyAI"""
        upload_endpoint = f"{self.base_url}/upload"
        
        with open(audio_path, 'rb') as f:
            response = requests.post(
                upload_endpoint,
                headers=self.headers,
                data=f
            )
        
        response.raise_for_status()
        return response.json()['upload_url']
    
    def _create_transcript(
        self,
        audio_url: str,
        language: str,
        requests,
        **kwargs
    ) -> str:
        """Create transcription job"""
        transcript_endpoint = f"{self.base_url}/transcript"
        
        json_data = {
            "audio_url": audio_url,
            "language_code": language,
            "punctuate": kwargs.get('punctuate', True),
            "format_text": kwargs.get('format_text', True),
            "speaker_labels": kwargs.get('speaker_labels', False),
            "auto_chapters": kwargs.get('auto_chapters', False),
            "entity_detection": kwargs.get('entity_detection', False),
            "sentiment_analysis": kwargs.get('sentiment_analysis', False),
            "auto_highlights": kwargs.get('auto_highlights', False),
        }
        
        response = requests.post(
            transcript_endpoint,
            json=json_data,
            headers=self.headers
        )
        
        response.raise_for_status()
        return response.json()['id']
    
    def _poll_transcript(self, transcript_id: str, requests, timeout: int = 300) -> dict:
        """Poll for transcription completion"""
        polling_endpoint = f"{self.base_url}/transcript/{transcript_id}"
        
        start_time = time.time()
        
        while True:
            response = requests.get(polling_endpoint, headers=self.headers)
            response.raise_for_status()
            
            transcript_data = response.json()
            status = transcript_data['status']
            
            if status == 'completed':
                return transcript_data
            elif status == 'error':
                raise ProviderError(f"Transcription error: {transcript_data.get('error')}")
            
            # Check timeout
            if time.time() - start_time > timeout:
                raise ProviderError("Transcription timeout")
            
            # Wait before next poll
            time.sleep(3)
    
    def _format_response(self, data: dict, audio_path: str) -> Dict[str, Any]:
        """Format AssemblyAI response to standard format"""
        words = []
        
        if 'words' in data:
            for word_data in data['words']:
                words.append({
                    'word': word_data['text'],
                    'start': word_data['start'] / 1000.0,  # Convert to seconds
                    'end': word_data['end'] / 1000.0,
                    'confidence': word_data.get('confidence', 0)
                })
        
        return {
            'text': data.get('text', '').strip(),
            'confidence': data.get('confidence', 0),
            'words': words,
            'duration': get_audio_duration(audio_path),
            'metadata': {
                'language': data.get('language_code'),
                'audio_duration': data.get('audio_duration'),
                'utterances': data.get('utterances', []),
                'chapters': data.get('chapters', []),
                'entities': data.get('entities', []),
                'sentiment_analysis_results': data.get('sentiment_analysis_results', [])
            }
        }
    
    def get_supported_languages(self) -> List[str]:
        """
        AssemblyAI supports 99+ languages
        Using 2-letter codes
        """
        return [
            'en', 'es', 'fr', 'de', 'it', 'pt', 'nl', 'hi', 'ja', 'zh', 'fi',
            'ko', 'pl', 'ru', 'tr', 'uk', 'vi', 'ar', 'da', 'he', 'id', 'ms',
            'no', 'sv', 'th', 'bg', 'ca', 'cs', 'el', 'et', 'fa', 'hr', 'hu',
            'is', 'ka', 'kk', 'lt', 'lv', 'mk', 'ro', 'sk', 'sl', 'sr', 'ta',
            'te', 'bn', 'mr', 'gu', 'kn', 'ml', 'pa', 'ur'
        ]
    
    def get_cost_estimate(self, duration_seconds: float) -> float:
        """
        AssemblyAI pricing:
        - Core: $0.00025/second ($0.015/minute)
        - Best: $0.00037/second ($0.0222/minute)
        """
        # Using Core pricing
        return duration_seconds * 0.00025