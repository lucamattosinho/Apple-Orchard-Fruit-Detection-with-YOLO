# -*- coding: utf-8 -*-
import numpy as np
import cv2
import cv2_ext
import os
from glob import glob

# Diretórios de entrada e saída
input_dir = "C:\\Users\\píchau\\Documents\\TCC\\dataset\\images\\test"
output_dir = "C:\\Users\\píchau\\Documents\\TCC\\dataset\\images\\test_preprocessed"

print(input_dir)
# Criar diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Configuração do CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_paths = glob(os.path.join(input_dir, "*.png"))
files = os.listdir(input_dir)
print("Imagens encontradas:", image_paths)
# Pré-processar todas as imagens
for image_path in glob(os.path.join(input_dir, "*.png")):
    print(f"Pré-processando {image_path}")
    # Carregar imagem
    img = cv2_ext.imread(image_path)
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir intervalos de cor para vermelho
    intervalo_baixo1 = np.array([0, 25, 25])   # Vermelho inicial
    intervalo_alto1 = np.array([10, 255, 255])
    intervalo_baixo2 = np.array([160, 100, 100]) # Vermelho final
    intervalo_alto2 = np.array([180, 255, 255])

    # Criar máscaras para os intervalos de vermelho
    mascara1 = cv2.inRange(hsv, intervalo_baixo1, intervalo_alto1)
    mascara2 = cv2.inRange(hsv, intervalo_baixo2, intervalo_alto2)

    mascara = cv2.bitwise_or(mascara1, mascara2)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    mascara_limpa = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
    mascara_limpa = cv2.morphologyEx(mascara_limpa, cv2.MORPH_OPEN, kernel)

    # Aplicar máscara na imagem original
    img_realce = cv2.bitwise_and(img, img, mask=mascara_limpa)
    '''
    
    blurred = cv2.GaussianBlur(img, (9, 9), 0)

    # Definir o fator de amplificação (A)
    A = 1.5

    # Aplicar o filtro high-boost
    high_boost = cv2.addWeighted(img, A, blurred, -0.7, 0)


    alpha = 1.2  # Contraste (1.2)
    beta = 20    # Brilho (20)
    adjusted = cv2.convertScaleAbs(high_boost, alpha=alpha, beta=beta)
    high_boost = np.clip(high_boost, 0, 255).astype(np.uint8)
    '''
    # Converter para o espaço LAB
    lab = cv2.cvtColor(high_boost, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Aplicar CLAHE ao canal L
    l_clahe = clahe.apply(l)

    # Recombinar os canais
    lab_clahe = cv2.merge((l_clahe, a, b))

    # Converter de volta para BGR
    img_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)
    '''
    # Salvar imagem pré-processada
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2_ext.imwrite(output_path, high_boost)

print(f"Imagens pré-processadas salvas em {output_dir}")
