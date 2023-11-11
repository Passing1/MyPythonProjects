import pyautogui
import time
from screeninfo import get_monitors

# Iteriere über alle Monitore und speichere deren Breite und Höhe
for monitor in get_monitors():
    width = monitor.width
    height = monitor.height

# Setze die Bildschirmbreite und -höhe basierend auf dem Hauptmonitor
screen_width = width
screen_height = height

# Erstelle einen Screenshot und speichere ihn als "screenshot.png"
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Funktion zur Berechnung von Positionen basierend auf top_left und bottom_right
def compute_positions(top_left, bottom_right):
    width = (bottom_right[0] - top_left[0]) // 2
    height = (bottom_right[1] - top_left[1]) // 2

    # Definiere die Positionen der neun Bereiche im Rechteck
    positions_ = [
        (top_left[0], top_left[1]),
        (top_left[0] + width, top_left[1]),
        (bottom_right[0], top_left[1]),
        (top_left[0], top_left[1] + height),
        (top_left[0] + width, top_left[1] + height),
        (bottom_right[0], top_left[1] + height),
        (top_left[0], bottom_right[1]),
        (top_left[0] + width, bottom_right[1]),
        (bottom_right[0], bottom_right[1])
    ]

    # Stelle sicher, dass die Koordinaten innerhalb der Grenzen des Hauptmonitors liegen
    positions_ = [(x, y) for x, y in positions_ if 0 <= x < screen_width and 0 <= y < screen_height]

    return positions_

# Definiere den Bereich für die Flash-Überwachung
top_left_ = (780, 400)
bottom_right_ = (1110, 730)

# Berechne die Positionen innerhalb des angegebenen Bereichs
positions = compute_positions(top_left_, bottom_right_)

# Gib die berechneten Positionen aus
print(positions)

# Initialisiere Listen für geblinkte Bereiche und die Zeit des letzten Flashes
flash_list = []
last_flash_time = None

try:
    # Starte eine Endlosschleife für die Überwachung von Blinkvorgängen
    while True:
        for idx, pos in enumerate(positions):
            # Überprüfe, ob die Farbe an der Position weiß ist (255, 255, 255)
            if pyautogui.pixelMatchesColor(pos[0], pos[1], (255, 255, 255)):
                # Füge den Index zur Blinkliste hinzu, wenn nicht bereits enthalten
                if len(flash_list) == 0 or flash_list[-1] != idx:
                    flash_list.append(idx)
                    last_flash_time = time.time()

        # Überprüfe, ob seit dem letzten Blinken mehr als 1 Sekunde vergangen sind
        if last_flash_time and (time.time() - last_flash_time) >= 1:
            # Klicke auf alle geblinkten Bereiche
            for idx in flash_list:
                pyautogui.click(positions[idx][0], positions[idx][1])

            # Leere die Blinkliste und setze die Zeit des letzten Flashes zurück
            flash_list.clear()
            last_flash_time = None

        # Warte 0,1 Sekunden, um die Schleife zu verlangsamen
        time.sleep(0.1)

# Behandle den KeyboardInterrupt, um das Skript ordnungsgemäß zu beenden
except KeyboardInterrupt:
    print("Script Terminated by user.")
