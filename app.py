import customtkinter as ctk
from tkinter import filedialog
from error_explainer import explain_error
from image_reader import read_code_from_image
from language_detector import detect_language
from code_executor import execute_python, execute_cpp, execute_java
from voice_engine import speak
from voice_listener import listen
import speech_recognition as sr

# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create window
app = ctk.CTk()
app.title("SMART SENSEI STYLE PROGRAM COMPILER")
app.geometry("1000x850")

# Scrollable Frame
scrollable_frame = ctk.CTkScrollableFrame(app, width=950, height=800)
scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

ocr_result = ""

# Upload Function
def upload_image():
    global ocr_result

    file_path = filedialog.askopenfilename(
        title="Select Code Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if file_path:
        status_label.configure(text="Image Selected")

        try:
            ocr_result = read_code_from_image(file_path)

            code_box.delete("1.0", "end")
            code_box.insert("end", ocr_result)

            speak("Image uploaded successfully")

        except Exception as e:
            code_box.delete("1.0", "end")
            code_box.insert("end", f"Error: {e}")

# Execute Function
def execute_code():
    code = code_box.get("1.0", "end")

    try:
        language = detect_language(code)

        if language == "python":
            status, output = execute_python(code)

        elif language == "cpp":
            status, output = execute_cpp(code)

        elif language == "java":
            status, output = execute_java(code)

        else:
            status = "error"
            output = "Language not recognized"

        # Show execution result
        result_box.delete("1.0", "end")
        result_box.insert("end", output)

        speak("Code execution completed")

        # Error Explanation
        if status != "success":
            explanation = explain_error(output)

            explanation_box.delete("1.0", "end")
            explanation_box.insert("end", explanation)

            speak("Student, I detected an error in your program")
            speak(explanation)

        else:
            explanation_box.delete("1.0", "end")
            explanation_box.insert("end", "No errors detected")

            speak("Great job student. No errors detected")

    except Exception as e:
        result_box.delete("1.0", "end")
        result_box.insert("end", str(e))

# Voice Question Function
def ask_sensei():
    recognizer = sr.Recognizer()

    try:
        speak("I am listening student. Ask your question.")

        audio = listen(duration=6)
        question = recognizer.recognize_google(audio)

        voice_box.delete("1.0", "end")
        voice_box.insert("end", f"You Asked: {question}\n")

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

# Title
label = ctk.CTkLabel(
    scrollable_frame,
    text="SMART SENSEI STYLE PROGRAM COMPILER",
    font=("Arial", 24, "bold")
)
label.pack(pady=15)

# Button States
voice_active = False
run_active = False

# Toggle Voice Button

def toggle_voice():
    global voice_active

    voice_active = not voice_active

    if voice_active:
        voice_button.configure(text="Ask Sensei ON")
        ask_sensei()
    else:
        voice_button.configure(text="Ask Sensei OFF")

# Toggle Run Button

def toggle_run():
    global run_active

    run_active = not run_active

    if run_active:
        execute_button.configure(text="Run Code ON")
        execute_code()
    else:
        execute_button.configure(text="Run Code OFF")

# Clear Function
def clear_all():
    code_box.delete("1.0", "end")
    result_box.delete("1.0", "end")
    explanation_box.delete("1.0", "end")
    voice_box.delete("1.0", "end")

    status_label.configure(text="No image selected")

# Upload Button
upload_button = ctk.CTkButton(
    scrollable_frame,
    text="Upload Code Image",
    command=upload_image,
    width=220,
    height=45
)
upload_button.pack(pady=8)

# Execute Button
execute_button = ctk.CTkButton(
    scrollable_frame,
    text="Run Code",
    command=toggle_run,
    width=220,
    height=45
)
execute_button.pack(pady=8)

# Voice Button
voice_button = ctk.CTkButton(
    scrollable_frame,
    text="Ask Sensei",
    command=toggle_voice,
    width=220,
    height=45
)
voice_button.pack(pady=8)

# Clear Button
clear_button = ctk.CTkButton(
    scrollable_frame,
    text="Clear All",
    command=clear_all,
    width=220,
    height=45
)
clear_button.pack(pady=8)

# Status Label
status_label = ctk.CTkLabel(
    scrollable_frame,
    text="No image selected",
    font=("Arial", 14)
)
status_label.pack(pady=5)

# Code Output Title
output_title = ctk.CTkLabel(
    scrollable_frame,
    text="Extracted Code",
    font=("Arial", 18, "bold")
)
output_title.pack(pady=5)

# Code Box
code_box = ctk.CTkTextbox(
    scrollable_frame,
    width=800,
    height=220,
    font=("Consolas", 14)
)
code_box.pack(pady=10)

# Result Title
result_title = ctk.CTkLabel(
    scrollable_frame,
    text="Execution Result",
    font=("Arial", 18, "bold")
)
result_title.pack(pady=5)

# Result Box
result_box = ctk.CTkTextbox(
    scrollable_frame,
    width=800,
    height=150,
    font=("Consolas", 13)
)
result_box.pack(pady=10)

# Explanation Title
explanation_title = ctk.CTkLabel(
    scrollable_frame,
    text="Error Explanation",
    font=("Arial", 18, "bold")
)
explanation_title.pack(pady=5)

# Explanation Box
explanation_box = ctk.CTkTextbox(
    scrollable_frame,
    width=800,
    height=120,
    font=("Consolas", 13)
)
explanation_box.pack(pady=10)

# Voice Title
voice_title = ctk.CTkLabel(
    scrollable_frame,
    text="Sensei Voice Interaction",
    font=("Arial", 18, "bold")
)
voice_title.pack(pady=5)

# Voice Box
voice_box = ctk.CTkTextbox(
    scrollable_frame,
    width=800,
    height=100,
    font=("Consolas", 13)
)
voice_box.pack(pady=10)

# Run App
app.mainloop()