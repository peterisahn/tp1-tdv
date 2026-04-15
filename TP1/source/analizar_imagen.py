import time
import numpy as np
from PIL import Image
import subprocess

def imagen_a_txt(ruta_imagen, ruta_salida, max_size=12):
    """Convierte imagen a matriz de energía en formato .txt"""
    img = Image.open(ruta_imagen).convert("RGB")
    
    # Redimensionar para que FB y BT sean viables
    img = img.resize((max_size, max_size))
    img_array = np.array(img).astype(float)
    
    n, m = img_array.shape[:2]
    energia = np.zeros((n, m))
    
    for canal in range(3):
        dx = np.roll(img_array[:,:,canal], -1, axis=1) - np.roll(img_array[:,:,canal], 1, axis=1)
        dy = np.roll(img_array[:,:,canal], -1, axis=0) - np.roll(img_array[:,:,canal], 1, axis=0)
        energia += dx**2 + dy**2
    energia = np.sqrt(energia)
    
    # Calcular y mostrar varianza
    print(f"Imagen: {ruta_imagen}")
    print(f"Varianza de energía: {np.var(energia):.2f}")
    print(f"Desvío estándar:     {np.std(energia):.2f}")
    print(f"Media:               {np.mean(energia):.2f}")
    print(f"Min:                 {np.min(energia):.2f}")
    print(f"Max:                 {np.max(energia):.2f}")
    
    # Guardar como .txt
    with open(ruta_salida, 'w') as f:
        f.write(f"{n} {m}\n")
        for fila in energia:
            f.write("  ".join(f"{v:.2f}" for v in fila) + "\n")
    
    return energia

def medir_tiempo(algoritmo, ruta_txt):
    """Mide el tiempo de ejecución del ejecutable C++"""
    inicio = time.time()
    subprocess.run(
        ["./source/seam", "--numerico", ruta_txt, "--algoritmo", algoritmo],
        capture_output=True
    )
    fin = time.time()
    return (fin - inicio) * 1000  # ms

# ── USO ──────────────────────────────────────────────────────
ruta_imagen = "img/varianzaalta.jpg"       # cambiá por tu imagen
ruta_txt    = "input/img_energia.txt"

energia = imagen_a_txt(ruta_imagen, ruta_txt, max_size=12)

print("\nTiempos de ejecución:")
for alg in ["fb", "bt", "pd"]:
    t = medir_tiempo(alg, ruta_txt)
    print(f"  {alg}: {t:.2f} ms")

