import random

# Lista para almacenar los números aleatorios
random_integers = []

# Número de números aleatorios a generar
num_numbers = 500

# Rango de los números aleatorios
min_value = 0
max_value = 100

# Ciclo para generar y almacenar los números aleatorios
for _ in range(num_numbers):
    random_number = random.randint(min_value, max_value)
    random_integers.append(random_number)

# Imprimir los primeros 10 números aleatorios generados para verificar
print(random_integers)
