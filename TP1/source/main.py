import time
import csv
from pathlib import Path

from Backtracking import encontrar_seam_backtracking
from ProgramacionDinamica import encontrar_seam_pd


def leer_matriz(ruta):
    with open(ruta, "r") as f:
        filas, columnas = map(int, f.readline().split())
        matriz = [list(map(float, f.readline().split())) for _ in range(filas)]
    return matriz


def correr_experimentos():
    varianzas = ["baja", "media", "alta"]
    algoritmos = ["bt", "pd"]   # sin FB
    instancias = 5
    repeticiones = 5

    with open("resultados_python.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algoritmo", "varianza", "instancia", "tiempo_ms"])

        for var in varianzas:
            for i in range(instancias):

                path = f"../input/exp_var/{var}_{i}.txt"
                energia = leer_matriz(path)

                for alg in algoritmos:

                    tiempo_total = 0

                    for _ in range(repeticiones):
                        start = time.perf_counter()

                        if alg == "bt":
                            encontrar_seam_backtracking(energia)
                        else:
                            encontrar_seam_pd(energia)

                        end = time.perf_counter()
                        tiempo_total += (end - start) * 1000

                    promedio = tiempo_total / repeticiones

                    writer.writerow([alg, var, i, promedio])

                    print(f"✔ {alg} {var}_{i} -> {promedio:.4f} ms")

    print("\n📊 CSV generado: resultados_python.csv")


if __name__ == "__main__":
    correr_experimentos()