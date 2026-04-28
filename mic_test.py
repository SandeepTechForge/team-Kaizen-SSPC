# mic_test.py
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import tempfile
import wavio

# Function to record from microphone
def listen(duration=5, fs=44100):
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


# -------- TEST MICROPHONE --------
if __name__ == "__main__":
    audio_data = listen(duration=5)
    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error accessing Google Speech Recognition; {e}")