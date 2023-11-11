import cv2
import pytesseract
from PIL import ImageGrab
import keyboard

# Setze den Pfad für Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Endlose Schleife für die Hauptausführung des Programms
while True:
    # Überprüfen, ob die "esc"-Taste gedrückt wurde
    if keyboard.read_key() == "esc":
        # Erfassen des Bildschirmbereichs zwischen den Koordinaten (350, 480) und (1550, 700)
        screenshot = ImageGrab.grab(bbox=(350, 480, 1550, 700))
        
        # Speichern des Screenshots als "screenshot.png"
        screenshot.save("screenshot.png")
        
        # Einlesen des gespeicherten Screenshots mit OpenCV
        image = cv2.imread("screenshot.png")
        
        # Extrahieren des Textes aus dem Bild mithilfe von Tesseract
        text = pytesseract.image_to_string(image).replace("\n", " ")

        # Überprüfen, ob der extrahierte Text mit "|" oder "[" beginnt
        if text[0] == "|" or text[0] == "[":
            # Ersetzen von "|" durch "I" und Ausgabe des Textes ab dem zweiten Zeichen
            fex = text.replace("|", "I")
            print(fex[1:])
            # Schreiben des Textes in die Tastatur (ohne das erste Zeichen)
            keyboard.write(fex[1:])
        else:
            # Ersetzen von "|" durch "I" und Ausgabe des gesamten Textes
            fex = text.replace("|", "I")
            print(fex)
            # Schreiben des Textes in die Tastatur
            keyboard.write(fex)
    
    # Überprüfen, ob die "alt"-Taste gedrückt wurde, um die Schleife zu beenden
    if keyboard.read_key() == "alt":
        break
