<header>

# LIVE-CAPTION

A Python tool that converts speech into text with the following features:

1. **Roman Hindi Transcription**: Converts spoken Hindi words into Hindi using English letters (Roman Hindi), ensuring accurate phonetic representation without using Hindi script.

2. **English Title Generation**: Based on the transcribed text, generates a concise and relevant English title summarizing the main idea of the speech.

## Requirements

- Python 3.6 or higher
- Internet connection (for Google Speech Recognition and Translation APIs)
- Microphone (for live speech input) or audio files

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/LIVE-CAPTION.git
   cd LIVE-CAPTION
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Using Microphone Input

To transcribe live speech from your microphone:

```
python live_caption.py
```

The program will listen for speech, transcribe it to Roman Hindi, and generate an English title.

### Using Audio File Input

To transcribe speech from an audio file:

```
python live_caption.py -f path/to/your/audio/file.wav
```

Note: The audio file should be in a format supported by the SpeechRecognition library (WAV, AIFF, FLAC).

## Example Output

```
--- Results ---
Roman Hindi Transcription:
namaste, mera naam rahul hai aur main dilli se hoon.

English Title:
Hello, my name is Rahul and I am from Delhi.
```

## Features

- **Speech Recognition**: Uses Google's Speech Recognition API for accurate speech-to-text conversion.
- **Language Detection**: Automatically detects if the speech is in Hindi.
- **Roman Hindi Conversion**: Converts Hindi text to Roman Hindi (Hindi written using English letters).
- **English Title Generation**: Creates a concise English title based on the transcribed text.
- **Error Handling**: Robust error handling for various speech recognition scenarios.

## Limitations

- Requires an internet connection for speech recognition and translation.
- The accuracy of transcription depends on the quality of the audio and clarity of speech.
- Currently optimized for Hindi language input, but can be extended to other languages.

## License

This project is licensed under the MIT License - see the LICENSE file for details.