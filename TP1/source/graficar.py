import pandas as pd
import matplotlib.pyplot as plt

# Leer CSV
df = pd.read_csv("resultados.csv")

orden = ["baja", "media", "alta"]

# ================================
# 📊 GRÁFICO 1: TIEMPOS
# ================================
df_tiempos = (
    df.groupby(["varianza", "algoritmo"])["tiempo_ms"]
    .mean()
    .unstack()
    .reindex(orden)
)

plt.figure()
ax = df_tiempos.plot(kind="bar", color=["#1f77b4", "#d62728"])  # BT azul, FB rojo

ax.set_title("Tiempo de ejecución promedio según la varianza de los datos")
ax.set_xlabel("Nivel de varianza")
ax.set_ylabel("Tiempo de ejecución [ms]")
ax.set_xticklabels(orden, rotation=0)

plt.legend(title="Algoritmo", labels=["Backtracking", "Fuerza Bruta"])
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("grafico_tiempos.png", dpi=300)
plt.show()

# ================================
# 📈 GRÁFICO 2: PODAS (HORIZONTAL)
# ================================
df_podas = (
    df[df["algoritmo"] == "bt"]
    .groupby("varianza")["podas"]
    .mean()
    .reindex(orden)
)

plt.figure()
ax = df_podas.plot(kind="barh", color="#2ca02c")  # verde

ax.set_title("Cantidad promedio de podas según la varianza (Backtracking)")
ax.set_xlabel("Cantidad de podas")
ax.set_ylabel("Nivel de varianza")

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("grafico_podas.png", dpi=300)
plt.show()