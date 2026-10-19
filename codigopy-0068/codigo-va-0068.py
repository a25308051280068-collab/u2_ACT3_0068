import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

print("Christian garcia jimenez Nc=0068")

# -----------------------------------------
# 1. Rutas absolutas según la estructura
# -----------------------------------------
CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

RUTA_IMAGEN = (
    CARPETA_PROYECTO
    / "img-original-0068"
    / "img-mercedes-0068.jpg"
)

CARPETA_RESULTADOS = CARPETA_PROYECTO / "resultados-img-0068"
CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. Lectura y preparación de imagen
# -----------------------------------------
if not RUTA_IMAGEN.is_file():
    print(f"ERROR: No se encontró la imagen en {RUTA_IMAGEN}")
    raise SystemExit(1)

img_bgr = cv2.imread(str(RUTA_IMAGEN))
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Separación de canales
R, G, B = cv2.split(img_rgb)

# Matriz de ceros para aislar el color
ceros = np.zeros_like(R)

# Reconstrucción de canales individuales con color
canal_rojo = cv2.merge([R, ceros, ceros])   # Solo canal Rojo activo
canal_verde = cv2.merge([ceros, G, ceros])  # Solo canal Verde activo
canal_azul = cv2.merge([ceros, ceros, B])   # Solo canal Azul activo

# -----------------------------------------
# 3. Visualización con Matplotlib
# -----------------------------------------
fig = plt.figure(figsize=(10, 8))

# CANAL ROJO A COLOR
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(canal_rojo)
ax1.set_title("CANAL ROJO")

# CANAL VERDE A COLOR
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(canal_verde)
ax2.set_title("CANAL VERDE")

# CANAL AZUL A COLOR
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(canal_azul)
ax3.set_title("CANAL AZUL")

# IMAGEN ORIGINAL RECONSTRUIDA
imgre = cv2.merge([R, G, B])
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

plt.tight_layout()

# Guardar resultado
ruta_figura = CARPETA_RESULTADOS / "canales-descompuestos-0068.png"
plt.savefig(str(ruta_figura))

plt.show()

print("Christian garcia jimenez Nc=0068")