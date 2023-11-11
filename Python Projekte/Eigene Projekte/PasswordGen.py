import random
import string

# Funktion zur Generierung eines Passworts
def generate_password():
    # Benutzereingabe für die Passwortlänge
    lang = int(input('Passwortlänge: '))
    
    # Benutzereingabe für die Auswahl der Zeichenkategorien
    alph_ak = input('Kleine Buchstaben (J/N): ').lower()
    alph_ag = input('Große Buchstaben (J/N): ').lower()
    numm_a = input('Zahlen (J/N): ').lower()
    sonder_a = input('Sonderzeichen (J/N): ').lower()

    # Listen für verschiedene Zeichenkategorien
    alph_k = list(string.ascii_lowercase)
    alph_g = list(string.ascii_uppercase)
    numm = list(string.digits)
    sonder = list(string.punctuation)

    # Liste für die ausgewählten Zeichen
    aus = []
    # Überprüfen, welche Zeichenkategorien ausgewählt wurden
    if alph_ak == 'j':
        aus += alph_k
    if alph_ag == 'j':
        aus += alph_g
    if numm_a == 'j':
        aus += numm
    if sonder_a == 'j':
        aus += sonder

    # Überprüfen, ob mindestens eine Zeichenkategorie ausgewählt wurde
    if not aus:
        print('Es wurden keine Zeichen ausgewählt. Bitte mindestens eine Kategorie auswählen.')
        return

    # Generierung des Passworts
    pass_final = ''.join(random.choice(aus) for _ in range(lang))
    print(f'Das Passwort lautet: {pass_final}')

# Hauptprogramm
if __name__ == "__main__":
    while True:
        # Passwort generieren
        generate_password()
        # Benutzereingabe für die Fortsetzung
        loop = input('Weiteres Passwort erstellen? (J/N): ').lower()
        if loop != 'j':
            break
