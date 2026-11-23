# Exercise 32 - Python Data Structures

from collections import deque
fila = deque()
for numero in range(1, 6):
    fila.append(f"A{numero:03d}")
while fila:
    print("Chamando:", fila.popleft())
