import pyautogui
from mss import mss

# Koordinaten des Pixels
x, y = 280, 420

# RGB-Farbe für Rot und Grün
red = (206, 38, 54)
green = (75, 219, 106)

# Erstelle ein mss Objekt
sct = mss()

while True:
    # Farbe des Pixels an den Koordinaten (x, y) abrufen
    pixel_color = sct.grab({"top": y, "left": x, "width": 1, "height": 1}).pixel(0, 0)

    # Wenn die Farbe rot ist
    if pixel_color == red:
        # Warte auf den Wechsel zu Grün
        while pixel_color != green:
            pixel_color = sct.grab({"top": y, "left": x, "width": 1, "height": 1}).pixel(0, 0)
        
        # Sobald es zu Grün wechselt, klicke auf den Bildschirm bei (x, y)
        pyautogui.click(x, y)
