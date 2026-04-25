import time
import numpy as np
from PIL import Image
import subprocess

def imagen_a_txt(ruta_imagen, ruta_salida, max_size=12):
    """
    Convierte una imagen en una matriz de energía (tipo seam carving)
    y la guarda en un archivo .txt.
    
    Además imprime estadísticas de la matriz (varianza, media, etc.)
    """
    
    # Abrir la imagen y convertirla a RGB
    img = Image.open(ruta_imagen).convert("RGB")
    
    # Redimensionar a max_size x max_size (ej: 12x12 para simplificar el análisis)
    img = img.resize((max_size, max_size))
    
    # Convertir la imagen a un array de numpy (valores float)
    img_array = np.array(img).astype(float)
    
    # Obtener dimensiones
    n, m = img_array.shape[:2]
    
    # Inicializar matriz de energía
    energia = np.zeros((n, m))
    
    # Calcular energía sumando gradientes en X e Y para cada canal (R, G, B)
    for canal in range(3):
        # Derivada aproximada en X (izquierda - derecha)
        dx = np.roll(img_array[:,:,canal], -1, axis=1) - np.roll(img_array[:,:,canal], 1, axis=1)
        
        # Derivada aproximada en Y (arriba - abajo)
        dy = np.roll(img_array[:,:,canal], -1, axis=0) - np.roll(img_array[:,:,canal], 1, axis=0)
        
        # Acumular energía (gradiente al cuadrado)
        energia += dx**2 + dy**2
    
    # Raíz cuadrada final (norma del gradiente)
    energia = np.sqrt(energia)
    
    # Mostrar estadísticas útiles para análisis experimental
    print(f"Imagen: {ruta_imagen}")
    print(f"Varianza de energía: {np.var(energia):.2f}")
    print(f"Desvío estándar:     {np.std(energia):.2f}")
    print(f"Media:               {np.mean(energia):.2f}")
    print(f"Min:                 {np.min(energia):.2f}")
    print(f"Max:                 {np.max(energia):.2f}")
    
    # Guardar la matriz en archivo .txt (formato esperado por el ejecutable)
    with open(ruta_salida, 'w') as f:
        f.write(f"{n} {m}\n")  # dimensiones
        for fila in energia:
            f.write("  ".join(f"{v:.2f}" for v in fila) + "\n")
    
    return energia


def medir_tiempo(algoritmo, ruta_txt):
    """
    Ejecuta el programa en C++ con el algoritmo indicado
    y mide el tiempo de ejecución en milisegundos.
    """
    
    inicio = time.time()
    
    # Ejecutar el binario pasando parámetros por línea de comando
    subprocess.run(
        ["./source/seam", "--numerico", ruta_txt, "--algoritmo", algoritmo],
        capture_output=True  # no imprime salida en consola
    )
    
    fin = time.time()
    
    # Retornar tiempo en milisegundos
    return (fin - inicio) * 1000  


# Paths de entrada/salida
ruta_imagen = "img/foto.jpg"
ruta_txt    = "input/img_energia.txt"

# Generar matriz de energía desde la imagen
energia = imagen_a_txt(ruta_imagen, ruta_txt, max_size=12)

# Medir tiempos de los 3 algoritmos
print("\nTiempos de ejecución:")
for alg in ["fb", "bt", "pd"]:  # fuerza bruta, backtracking, programación dinámica
    t = medir_tiempo(alg, ruta_txt)
    print(f"  {alg}: {t:.2f} ms")