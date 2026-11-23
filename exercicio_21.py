# Exercise 21 - Python Data Structures

historico = []
texto = "Olá"
historico.append(texto)
texto += " mundo"
print("Editado:", texto)
if historico:
    texto = historico.pop()
print("Desfeito:", texto)
