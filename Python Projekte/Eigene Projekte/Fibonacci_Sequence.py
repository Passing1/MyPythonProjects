def fibonacci(n):
    # Initialisiere die Fibonacci-Folge mit den ersten drei Gliedern.
    fib_sequence = [0, 1, 1]

    # Überprüfe, ob die Position gültig ist (größer oder gleich 1).
    if n <= 0:
        raise ValueError("Die Position sollte größer oder gleich 1 sein.")

    # Wenn n kleiner oder gleich 3 ist, ist das n-te Glied bereits in der Liste.
    if n <= 3:
        result = fib_sequence[n - 1]
        fib_sequence = fib_sequence[:n]
    else:
        # Berechne die Fibonacci-Folge für n > 3.
        for _ in range(n - 3):
            # Berechne das nächste Glied durch Addition der letzten beiden Glieder.
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            # Füge das nächste Glied zur Liste hinzu.
            fib_sequence.append(next_fib)

        # Das Ergebnis ist das letzte Glied der Liste.
        result = fib_sequence[-1]

    # Gib das Ergebnis und die gesamte Fibonacci-Folge zurück.
    return result, fib_sequence


def main():
    try:
        # Benutzereingabe für die Position des gewünschten Glieds.
        n = int(input('Folgenglied für n: '))
        
        # Berechne das n-te Glied und erhalte die gesamte Fibonacci-Folge.
        result, fib_sequence = fibonacci(n)
        
        # Gib das Ergebnis aus.
        print(f'Das Folgenglied für {n} lautet {result}')

        # Benutzereingabe, ob die Liste der Folgenglieder angezeigt werden soll.
        show_list = input('Liste der Folgenglieder anzeigen? (J/N): ')
        if show_list.lower() == 'j':
            print(f'Liste: {fib_sequence}')

    except ValueError:
        print("Bitte geben Sie eine gültige positive ganze Zahl für n ein.")

if __name__ == "__main__":
    main()
