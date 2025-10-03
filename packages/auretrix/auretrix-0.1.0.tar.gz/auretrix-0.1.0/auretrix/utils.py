"""
Utility functions for audio processing
"""

from pathlib import Path
from typing import Union
import logging

from auretrix.exceptions import AudioError, InvalidAudioFormatError

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = ['.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac', '.wma', '.webm']


def validate_audio_file(file_path: str) -> bool:
    """
    Validate audio file exists and has supported format
    
    Args:
        file_path: Path to audio file
    
    Returns:
        True if valid
    
    Raises:
        AudioError: If file invalid
    """
    path = Path(file_path)
    
    if not path.exists():
        raise AudioError(f"Audio file not found: {file_path}")
    
    if not path.is_file():
        raise AudioError(f"Not a file: {file_path}")
    
    if path.suffix.lower() not in SUPPORTED_FORMATS:
        raise InvalidAudioFormatError(
            f"Unsupported format: {path.suffix}. "
            f"Supported: {', '.join(SUPPORTED_FORMATS)}"
        )
    
    return True


def get_audio_duration(file_path: str) -> float:
    """
    Get audio file duration in seconds
    
    Args:
        file_path: Path to audio file
    
    Returns:
        Duration in seconds
    """
    try:
        from pydub import AudioSegment
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000.0  # Convert to seconds
    except ImportError:
        logger.warning("pydub not installed, cannot determine duration")
        return 0.0
    except Exception as e:
        logger.warning(f"Could not get duration: {e}")
        return 0.0


def convert_audio_format(
    input_path: str,
    output_format: str = 'wav',
    output_path: str = None
) -> str:
    """
    Convert audio to different format
    
    Args:
        input_path: Input audio file
        output_format: Target format (wav, mp3, etc.)
        output_path: Output file path (optional)
    
    Returns:
        Path to converted file
    """
    try:
        from pydub import AudioSegment
        
        audio = AudioSegment.from_file(input_path)
        
        if output_path is None:
            input_file = Path(input_path)
            output_path = input_file.parent / f"{input_file.stem}.{output_format}"
        
        audio.export(output_path, format=output_format)
        return str(output_path)
    
    except ImportError:
        raise AudioError("pydub required for format conversion")
    except Exception as e:
        raise AudioError(f"Conversion failed: {e}")


def split_audio(
    file_path: str,
    chunk_duration: int = 300,
    output_dir: str = None
) -> list:
    """
    Split long audio into chunks
    
    Args:
        file_path: Audio file path
        chunk_duration: Chunk duration in seconds
        output_dir: Output directory for chunks
    
    Returns:
        List of chunk file paths
    """
    try:
        from pydub import AudioSegment
        from pydub.utils import make_chunks
        
        audio = AudioSegment.from_file(file_path)
        chunk_length_ms = chunk_duration * 1000
        
        chunks = make_chunks(audio, chunk_length_ms)
        
        input_file = Path(file_path)
        if output_dir is None:
            output_dir = input_file.parent / "chunks"
        
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        chunk_paths = []
        for i, chunk in enumerate(chunks):
            chunk_path = output_dir / f"{input_file.stem}_chunk{i}.{input_file.suffix[1:]}"
            chunk.export(chunk_path, format=input_file.suffix[1:])
            chunk_paths.append(str(chunk_path))
        
        return chunk_paths
    
    except ImportError:
        raise AudioError("pydub required for audio splitting")
    except Exception as e:
        raise AudioError(f"Splitting failed: {e}")


def get_file_size_mb(file_path: str) -> float:
    """Get file size in megabytes"""
    return Path(file_path).stat().st_size / (1024 * 1024)


def is_audio_file(file_path: str) -> bool:
    """Check if file is a supported audio format"""
    return Path(file_path).suffix.lower() in SUPPORTED_FORMATS