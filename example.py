#!/usr/bin/env python3
"""
Example script demonstrating the LIVE-CAPTION tool with sample Hindi text.
This is useful for testing the functionality without audio input.
"""

from live_caption import LiveCaption

def main():
    """Main function to demonstrate the LIVE-CAPTION tool."""
    # Create a LiveCaption instance
    live_caption = LiveCaption()
    
    # Sample Hindi text (you would normally get this from audio)
    sample_hindi_text = "नमस्ते, मेरा नाम राहुल है और मैं दिल्ली से हूँ। मुझे भारतीय संस्कृति और इतिहास में रुचि है।"
    
    print("Sample Hindi Text:")
    print(sample_hindi_text)
    print("\nProcessing...")
    
    # Convert to Roman Hindi
    roman_hindi = live_caption.convert_to_roman_hindi(sample_hindi_text)
    
    # Generate English title
    english_title = live_caption.generate_english_title(roman_hindi)
    
    # Display results
    print("\n--- Results ---")
    print(f"Roman Hindi Transcription:\n{roman_hindi}")
    print(f"\nEnglish Title:\n{english_title}")

if __name__ == "__main__":
    main()