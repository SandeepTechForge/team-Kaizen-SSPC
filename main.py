from image_reader import read_code_from_image
from voice_engine import speak
from error_explainer import explain_error
from language_detector import detect_language
from code_executor import execute_python, execute_cpp, execute_java
from voice_listener import listen
import speech_recognition as sr
import os
import time


def answer_question(question):
    """
    Sensei answers student questions.
    You can expand this logic later or integrate AI.
    """
    question = question.lower()

    if "error" in question:
        speak("Check your brackets, quotes, or colons carefully.")

    elif "line" in question:
        speak("Look closely at the line where the syntax error occurred.")

    elif "python" in question or "c++" in question or "java" in question:
        speak(f"You asked about {question}. Remember to follow the syntax rules for that language.")

    else:
        speak("I heard your question, but I need more info to answer it.")


if __name__ == "__main__":

    recognizer = sr.Recognizer()

    try:
        speak("SMART SENSEI STYLE CODE COMPILER ACTIVATED.")

        print("Sensei is listening... Speak now!")
        audio_data = listen(duration=5)

        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)

        except sr.UnknownValueError:
            print("Sensei could not understand what you said.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        # -------- IMAGE SOURCE --------
        image_path = os.path.join(os.path.dirname(__file__), "sample.png")

        speak("Reading image and extracting code.")

        # -------- OCR READING --------
        result = read_code_from_image(image_path)

        print("===== RAW OCR TEXT =====")
        print(result)

        # -------- CLEAN OCR TEXT --------
        lines = result.split("\n")
        clean_lines = []

        for line in lines:
            line = line.strip()
            if line and line.lower() != "python":
                clean_lines.append(line)

        result = "\n".join(clean_lines)

        print("\n===== CLEANED CODE =====")
        print(repr(result))

        speak("Analyzing extracted code.")

        # -------- CHECK IF OCR RETURNED CODE --------
        if result.strip() == "":
            print("❌ No code detected from image.")
            speak("No code detected in the image.")
            time.sleep(2)

        else:

            # -------- LANGUAGE DETECTION --------
            language = detect_language(result)
            print("Detected language:", language)

            # -------- EXECUTION BASED ON LANGUAGE --------
            if language == "python":
                status, error = execute_python(result)

            elif language == "cpp":
                status, error = execute_cpp(result)

            elif language == "java":
                status, error = execute_java(result)

            else:
                speak("I could not recognize the programming language.")
                status = "error"
                error = "Unknown programming language"

            # -------- HANDLE RESULT --------
            if status == "success":

                print("Code executed successfully.")
                speak("Code executed successfully. No errors detected.")
                time.sleep(2)

            else:


                try:
                    explanation = explain_error(error)

                except Exception:
                    explanation = "There is an error in your program but I could not fully analyze it."

                print("Execution Error:", explanation)

                speak(explanation)
                speak("Please correct your code and try again.")

                time.sleep(3)

        # -------- FOLLOW-UP QUESTIONS --------
        while True:

            speak("Do you have another question?")

            audio_data = listen(duration=7)

            try:
                question = recognizer.recognize_google(audio_data)

            except sr.UnknownValueError:
                speak("Sorry student, I could not understand what you said.")
                continue

            except sr.RequestError:
                speak("Sorry student, there was a problem with the recognition service.")
                continue

            if question.lower() in ["no", "exit", "nothing"]:
                speak("Okay student, session ended. Goodbye!")
                break

            else:
                answer_question(question)

    except Exception as e:

        # -------- SYSTEM LEVEL ERROR --------
        try:
            explanation = explain_error(e)

        except Exception:
            explanation = "A system error occurred while analyzing your code."

        print("System Error:", explanation)

        speak("A system error occurred.")
        speak(explanation)

        time.sleep(3)