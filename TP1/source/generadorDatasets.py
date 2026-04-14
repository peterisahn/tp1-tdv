import os
import random
import numpy as np

# ─────────────────────────────────────────────────────────────
# 📁 Guardado
# ─────────────────────────────────────────────────────────────

def guardar(nombre, n, m, matriz):
    os.makedirs(os.path.dirname(nombre), exist_ok=True)
    with open(nombre, 'w') as f:
        f.write(f"{n} {m}\n")
        for fila in matriz:
            f.write(" ".join(map(str, fila)) + "\n")

# ─────────────────────────────────────────────────────────────
# 🎯 GENERADORES BASE
# ─────────────────────────────────────────────────────────────

def gen_random(n, m):
    return [[round(random.uniform(0.1, 10), 2) for _ in range(m)] for _ in range(n)]

def gen_uniforme(n, m, valor):
    return [[valor] * m for _ in range(n)]

# ─────────────────────────────────────────────────────────────
# 🔬 EXPERIMENTOS POR VARIANZA (CLAVE)
# ─────────────────────────────────────────────────────────────

def gen_varianza_baja(n, m):
    return [[round(random.uniform(1.0, 1.1), 2) for _ in range(m)] for _ in range(n)]

def gen_varianza_media(n, m):
    return [[round(random.uniform(1.0, 5.0), 2) for _ in range(m)] for _ in range(n)]

def gen_varianza_alta(n, m):
    return [[round(random.uniform(0.1, 10.0), 2) for _ in range(m)] for _ in range(n)]

# ⭐ versión PRO (control real de varianza)
def gen_con_varianza_controlada(n, m, media=5, varianza=1):
    matriz = np.random.normal(loc=media, scale=varianza**0.5, size=(n, m))
    matriz = np.clip(matriz, 0.1, 10)
    return [[round(float(x), 2) for x in fila] for fila in matriz]

# ─────────────────────────────────────────────────────────────
# ⚠️ CASOS EXTREMOS / ESTRUCTURADOS
# ─────────────────────────────────────────────────────────────

def gen_columna_barata(n, m, col_barata, energia_baja=0.1, energia_alta=9.9):
    matriz = []
    for _ in range(n):
        fila = [energia_alta] * m
        fila[col_barata] = energia_baja
        matriz.append(fila)
    return matriz

def gen_diagonal(n, m):
    matriz = [[9.9] * m for _ in range(n)]
    col = 0
    for f in range(n):
        matriz[f][col] = 0.1
        if col < m - 1:
            col += 1
    return matriz

def gen_zigzag(n, m):
    matriz = [[9.9] * m for _ in range(n)]
    for f in range(n):
        col = f % 2
        matriz[f][col] = 0.1
    return matriz

def gen_gradiente(n, m):
    matriz = []
    for _ in range(n):
        fila = [round(i * (10.0 / (m - 1)), 2) for i in range(m)]
        matriz.append(fila)
    return matriz

def gen_checkerboard(n, m):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(m):
            fila.append(0.1 if (f + c) % 2 == 0 else 9.9)
        matriz.append(fila)
    return matriz

# ─────────────────────────────────────────────────────────────
# 🚀 GENERACIÓN DE DATASETS
# ─────────────────────────────────────────────────────────────

N = 15
M = 15
REPS = 10  # cantidad de instancias por caso

# ── 1. EXPERIMENTOS PRINCIPALES (VARIANZA) ────────────────────

for i in range(REPS):
    guardar(f"TP1/input/exp_var/baja_{i}.txt",  N, M, gen_varianza_baja(N, M))
    guardar(f"TP1/input/exp_var/media_{i}.txt", N, M, gen_varianza_media(N, M))
    guardar(f"TP1/input/exp_var/alta_{i}.txt",  N, M, gen_varianza_alta(N, M))

# ⭐ opcional PRO
guardar("TP1/input/exp_var_controlada/baja.txt",  N, M, gen_con_varianza_controlada(N, M, varianza=0.01))
guardar("TP1/input/exp_var_controlada/media.txt", N, M, gen_con_varianza_controlada(N, M, varianza=2))
guardar("TP1/input/exp_var_controlada/alta.txt",  N, M, gen_con_varianza_controlada(N, M, varianza=10))

# ── 2. CASOS EXTREMOS (ANÁLISIS ADICIONAL) ────────────────────

guardar("TP1/input/extremos/col_barata_primera.txt", N, M, gen_columna_barata(N, M, 0))
guardar("TP1/input/extremos/col_barata_ultima.txt",  N, M, gen_columna_barata(N, M, M-1))
guardar("TP1/input/extremos/col_barata_centro.txt",  N, M, gen_columna_barata(N, M, M//2))

guardar("TP1/input/extremos/diagonal.txt",    N, M, gen_diagonal(N, M))
guardar("TP1/input/extremos/zigzag.txt",      N, M, gen_zigzag(N, M))
guardar("TP1/input/extremos/gradiente.txt",   N, M, gen_gradiente(N, M))
guardar("TP1/input/extremos/checkerboard.txt",N, M, gen_checkerboard(N, M))

# ── 3. CASOS BORDE ────────────────────────────────────────────

guardar("TP1/input/bordes/n1_m1.txt", 1, 1, gen_random(1, 1))
guardar("TP1/input/bordes/n1_m10.txt", 1, 10, gen_random(1, 10))
guardar("TP1/input/bordes/n10_m1.txt", 10, 1, gen_random(10, 1))

# ── 4. CASOS GRANDES (SOLO PD / BT) ───────────────────────────

guardar("TP1/input/grandes/random_100.txt", 100, 100, gen_random(100, 100))
guardar("TP1/input/grandes/col_barata_100.txt", 100, 100, gen_columna_barata(100, 100, 0))