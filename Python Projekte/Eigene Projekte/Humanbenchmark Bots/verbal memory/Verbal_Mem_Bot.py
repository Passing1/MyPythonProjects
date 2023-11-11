import cv2
import pytesseract
from PIL import ImageGrab
import pyautogui
 
# Setze den Pfad für Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Liste, um bereits erkannte Wörter zu speichern
seen = []

# Hauptprogrammschleife
while True:
    # Erfasse einen Bildschirmbereich
    screenshot = ImageGrab.grab(bbox=(640, 470, 1340, 550))
    
    # Speichere den Screenshot als Bild
    screenshot.save("screenshot.png")
    
    # Lade das Bild mit OpenCV
    image = cv2.imread("screenshot.png")
    
    # Verwende Tesseract OCR, um Text aus dem Bild zu extrahieren
    word = pytesseract.image_to_string(image)

    # Überprüfe, ob das Wort bereits gesehen wurde
    if word not in seen:
        # Falls nicht, füge es zur Liste hinzu und klicke an eine Position
        seen.append(word)
        pyautogui.click(1030, 620)
    else:
        # Falls das Wort bereits gesehen wurde, klicke an eine andere Position
        pyautogui.click(860, 630)
