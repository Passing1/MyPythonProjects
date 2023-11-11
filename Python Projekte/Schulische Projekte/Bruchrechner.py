# Funktion, die einen Bruch auf der Konsole ausgibt
def printFract(frac):
    print(f"\nDas Ergebnis lautet: {frac[0]}/{frac[1]}")

# Funktion zur Eingabe eines Bruchs von der Konsole
def inputFract():
    while True:
        try:
            a = int(input("Gib den Zähler ein: "))
            b = int(input("Gib den Nenner ein: "))
            break
        except ValueError:
            print("Du hast keine Zahl eingegeben. Bitte versuche es erneut.")
    return [a, b]

# Definition einer Bruchklasse (Fraction)
class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    # Funktion, die eine lesbare Zeichenkette des Bruchs zurückgibt
    def __str__(self):
        return f"{self.num}/{self.den}"

    # Funktion für die Berechnung des größten gemeinsamen Teilers (ggT) der beiden Zahlen im Bruch
    def getGcd(self):
        a, b = self.num, self.den
        while b:
            a, b = b, a % b
        return a

    # Funktion zur Kürzung des Bruchs
    def cancelFract(self):
        gcd = self.getGcd()
        a = self.num // gcd
        b = self.den // gcd
        return a, b

    # Funktion zur Negierung des Bruchs
    def negFract(self):
        return -self.num, self.den

    # Funktion zur Berechnung des Kehrwerts des Bruchs
    def invFract(self):
        return self.den, self.num

    # Funktion zur Multiplikation oder Division von Brüchen
    def MulDivFract(self, other, vz):
        if vz == ":":
            Z = self.num * other.den
            N = self.den * other.num
        elif vz == "*":
            Z = self.num * other.num
            N = self.den * other.den
        return Z, N

    # Funktion zur Addition oder Subtraktion von Brüchen
    def AddSubFract(self, other, vz):
        if self.den != other.den:
            # Gemeinsamen Nenner für die Addition oder Subtraktion berechnen
            gfract1 = [self.num * other.den, self.den * other.den]
            gfract2 = [other.num * self.den, other.den * self.den]
            subZ = gfract1[0] + gfract2[0] if vz == "+" else gfract1[0] - gfract2[0]
            subN = gfract1[1]
        else:
            # Wenn die Nenner gleich sind, direkt addieren oder subtrahieren
            subZ = self.num + other.num if vz == "+" else self.num - other.num
            subN = self.den
        return subZ, subN

# Hauptfunktion des Programms
def main():
    # Menüoptionen für den Benutzer anzeigen
    print("1. Den ggT eines Bruches erfahren.")
    print("2. Einen Bruch kürzen.")
    print("3. Einen Bruch negieren.")
    print("4. Den Kehrwert eines Bruchs bilden.")
    print("5. Zwei Brüche addieren.")
    print("6. Zwei Brüche subtrahieren.")
    print("7. Zwei Brüche multiplizieren.")
    print("8. Zwei Brüche dividieren.")

    action = 0
    again = False

    while action <= 0 or action > 8 or again:
        print()
        # Benutzer nach der gewünschten Aktion fragen
        action = int(input("Was möchtest du machen? "))
        # Benutzer nach dem ersten Bruch fragen
        inpuut = inputFract()
        f = Fraction(inpuut[0], inpuut[1])
        print()

        # Je nach Benutzeraktion die entsprechende Funktion aufrufen und das Ergebnis ausgeben
        if action == 1:
            print(f"Der ggT ist: {f.getGcd()}")
        elif action == 2:
            printFract(f.cancelFract())
        elif action == 3:
            printFract(f.negFract())
        elif action == 4:
            printFract(f.invFract())
        elif action in [5, 6, 7, 8]:
            # Benutzer nach dem zweiten Bruch fragen
            inpuuut = inputFract()
            f_1 = Fraction(inpuut[0], inpuut[1])
            f_2 = Fraction(inpuuut[0], inpuuut[1])

            # Je nach Benutzeraktion die entsprechende Berechnung durchführen
            if action == 5:
                result = f_1.AddSubFract(f_2, "+")
            elif action == 6:
                result = f_1.AddSubFract(f_2, "-")
            elif action == 7:
                result = f_1.MulDivFract(f_2, "*")
            elif action == 8:
                if f_2.num == 0:
                    print("Division durch Null ist nicht erlaubt.")
                    return
                result = f_1.MulDivFract(f_2, ":")

            # Nach der Rechenoperation nach Kürzung fragen
            reduce_choice = input("Möchtest du das Ergebnis auf den kleinstmöglichen gekürzten Bruch reduzieren? [j/n] ").lower()

            # Ergebnis reduzieren, wenn gewünscht
            if reduce_choice == "j":
                result = Fraction(result[0], result[1]).cancelFract()

            printFract(result)

        print()
        # Benutzer nach weiteren Aktionen fragen
        aa = input("Willst du noch etwas wissen? [j/n] ")
        again = aa.lower() == "j"

# Die Hauptfunktion ausführen, um das Programm zu starten
main()
