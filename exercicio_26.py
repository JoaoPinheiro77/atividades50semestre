# Exercise 26 - Python Data Structures

from collections import deque
fila = deque(["Ana", "Beto", "Caio"])
if fila:
    print("Atendido:", fila.popleft())
print("Restantes:", list(fila))
