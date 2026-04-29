from voice_listener import listen_to_student
from voice_engine import speak


speak("Student, ask your programming doubt.")

question = listen_to_student()

if question:

    speak("You asked")
    speak(question)

else:

    speak("I could not understand your question.")