import os

def calculate_global_iou(iou_results):
    """
    Calcula o IoU geral (IoU médio) com base nos IoUs individuais de cada arquivo.
    """
    total_iou = 0
    total_ground_truths = 0

    for file_name, iou_list in iou_results.items():
        total_iou += sum(iou_list)  # Soma dos IoUs de todas as ground truths
        total_ground_truths += len(iou_list)  # Número de ground truths

    if total_ground_truths == 0:
        return 0  # Evita divisão por zero, caso não haja ground truths

    return total_iou / total_ground_truths

def load_boxes_from_txt(file_path):
    """
    Lê caixas delimitadoras de um arquivo YOLO .txt.
    Retorna uma lista de caixas no formato (class_id, x_center, y_center, width, height).
    """
    boxes = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])
            boxes.append((class_id, x_center, y_center, width, height))
    return boxes

def convert_to_absolute(box, img_width, img_height):
    """
    Converte uma caixa YOLO normalizada para coordenadas absolutas.
    """
    class_id, x_center, y_center, width, height = box
    x_min = (x_center - width / 2) * img_width
    y_min = (y_center - height / 2) * img_height
    x_max = (x_center + width / 2) * img_width
    y_max = (y_center + height / 2) * img_height
    return class_id, x_min, y_min, x_max, y_max

def calculate_iou(box1, box2):
    """
    Calcula o IoU entre duas caixas no formato (x_min, y_min, x_max, y_max).
    """
    x_min_inter = max(box1[0], box2[0])
    y_min_inter = max(box1[1], box2[1])
    x_max_inter = min(box1[2], box2[2])
    y_max_inter = min(box1[3], box2[3])

    inter_width = max(0, x_max_inter - x_min_inter)
    inter_height = max(0, y_max_inter - y_min_inter)
    inter_area = inter_width * inter_height

    area_box1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area_box2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = area_box1 + area_box2 - inter_area

    return inter_area / union_area if union_area > 0 else 0

def calculate_iou_for_directories(labels_dir, preds_dir, img_width=640, img_height=480):
    """
    Calcula o IoU para cada arquivo em `labels_dir` e `preds_dir`.
    """
    results = {}
    for gt_file in os.listdir(labels_dir):
        gt_path = os.path.join(labels_dir, gt_file)
        pred_path = os.path.join(preds_dir, gt_file)

        if not os.path.exists(pred_path):
            print(f"A previsão para {gt_file} não foi encontrada em {preds_dir}.")
            continue

        gt_boxes = load_boxes_from_txt(gt_path)
        pred_boxes = load_boxes_from_txt(pred_path)

        iou_list = []
        for gt_box in gt_boxes:
            gt_abs = convert_to_absolute(gt_box, img_width, img_height)
            best_iou = 0
            for pred_box in pred_boxes:
                pred_abs = convert_to_absolute(pred_box, img_width, img_height)
                iou = calculate_iou(gt_abs[1:], pred_abs[1:])  # Ignorar class_id
                best_iou = max(best_iou, iou)
            iou_list.append(best_iou)

        results[gt_file] = iou_list

    return results

# Diretórios contendo os arquivos .txt
labels_dir = "C:/Users/píchau/Documents/TCC/dataset/labels/test_preprocessed"       # Diretório com ground truth
preds_dir = "C:/Users/píchau/Documents/TCC/yolov8-env/runs/detect/predict_clahe_gauss/labels"   # Diretório com previsões

# Dimensões das imagens (modifique se necessário)
img_width = 1024
img_height = 1024

# Cálculo do IoU
iou_results = calculate_iou_for_directories(labels_dir, preds_dir, img_width, img_height)

# Cálculo do IoU global
global_iou = calculate_global_iou(iou_results)

# Exibir resultados
for file_name, iou_list in iou_results.items():
    print(f"{file_name}: IoUs = {iou_list}")
    
# Exibir resultado global
print(f"IoU global: {global_iou}")
