import pandas as pd
import matplotlib.pyplot as plt

algoritmo_objetivo = "bt"   # o "pd"
orden = ["baja", "media", "alta"]

cpp = pd.read_csv("resultados.csv")
py = pd.read_csv("resultados_python.csv")

cpp["lenguaje"] = "C++"
py["lenguaje"] = "Python"

cpp = cpp[["algoritmo", "varianza", "instancia", "tiempo_ms", "lenguaje"]]
py = py[["algoritmo", "varianza", "instancia", "tiempo_ms", "lenguaje"]]

df = pd.concat([cpp, py], ignore_index=True)
df = df[df["algoritmo"] == algoritmo_objetivo]

df_plot = (
    df.groupby(["varianza", "lenguaje"])["tiempo_ms"]
    .mean()
    .unstack()
    .reindex(orden)
)

ax = df_plot.plot(kind="bar")

nombre_alg = "Backtracking" if algoritmo_objetivo == "bt" else "Programación Dinámica"

ax.set_title(f"Comparación de tiempo de ejecución: {nombre_alg} en C++ y Python")
ax.set_xlabel("Nivel de varianza")
ax.set_ylabel("Tiempo de ejecución [ms]")
ax.set_xticklabels(orden, rotation=0)
ax.set_yscale("log")

plt.legend(title="Lenguaje")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(f"grafico_{algoritmo_objetivo}_lenguajes.png", dpi=300)
plt.show()