from PIL import ImageGrab, Image, ImageEnhance, ImageFilter
import pytesseract
import pyautogui
import time
import keyboard
from mss import mss

# Setze den Pfad für Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Festlegen der Bildschirmkoordinaten
x, y = 890, 588

# Definition von Farbwerten
blue = (39, 121, 188)
white = (255, 255, 255)

# Erstellen eines mss-Objekts
sct = mss()
counter = 0

# Warten auf Tastendruck "esc" zum Starten des Programms
if keyboard.read_key() == "esc":
    # Endlose Schleife für die Bilderkennung und -verarbeitung
    while True:
        # Erstellen eines Screenshots des ausgewählten Bereichs
        screenshot = ImageGrab.grab(bbox=(50, 200, 1800, 650))

        # Verbesserung der Bildqualität durch Kontrasterhöhung
        enhancer = ImageEnhance.Contrast(screenshot)
        enhanced_screenshot = enhancer.enhance(1.5)

        # Anwendung von Bildfiltern
        filtered_screenshot = enhanced_screenshot.filter(ImageFilter.SHARPEN)
        filtered_screenshot = filtered_screenshot.filter(ImageFilter.DETAIL)
        
        # Speichern des gefilterten Screenshots
        filtered_screenshot.save("screenshot.png")

        # Öffnen des gespeicherten Screenshots
        image = Image.open("screenshot.png")

        # Extrahieren von Zahlen aus dem Bild mit Tesseract OCR
        numbers = pytesseract.image_to_string(image, config='digits')

        # Extrahieren der Farbe eines einzelnen Pixels an den angegebenen Koordinaten
        pixel_color = sct.grab({"top": y, "left": x, "width": 1, "height": 1}).pixel(0, 0)

        # Überprüfen, ob die Pixelfarbe weiß ist
        if pixel_color == white:
            # Warten, bis die Pixelfarbe blau ist
            while pixel_color != blue:
                pixel_color = sct.grab({"top": y, "left": x, "width": 1, "height": 1}).pixel(0, 0)
            
            # Warten mit zusätzlichem Zeitfaktor
            time.sleep(0.5 + counter)
            
            # Ausgabe und Eingabe der erkannten Zahlen
            print(numbers)
            keyboard.write(numbers)
            
            # Warten und Klicken an bestimmten Bildschirmkoordinaten
            time.sleep(0.5)
            pyautogui.click(950, 630)
            time.sleep(1)
            pyautogui.click(950, 715)
