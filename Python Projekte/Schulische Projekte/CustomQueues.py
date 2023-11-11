# Eine abstrakte Warteschlangenklasse
class AbstractQueue:
    def __init__(self):
        # Liste zur Speicherung der Elemente in der Warteschlange
        self.elements = []

    def add_element(self, element):
        # Methode zum Hinzufügen eines Elements zur Warteschlange
        self.elements.append(element)

    def is_empty(self):
        # Methode zur Überprüfung, ob die Warteschlange leer ist
        return len(self.elements) == 0


# Eine spezielle FIFO-Warteschlangenklasse, die von der abstrakten Klasse erbt
class FifoQueue(AbstractQueue):
    def pop_element(self):
        # Methode zum Entfernen und Zurückgeben des ersten Elements der Warteschlange (FIFO)
        if not self.is_empty():
            return self.elements.pop(0)


# Eine spezielle LIFO-Warteschlangenklasse, die von der abstrakten Klasse erbt
class LifoQueue(AbstractQueue):
    def pop_element(self):
        # Methode zum Entfernen und Zurückgeben des letzten Elements der Warteschlange (LIFO)
        if not self.is_empty():
            return self.elements.pop()


# Testen der Queue-Klassen
fifo_queue = FifoQueue()
lifo_queue = LifoQueue()

# Elemente zur FIFO-Queue hinzufügen
for i in range(1, 10):
    fifo_queue.add_element(i)

# Elemente zur LIFO-Queue hinzufügen
for i in range(1, 10):
    lifo_queue.add_element(i)

# Elemente aus der FIFO-Queue abrufen und ausgeben
for i in range(1, 10):
    print(f"FIFO Queue: {fifo_queue.pop_element()}")

print()

# Elemente aus der LIFO-Queue abrufen und ausgeben
for i in range(1, 10):
    print(f"LIFO Queue: {lifo_queue.pop_element()}")
