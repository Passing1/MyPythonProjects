# Basisklasse für alle grafischen Elemente
class Graphic:
    # Gibt den Präfix-Tag für SVG zurück
    def getSVGPrefix(self):
        return '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'

    # Gibt den Suffix-Tag für SVG zurück
    def getSVGSuffix(self):
        return '</svg>'

    # Gibt den Inhalt des SVG zurück (standardmäßig leer)
    def getSVGContent(self):
        return ''

    # Gibt das vollständige SVG zurück, bestehend aus Präfix, Inhalt und Suffix
    def getSVG(self):
        return self.getSVGPrefix() + self.getSVGContent() + self.getSVGSuffix()

    # Gibt den Stil des SVG zurück (standardmäßig schwarz gestrichelt, 2px breit, weiß gefüllt)
    def getStyle(self):
        return 'stroke="black" stroke-width="2" fill="%s"' % self.color
    
    def setStyle(self, fill_color="white"):
        self.color = fill_color
    

# Klasse für eine Gruppe von grafischen Elementen, erbt von Graphic
class GraphicGroup(Graphic):
    # Konstruktor initialisiert die Liste der Elemente
    def __init__(self):
        self._elements = []

    # Gibt den SVG-Inhalt für alle Elemente in der Gruppe zurück
    def getSVGContent(self):
        ret = ""
        for element in self._elements:
            ret += element.getSVGContent()
        return ret

    # Fügt ein Element zur Gruppe hinzu
    def addElement(self, element: Graphic):
        self._elements.append(element)

    # Gibt alle Elemente in der Gruppe zurück
    def getElements(self):
        return self._elements

    # Entfernt ein Element aus der Gruppe
    def removeElement(self, element):
        self._elements[:] = [x for x in self._elements if not element == x]

    # Ändert die Farbe aller Elemente in der Gruppe
    def globalColor(self, fill_color="white"):
        for i in self._elements:
            i.setColor(fill_color)


# Klasse für ein Kreiselement, erbt von Graphic
class Circle(Graphic):
    # Konstruktor setzt das Zentrum und den Radius des Kreises
    def __init__(self, center, radius, color="white"):
        self.setCenter(center)
        self.setRadius(radius)
        self.color = color

    # Setzt das Zentrum des Kreises
    def setCenter(self, center):
        self._center = center

    # Setzt den Radius des Kreises
    def setRadius(self, radius):
        self._radius = radius

    # Gibt den Radius des Kreises zurück
    def getRadius(self):
        return self._radius

    # Gibt das Zentrum des Kreises zurück
    def getCenter(self):
        return self._center

    # Gibt den SVG-Inhalt für den Kreis zurück
    def getSVGContent(self):
        return '<circle cx="%d" cy="%d" r="%d" %s />' \
               % (self.getCenter()[0], self.getCenter()[1],
                  self.getRadius(), self.getStyle())


# Klasse für ein Rechteckelement, erbt von Graphic
class Rectangle(Graphic):
    # Konstruktor setzt die Punkte und die Rotation des Rechtecks
    def __init__(self, p1, p2, rotation=0, color="white"):
        self.setPoints(p1, p2)
        self.setRotation(rotation)
        self.color = color

    # Setzt die Punkte des Rechtecks
    def setPoints(self, p1, p2):
        self._p1 = p1
        self._p2 = p2

    # Setzt die Rotation des Rechtecks
    def setRotation(self, rotation):
        self._rotation = rotation

    # Gibt die Punkte des Rechtecks zurück
    def getPoints(self):
        return (self._p1, self._p2)

    # Gibt die Rotation des Rechtecks zurück
    def getRotation(self):
        return self._rotation

    # Gibt den SVG-Inhalt für das Rechteck zurück
    def getSVGContent(self):
         center = self.getCenter()
         return '<rect x="%d" y="%d" width="%d" height="%d" transform="rotate(%d,%d,%d)" %s />' \
                % (self.getPoints()[0][0], self.getPoints()[0][1],
                   self.getPoints()[1][0] - self.getPoints()[0][0],
                   self.getPoints()[1][1] - self.getPoints()[0][1],
                   self.getRotation(), center[0], center[1], self.getStyle())

    # Gibt das Zentrum des Rechtecks zurück
    def getCenter(self):
         return ((self._p1[0] + self._p2[0]) / 2, (self._p1[1] + self._p2[1]) / 2)


