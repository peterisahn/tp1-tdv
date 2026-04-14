#import random
#import os
#
#def generar_dataset(n, m, nombre):
#    os.makedirs(os.path.dirname(nombre), exist_ok=True)
#    with open(nombre, 'w') as f:
#        f.write(f"{n} {m}\n")
#        for _ in range(n):
#            fila = [round(random.uniform(0, 10), 2) for _ in range(m)]
#            f.write("  ".join(map(str, fila)) + "\n")
#
 #Datasets para FB y BT: n chico porque son exponenciales
#m_fijo = 10
#for n in [5, 8, 10, 12, 15]:
#    generar_dataset(n, m_fijo, f"TP1/input/fb_bt_n{n}_m{m_fijo}.txt")

# Datasets para PD: puede manejar n y m mucho más grandes
#for n in [10, 50, 100, 500, 1000]:
#    generar_dataset(n, 100, f"TP1/input/pd_n{n}_m100.txt")
#
import random
import os

def guardar(nombre, n, m, matriz):
    os.makedirs(os.path.dirname(nombre), exist_ok=True)
    with open(nombre, 'w') as f:
        f.write(f"{n} {m}\n")
        for fila in matriz:
            f.write("  ".join(map(str, fila)) + "\n")

def gen_random(n, m):
    return [[round(random.uniform(0, 10), 2) for _ in range(m)] for _ in range(n)]

def gen_uniforme(n, m, valor):
    return [[valor] * m for _ in range(n)]

def gen_columna_barata(n, m, col_barata, energia_baja=0.1, energia_alta=9.9):
    matriz = []
    for _ in range(n):
        fila = [energia_alta] * m
        fila[col_barata] = energia_baja
        matriz.append(fila)
    return matriz

def gen_diagonal(n, m):
    # el seam optimo baja en diagonal desde (0,0) hasta (n-1, min(n-1, m-1))
    matriz = [[9.9] * m for _ in range(n)]
    col = 0
    for f in range(n):
        matriz[f][col] = 0.1
        if col < m - 1:
            col += 1
    return matriz

def gen_zigzag(n, m):
    # el seam optimo zigzaguea entre columna 0 y columna 1
    matriz = [[9.9] * m for _ in range(n)]
    for f in range(n):
        col = f % 2
        matriz[f][col] = 0.1
    return matriz

def gen_gradiente(n, m):
    # energia crece de izquierda a derecha: columna 0 siempre es la mas barata
    matriz = []
    for _ in range(n):
        fila = [round(i * (10.0 / (m - 1)), 2) for i in range(m)]
        matriz.append(fila)
    return matriz

def gen_checkerboard(n, m):
    # patron ajedrez: celdas alternadas entre 0.1 y 9.9
    matriz = []
    for f in range(n):
        fila = []
        for c in range(m):
            fila.append(0.1 if (f + c) % 2 == 0 else 9.9)
        matriz.append(fila)
    return matriz


# ── Columna barata primera y última ──────────────────────────────────────────
guardar("TP1/input/col_barata_primera.txt",  15, 10, gen_columna_barata(15, 10, col_barata=0))
guardar("TP1/input/col_barata_ultima.txt",   15, 10, gen_columna_barata(15, 10, col_barata=9))

# ── Casos borde / límite ──────────────────────────────────────────────────────
guardar("TP1/input/borde_n1_m1.txt",         1,   1,   gen_random(1, 1))
guardar("TP1/input/borde_n1_m10.txt",        1,   10,  gen_random(1, 10))   # una sola fila: cualquier columna es un seam valido
guardar("TP1/input/borde_n10_m1.txt",        10,  1,   gen_random(10, 1))   # una sola columna: unico seam posible
guardar("TP1/input/borde_n2_m2.txt",         2,   2,   gen_random(2, 2))    # minimo no trivial

# ── Casos uniformes ───────────────────────────────────────────────────────────
guardar("TP1/input/uniforme_cero.txt",       10,  10,  gen_uniforme(10, 10, 0.0))   # todos cero: cualquier seam es optimo
guardar("TP1/input/uniforme_alto.txt",       10,  10,  gen_uniforme(10, 10, 9.9))   # todos iguales y altos

# ── Casos con seam optimo conocido ───────────────────────────────────────────
guardar("TP1/input/col_barata_centro.txt",   15,  11,  gen_columna_barata(15, 11, col_barata=5))   # optimo: columna del medio
guardar("TP1/input/diagonal.txt",            10,  10,  gen_diagonal(10, 10))                        # optimo baja en diagonal
guardar("TP1/input/zigzag.txt",              10,  10,  gen_zigzag(10, 10))                          # optimo zigzaguea

# ── Casos de gradiente ────────────────────────────────────────────────────────
guardar("TP1/input/gradiente_izq_der.txt",   10,  10,  gen_gradiente(10, 10))                       # optimo siempre columna 0
guardar("TP1/input/gradiente_der_izq.txt",   10,  10,  [list(reversed(f)) for f in gen_gradiente(10, 10)])  # optimo siempre columna m-1

# ── Patron ajedrez ────────────────────────────────────────────────────────────
guardar("TP1/input/checkerboard.txt",        10,  10,  gen_checkerboard(10, 10))

# ── Casos grandes solo para PD ───────────────────────────────────────────────
guardar("TP1/input/pd_grande_n1000_m1000.txt",  1000, 1000, gen_random(1000, 1000))
guardar("TP1/input/pd_col_barata_grande.txt",   1000, 1000, gen_columna_barata(1000, 1000, col_barata=0))