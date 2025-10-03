# 🎙️ Auretrix

**Unified Speech Recognition Library** - Simplify speech-to-text with multi-provider support, auto-fallback, and Indian language focus.

[![PyPI version](https://badge.fury.io/py/auretrix.svg)](https://badge.fury.io/py/auretrix)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Features

- 🔄 **Multi-Provider Support** - Whisper, Google Speech, AssemblyAI, Azure
- 🛡️ **Auto-Fallback** - Automatically switches providers on failure
- 💰 **Cost Optimization** - Intelligently chooses cheapest provider
- 🇮🇳 **Indian Languages** - First-class support for Hindi, Tamil, Telugu, and 10+ Indian languages
- 📝 **Multiple Formats** - Export to TXT, JSON, SRT, VTT
- ⚡ **Simple API** - One-liner transcription
- 🔧 **Flexible** - Use local models or cloud APIs

---

## 📦 Installation

```bash
# Basic installation
pip install auretrix

# With Whisper support (local transcription)
pip install auretrix[whisper]

# With all providers
pip install auretrix[all]
```

---

## 🎯 Quick Start

### Simple Transcription

```python
from auretrix import transcribe_audio

# One-liner transcription
text = transcribe_audio('meeting.mp3', language='hi-IN')
print(text)
```

### Advanced Usage

```python
from auretrix import SpeechRecognizer

# Initialize with multiple providers
recognizer = SpeechRecognizer(
    providers=['whisper', 'google', 'assemblyai'],
    auto_fallback=True,
    optimize_cost=True
)

# Transcribe with detailed results
result = recognizer.recognize('podcast.mp3', language='en-US')

print(f"Text: {result['text']}")
print(f"Provider: {result['provider']}")
print(f"Confidence: {result['confidence']}")
```

### Batch Transcription

```python
from auretrix import batch_transcribe

files = ['audio1.mp3', 'audio2.wav', 'audio3.m4a']
results = batch_transcribe(files, language='hi-IN')

for result in results:
    print(f"{result['file']}: {result['text']}")
```

### Export to Subtitles

```python
from auretrix import transcribe_file

# Generate SRT subtitles
result = transcribe_file(
    'video.mp4',
    output_format='srt',
    language='en-US',
    include_timestamps=True
)

print(f"Subtitles saved to: {result['output_file']}")
```

---

## 🌏 Language Support

### Indian Languages

```python
from auretrix.languages import INDIAN_LANGUAGES, list_indian_languages

# See all supported Indian languages
languages = list_indian_languages()
for lang in languages:
    print(f"{lang['name']} ({lang['native']}): {lang['code']}")
```

**Supported Indian Languages:**
- 🇮🇳 Hindi (हिन्दी) - `hi-IN`
- 🇮🇳 Bengali (বাংলা) - `bn-IN`
- 🇮🇳 Telugu (తెలుగు) - `te-IN`
- 🇮🇳 Marathi (मराठी) - `mr-IN`
- 🇮🇳 Tamil (தமிழ்) - `ta-IN`
- 🇮🇳 Gujarati (ગુજરાતી) - `gu-IN`
- 🇮🇳 Kannada (ಕನ್ನಡ) - `kn-IN`
- 🇮🇳 Malayalam (മലയാളം) - `ml-IN`
- 🇮🇳 Punjabi (ਪੰਜਾਬੀ) - `pa-IN`
- 🇮🇳 Urdu (اردو) - `ur-IN`
- And more...

---

## 🔑 Provider Setup

### Whisper (Local - Free)

```python
from auretrix import SpeechRecognizer

# Use local Whisper model (no API key needed)
recognizer = SpeechRecognizer(
    providers=['whisper'],
    use_local=True,
    model='base'  # Options: tiny, base, small, medium, large
)
```

### Google Speech API

```bash
export GOOGLE_SPEECH_API_KEY='your-api-key'
```

```python
recognizer = SpeechRecognizer(providers=['google'])
```

### AssemblyAI

```bash
export ASSEMBLYAI_API_KEY='your-api-key'
```

### Azure Speech

```bash
export AZURE_SPEECH_KEY='your-key'
export AZURE_SPEECH_REGION='your-region'
```

---

## 💡 Use Cases

### 1. Podcast Transcription
```python
result = transcribe_file(
    'podcast_episode.mp3',
    output_format='txt',
    language='en-US'
)
```

### 2. Meeting Notes
```python
recognizer = SpeechRecognizer(providers=['whisper'])
result = recognizer.recognize('team_meeting.wav', language='hi-IN')
```

### 3. Video Subtitles
```python
transcribe_file(
    'video.mp4',
    output_format='srt',
    include_timestamps=True
)
```

### 4. Multi-Language Content
```python
# Detect and transcribe multiple languages
for audio_file, lang in [('hindi.mp3', 'hi-IN'), ('tamil.mp3', 'ta-IN')]:
    text = transcribe_audio(audio_file, language=lang)
    print(f"{lang}: {text}")
```

---

## 🛠️ Configuration

### Environment Variables

```bash
# Optional API keys
export GOOGLE_SPEECH_API_KEY='...'
export ASSEMBLYAI_API_KEY='...'
export AZURE_SPEECH_KEY='...'
export AZURE_SPEECH_REGION='...'
```

### Provider Priority

```python
recognizer = SpeechRecognizer(
    providers=['whisper', 'google', 'assemblyai'],  # Priority order
    auto_fallback=True  # Auto switch on failure
)
```

### Cost Optimization

```python
recognizer = SpeechRecognizer(
    optimize_cost=True  # Chooses cheapest provider based on audio length
)
```

---

## 📊 Provider Comparison

| Provider | Cost | Speed | Languages | Local |
|----------|------|-------|-----------|-------|
| **Whisper** | Free | Fast | 99+ | ✅ |
| **Google** | $0.024/min | Fast | 125+ | ❌ |
| **AssemblyAI** | $0.00025/sec | Medium | 99+ | ❌ |
| **Azure** | $1/hour | Fast | 100+ | ❌ |

---

## 🤝 Contributing

Contributions are welcome! Check out our [Contributing Guide](CONTRIBUTING.md).

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

---

## 🔗 Links

- **Website**: [auretrix.com](https://auretrix.com)
- **Documentation**: [docs.auretrix.com](https://docs.auretrix.com)
- **GitHub**: [github.com/auretrix/auretrix](https://github.com/auretrix/auretrix)
- **PyPI**: [pypi.org/project/auretrix](https://pypi.org/project/auretrix)

---

## 💬 Support

- 📧 Email: contact@auretrix.com
- 💬 Discord: [Join our community](https://discord.gg/auretrix)
- 🐛 Issues: [GitHub Issues](https://github.com/auretrix/auretrix/issues)

---

**Made with ❤️ by Auretrix AI**

*Building AI tools for creators, by creators.*