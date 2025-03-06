#!/usr/bin/env python3
"""
LIVE-CAPTION: A tool to convert speech to Roman Hindi text and generate English titles.

This script provides functionality to:
1. Convert spoken Hindi to Roman Hindi text (Hindi written using English letters)
2. Generate a concise English title based on the transcribed text
"""

import os
import sys
import argparse
import speech_recognition as sr
from googletrans import Translator
import re

class LiveCaption:
    def __init__(self):
        """Initialize the LiveCaption object with necessary components."""
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        
    def transcribe_audio(self, audio_file_path=None):
        """
        Transcribe speech from an audio file or microphone input.
        
        Args:
            audio_file_path: Path to the audio file (optional, uses microphone if None)
            
        Returns:
            Transcribed text in the original language
        """
        try:
            if audio_file_path:
                # Use audio file as source
                with sr.AudioFile(audio_file_path) as source:
                    audio_data = self.recognizer.record(source)
            else:
                # Use microphone as source
                print("Listening... Speak now.")
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio_data = self.recognizer.listen(source)
                print("Processing speech...")
            
            # Recognize speech using Google Speech Recognition
            # Assuming Hindi speech input, but can be modified for other languages
            text = self.recognizer.recognize_google(audio_data, language="hi-IN")
            return text
            
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def convert_to_roman_hindi(self, hindi_text):
        """
        Convert Hindi text to Roman Hindi (Hindi written in English letters).
        
        Args:
            hindi_text: Text in Hindi
            
        Returns:
            Text in Roman Hindi (Hindi written using English letters)
        """
        if not hindi_text:
            return None
            
        # For accurate romanization, we'll use Google Translate's romanization
        # First, we detect the language to confirm it's Hindi
        detected = self.translator.detect(hindi_text)
        
        if detected.lang == 'hi':
            # For Hindi text, we can use transliteration
            # This is a simple approach - for production, consider using dedicated
            # transliteration libraries like indic-transliteration
            roman_text = self.translator.translate(hindi_text, src='hi', dest='en').pronunciation
            
            # If pronunciation is None (which can happen), use a fallback approach
            if not roman_text:
                # Fallback: translate to English then back to Hindi for romanization
                roman_text = self.translator.translate(hindi_text, src='hi', dest='en').text
                
            return roman_text
        else:
            # If the text is not in Hindi, return as is
            return hindi_text
    
    def generate_english_title(self, roman_hindi_text):
        """
        Generate a concise English title based on the Roman Hindi text.
        
        Args:
            roman_hindi_text: Text in Roman Hindi
            
        Returns:
            A concise English title
        """
        if not roman_hindi_text:
            return None
            
        # Translate the Roman Hindi text to English
        english_text = self.translator.translate(roman_hindi_text, dest='en').text
        
        # Generate a concise title (first 50 characters or first sentence)
        title = english_text[:50]
        
        # Try to find the first sentence
        first_sentence = re.split(r'[.!?]', english_text)[0]
        if first_sentence and len(first_sentence) < 100:
            title = first_sentence
            
        return title.strip()
    
    def process_speech(self, audio_file_path=None):
        """
        Process speech to generate Roman Hindi text and English title.
        
        Args:
            audio_file_path: Path to the audio file (optional, uses microphone if None)
            
        Returns:
            Tuple of (roman_hindi_text, english_title)
        """
        # Step 1: Transcribe the audio
        hindi_text = self.transcribe_audio(audio_file_path)
        if not hindi_text:
            return None, None
            
        # Step 2: Convert to Roman Hindi
        roman_hindi_text = self.convert_to_roman_hindi(hindi_text)
        if not roman_hindi_text:
            return None, None
            
        # Step 3: Generate English title
        english_title = self.generate_english_title(roman_hindi_text)
        
        return roman_hindi_text, english_title

def main():
    """Main function to run the LiveCaption tool."""
    parser = argparse.ArgumentParser(description="Convert speech to Roman Hindi text and generate English titles")
    parser.add_argument("-f", "--file", help="Path to the audio file (if not provided, uses microphone)")
    args = parser.parse_args()
    
    live_caption = LiveCaption()
    roman_hindi, english_title = live_caption.process_speech(args.file)
    
    if roman_hindi and english_title:
        print("\n--- Results ---")
        print(f"Roman Hindi Transcription:\n{roman_hindi}")
        print(f"\nEnglish Title:\n{english_title}")
    else:
        print("Failed to process speech. Please try again.")

if __name__ == "__main__":
    main()