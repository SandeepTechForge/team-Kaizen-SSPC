import cv2
import easyocr
from ai_reconstructor import reconstruct_code
from ai_stage2 import stage2_reconstruct


def read_code_from_image(image_path):

    print("📷 Image reader called with:", image_path)

    # ---- LOAD IMAGE ----
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Image not found")
        return ""

    print("✅ Image loaded successfully")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ---- OCR ----
    reader = easyocr.Reader(['en'])
    results = reader.readtext(gray)

    raw_text = ""
    for (_, txt, conf) in results:
        if conf > 0.4:
            raw_text += txt + "\n"

    print("\n===== RAW OCR TEXT =====\n")
    print(raw_text)

    # ---- AI RECONSTRUCTION ----
    lines = raw_text.splitlines()
    final_code = reconstruct_code(lines)

    print("\n===== 🧠 AI RECONSTRUCTED CODE =====\n")
    print(final_code)

    # ---- STAGE 2 RECONSTRUCTION ----
    stage2_code = stage2_reconstruct(final_code.splitlines())

    # If Stage2 returns empty, keep original code
    if stage2_code.strip() != "":
        final_code = stage2_code

    print("\n===== 🧠 STAGE-2 AI RECONSTRUCTED CODE =====\n")
    print(final_code)

    # Return the final code to main.py
    return final_code