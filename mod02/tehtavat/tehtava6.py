import random

# Kolmenumeroinen koodi, numerot 0–9
koodi1 = random.randint(0, 999)

# Nelinumeroinen koodi, jokainen numero 1–6
koodi2 = ""

for i in range(4):
    koodi2 += str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi: {koodi1:03d}")
print(f"Nelinumeroinen koodi: {koodi2}")