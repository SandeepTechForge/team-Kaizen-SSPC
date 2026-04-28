import cv2
import pytesseract
import os
import sys

print("RUNNING FILE:", __file__)
print("WORKING DIRECTORY:", os.getcwd())

# ---- IMAGE PATH ----
image_path = r"D:\SMART PROGRAM CODING PEN\sample.png"
print("Trying to load image from:", image_path)

# ---- LOAD IMAGE ----
img = cv2.imread("D:\SMART PROGRAM CODING PEN\sample.png")

if img is None:
    print("❌ ERROR: Image not found or cannot be loaded!")
    sys.exit()

print("✅ Image loaded successfully")

# ---- OCR PROCESS ----
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

print("\n===== DETECTED TEXT =====\n")
print(text)
print("\n=========================\n")

# ---- SHOW IMAGE ----
cv2.imshow("OCR View", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()