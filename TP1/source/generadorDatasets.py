import os
import random


def guardar(nombre, n, m, matriz):
    os.makedirs(os.path.dirname(nombre), exist_ok=True)
    with open(nombre, 'w') as f:
        f.write(f"{n} {m}\n")
        for fila in matriz:
            f.write(" ".join(map(str, fila)) + "\n")

# Generadores Base
def gen_random(n, m):
    return [[round(random.uniform(0.1, 10), 2) for _ in range(m)] for _ in range(n)]

def gen_uniforme(n, m, valor):
    return [[valor] * m for _ in range(n)]


# Experimentos por Varianza
def gen_varianza_baja(n, m):
    return [[round(random.uniform(1.0, 1.1), 2) for _ in range(m)] for _ in range(n)]

def gen_varianza_media(n, m):
    return [[round(random.uniform(1.0, 5.0), 2) for _ in range(m)] for _ in range(n)]

def gen_varianza_alta(n, m):
    return [[round(random.uniform(0.1, 10.0), 2) for _ in range(m)] for _ in range(n)]

# Generación de datasets
N = 12
M = 12
REPS = 5  # cantidad de instancias por caso

# Experimentos Principales (Varianza)
for i in range(REPS):
    guardar(f"TP1/input/exp_var/baja_{i}.txt",  N, M, gen_varianza_baja(N, M))
    guardar(f"TP1/input/exp_var/media_{i}.txt", N, M, gen_varianza_media(N, M))
    guardar(f"TP1/input/exp_var/alta_{i}.txt",  N, M, gen_varianza_alta(N, M))
