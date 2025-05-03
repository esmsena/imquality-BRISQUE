from imquality.brisque import score
from PIL import Image
import numpy as np

# Abrir a imagem e converter para RGB
img = Image.open("niqe_env/sua_imagem.jpeg").convert("RGB")
img_array = np.array(img)

# Verificar o formato da imagem
print(f"Formato da imagem antes de calcular BRISQUE: {img_array.shape}")

# Garantir que a imagem tenha 3 canais
if len(img_array.shape) == 2:  # Caso seja escala de cinza
    img_array = np.stack((img_array,) * 3, axis=-1)

# Forçar o formato correto antes de passar para o BRISQUE
if img_array.shape[-1] != 3:
    raise ValueError(f"A imagem deve ter 3 canais, mas tem {img_array.shape[-1]} canais.")

# Calcular BRISQUE
try:
    brisque_score = score(img_array)
    print(f"BRISQUE Score: {brisque_score:.2f}")

    # Avaliar a qualidade da imagem
    if brisque_score < 20:
        qualidade = "boa"
    elif 20 <= brisque_score < 50:
        qualidade = "ruim"
    else:
        qualidade = "péssima"

    print(f"A qualidade da imagem é: {qualidade}")

    # Sugerir tirar uma nova foto se a qualidade for ruim ou péssima
    if qualidade in ["ruim", "péssima"]:
        print("A qualidade da imagem está ruim. Por favor, tire uma nova foto.")

except ValueError as e:
    print(f"Erro ao calcular BRISQUE: {e}")