"""
Simple transcription functions for quick usage
"""

from typing import Optional, Dict, Any
from pathlib import Path

from auretrix.speech import SpeechRecognizer


def transcribe_audio(
    audio_path: str,
    language: str = 'en-US',
    provider: Optional[str] = None,
    **kwargs
) -> str:
    """
    Quick transcription of audio file
    
    Args:
        audio_path: Path to audio file
        language: Language code (default: 'en-US')
        provider: Specific provider to use (optional)
        **kwargs: Additional parameters
    
    Returns:
        Transcribed text
    
    Example:
        >>> text = transcribe_audio('meeting.mp3', language='hi-IN')
        >>> print(text)
    """
    providers = [provider] if provider else None
    
    recognizer = SpeechRecognizer(
        providers=providers,
        auto_fallback=True,
        **kwargs
    )
    
    result = recognizer.recognize(audio_path, language=language)
    return result['text']


def transcribe_file(
    audio_path: str,
    output_format: str = 'txt',
    language: str = 'en-US',
    include_timestamps: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """
    Transcribe audio and save to file
    
    Args:
        audio_path: Path to audio file
        output_format: Output format ('txt', 'json', 'srt', 'vtt')
        language: Language code
        include_timestamps: Include word-level timestamps
        **kwargs: Additional parameters
    
    Returns:
        Dictionary with transcription and output file path
    
    Example:
        >>> result = transcribe_file(
        ...     'podcast.mp3',
        ...     output_format='srt',
        ...     language='en-US',
        ...     include_timestamps=True
        ... )
        >>> print(f"Saved to: {result['output_file']}")
    """
    recognizer = SpeechRecognizer(auto_fallback=True, **kwargs)
    
    result = recognizer.recognize(
        audio_path,
        language=language,
        include_timestamps=include_timestamps
    )
    
    # Generate output filename
    audio_file = Path(audio_path)
    output_file = audio_file.parent / f"{audio_file.stem}.{output_format}"
    
    # Save based on format
    if output_format == 'txt':
        _save_txt(result, output_file)
    elif output_format == 'json':
        _save_json(result, output_file)
    elif output_format == 'srt':
        _save_srt(result, output_file)
    elif output_format == 'vtt':
        _save_vtt(result, output_file)
    else:
        raise ValueError(f"Unsupported format: {output_format}")
    
    return {
        'text': result['text'],
        'output_file': str(output_file),
        'language': language,
        'provider': result['provider']
    }


def _save_txt(result: Dict, output_file: Path):
    """Save as plain text"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['text'])


def _save_json(result: Dict, output_file: Path):
    """Save as JSON"""
    import json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def _save_srt(result: Dict, output_file: Path):
    """Save as SRT subtitle format"""
    words = result.get('words', [])
    if not words:
        raise ValueError("Timestamps required for SRT format")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, word in enumerate(words, 1):
            start = _format_timestamp(word['start'])
            end = _format_timestamp(word['end'])
            f.write(f"{i}\n{start} --> {end}\n{word['word']}\n\n")


def _save_vtt(result: Dict, output_file: Path):
    """Save as WebVTT format"""
    words = result.get('words', [])
    if not words:
        raise ValueError("Timestamps required for VTT format")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("WEBVTT\n\n")
        for word in words:
            start = _format_timestamp(word['start'], vtt=True)
            end = _format_timestamp(word['end'], vtt=True)
            f.write(f"{start} --> {end}\n{word['word']}\n\n")


def _format_timestamp(seconds: float, vtt: bool = False) -> str:
    """Format timestamp for subtitles"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    
    if vtt:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"
    else:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def batch_transcribe(
    audio_files: list,
    language: str = 'en-US',
    output_dir: Optional[str] = None,
    **kwargs
) -> list:
    """
    Transcribe multiple audio files
    
    Args:
        audio_files: List of audio file paths
        language: Language code
        output_dir: Directory to save transcriptions
        **kwargs: Additional parameters
    
    Returns:
        List of transcription results
    """
    recognizer = SpeechRecognizer(auto_fallback=True, **kwargs)
    results = []
    
    for audio_file in audio_files:
        try:
            result = recognizer.recognize(audio_file, language=language)
            results.append({
                'file': audio_file,
                'success': True,
                'text': result['text'],
                'provider': result['provider']
            })
        except Exception as e:
            results.append({
                'file': audio_file,
                'success': False,
                'error': str(e)
            })
    
    return results