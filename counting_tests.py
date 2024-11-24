import os

def calculate_count_metrics(labels_dir, predictions_dir):
    """
    Calcula as métricas de precisão de contagem (MAE e MAPE) entre ground truths e predições.
    
    labels_dir: Diretório com os arquivos ground truth.
    predictions_dir: Diretório com os arquivos das predições.
    
    Retorna:
    - MAE: Mean Absolute Error
    - MAPE: Mean Absolute Percentage Error
    """
    total_absolute_error = 0
    total_percentage_error = 0
    total_images = 0

    # Iterar pelos arquivos de ground truth
    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)
        prediction_path = os.path.join(predictions_dir, label_file)

        # Verifica se há uma predição correspondente
        if not os.path.exists(prediction_path):
            continue

        # Conta as caixas nas anotações e predições
        with open(label_path, "r") as lf:
            num_real = len(lf.readlines())  # Número de maçãs reais
        
        with open(prediction_path, "r") as pf:
            num_predicted = len(pf.readlines())  # Número de maçãs previstas

        # Calcula o erro absoluto e percentual
        absolute_error = abs(num_real - num_predicted)
        percentage_error = (absolute_error / num_real) * 100 if num_real > 0 else 0

        # Acumula os erros
        total_absolute_error += absolute_error
        total_percentage_error += percentage_error
        total_images += 1

    # Calcula as métricas médias
    mae = total_absolute_error / total_images if total_images > 0 else 0
    mape = total_percentage_error / total_images if total_images > 0 else 0

    return mae, mape


# Diretórios com os arquivos ground truth e predições
labels_dir = "C:/Users/píchau/Documents/TCC/dataset/labels/test"       # Diretório com ground truth
preds_dir = "C:/Users/píchau/Documents/TCC/yolov8-env/runs/detect/predict2/labels"   # Diretório com previsões

# Calcula as métricas
mae, mape = calculate_count_metrics(labels_dir, preds_dir)

# Exibe os resultados
print(f"Erro Absoluto Médio (MAE): {mae:.2f}")
print(f"Erro Relativo Médio (MAPE): {mape:.2f}%")
