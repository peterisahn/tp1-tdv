import random
import os

def generar_dataset(n, m, nombre):
    os.makedirs(os.path.dirname(nombre), exist_ok=True)
    with open(nombre, 'w') as f:
        f.write(f"{n} {m}\n")
        for _ in range(n):
            fila = [round(random.uniform(0, 10), 2) for _ in range(m)]
            f.write("  ".join(map(str, fila)) + "\n")

 #Datasets para FB y BT: n chico porque son exponenciales
m_fijo = 10
for n in [5, 8, 10, 12, 15]:
    generar_dataset(n, m_fijo, f"TP1/input/fb_bt_n{n}_m{m_fijo}.txt")

# Datasets para PD: puede manejar n y m mucho más grandes
for n in [10, 50, 100, 500, 1000]:
    generar_dataset(n, 100, f"TP1/input/pd_n{n}_m100.txt")