# Klasse für ein Linien-Element, erbt von Graphic
class Line(Graphic):
    # Konstruktor setzt die Punkte der Linie
    def __init__(self, p1, p2, color="white"):
        self._p1 = p1
        self._p2 = p2
        self.color = color

    # Gibt den SVG-Inhalt für die Linie zurück
    def getSVGContent(self):
        return '<line x1="%d" y1="%d" x2="%d" y2="%d" %s />' \
               % (self._p1[0], self._p1[1], self._p2[0], self._p2[1], self.getStyle())


# Klasse für ein Dreieck-Element, erbt von Graphic
class Triangle(Graphic):
    # Konstruktor setzt die Punkte des Dreiecks
    def __init__(self, p1, p2, p3, color="white"):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self.color = color

    # Gibt den SVG-Inhalt für das Dreieck zurück
    def getSVGContent(self):
        return '<polygon points="%d,%d %d,%d %d,%d" %s />' \
               % (self._p1[0], self._p1[1], self._p2[0], self._p2[1], self._p3[0], self._p3[1], self.getStyle())


# Hauptteil des Programms
if __name__ == "__main__":
    # Erstellt verschiedene grafische Elemente (Kopf, Körpe und Arme (Augen, Nase und Beine))
    head = Circle((70, 30), 20)
    body = Rectangle((40, 50), (100, 110))
    body.setRotation(45)
    arms = (Rectangle((10, 60), (60, 65), 10),
            Rectangle((80, 60), (130, 65), 20))
    nose = Triangle((70, 30), (68, 35), (72, 35))
    eyes = (Line((55, 25), (60, 25)),
            Line((80, 25), (85, 25)))
    legs = (Triangle( ( 50, 80 ), ( 50, 150 ), ( 40, 150 ) ), 
            Triangle( ( 90, 80 ), ( 90, 150 ), ( 100, 150 ) ))

    # Farbeinstellungen
    def change_color(part, elements):
        i = 0
        pre = (part[0].upper(), part[1:])
        word = "".join(pre)

        if part in ["arme", "beine", "augen"]:
            bd = input(f"{word} einzeln färben? [J/N]: ").upper()
        else:
            bd = "N"

        if bd == "J":
            for element in elements:
                i += 1
                color = input(f"Wähle die Farbe für {word[:-1]} {i} (Antwort bitte in Englisch): ").lower()
                elements[i-1].color = color
        elif bd == "N":
            color = input(f"Wähle die Farbe für {word} (Antwort bitte in Englisch): ").lower()
            if part in ["arme", "beine", "augen", "alle"]:
                for element in elements:
                    element.color = color
            else:
                elements[0].color = color

    # Dictionary für Körperteile und ihre zugehörigen Grafikelemente
    body_parts = {
        "alle": [head, body, nose, arms[0], arms[1], legs[0], legs[1], eyes[0], eyes[1]],
        "kopf": [head],
        "körper": [body],
        "nase": [nose],
        "arme": [arms[0], arms[1]],
        "beine": [legs[0], legs[1]],
        "augen": [eyes[0], eyes[1]]
    }

    jn = "J"
    while jn == "J":
        print()
        jn = input("Möchtest du die Farbe von etwas ändern? [J/N]: ").upper()
        if jn == "J":
            print()
            print("Kopf, Körper, Arme, Nase, Augen, Beine")
            kt = input("Welche der Obenstehenden Körperteile möchtest du färben oder möchtest du eine Farbe für alle Wählen? [Körperteil/Alle]: ").lower()

            if kt in body_parts:
                change_color(kt, body_parts[kt])
            else:
                print("Ungültige Eingabe. Bitte versuche es erneut.")

        elif jn == "N":
            print()
            print("OK, dann nicht....")
            break

    # Fügt die Elemente zu einer GraphicGroup hinzu
    gfx = GraphicGroup()
    gfx.addElement(legs[0])
    gfx.addElement(legs[1])
    gfx.addElement(arms[0])
    gfx.addElement(arms[1])
    gfx.addElement(body)
    gfx.addElement(head)
    gfx.addElement(nose)
    gfx.addElement(eyes[0])
    gfx.addElement(eyes[1])

    # Schreibt das SVG der GraphicGroup in die Datei "output.svg"
    svgout = open("output.svg", "w")
    svgout.write(gfx.getSVG())
    svgout.close()
