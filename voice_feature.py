from voice_engine import speak
from voice_listener import listen
import speech_recognition as sr


def ask_sensei(voice_box):
    recognizer = sr.Recognizer()

    try:
        speak("I am listening student. Ask your question.")

        audio = listen(duration=6)
        question = recognizer.recognize_google(audio)

        voice_box.delete("1.0", "end")
        voice_box.insert("end", f"You Asked: {question}")

        question_lower = question.lower()

        if "error" in question_lower:
            response = "Check your syntax, brackets, or indentation carefully."

        elif "python" in question_lower:
            response = "Python depends heavily on indentation and syntax."

        elif "line" in question_lower:
            response = "Look at the line number shown in the execution result."

        else:
            response = "Please ask a programming related question."

        voice_box.insert("end", f"Sensei: {response}")
        speak(response)

    except Exception:
        voice_box.delete("1.0", "end")
        voice_box.insert("end", "Voice could not be recognized")