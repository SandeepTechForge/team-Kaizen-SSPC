# voice_listener.py
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import tempfile
import wavio

def listen(duration=5, fs=44100):
    """
    Records audio from microphone for duration seconds
    and returns audio as an AudioData object for SpeechRecognition.
    """
    print(f"Recording for {duration} seconds...")
    
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # wait until recording is finished

    # Save to temporary WAV file
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wavio.write(temp_file.name, recording, fs, sampwidth=2)
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_file.name) as source:
        audio_data = recognizer.record(source)
    
    return audio_data