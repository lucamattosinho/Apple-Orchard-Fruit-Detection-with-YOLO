import os

'''
Script used to verify and correct YOLO annotations.
'''

# Path to the directory containing the annotation files
annotations_dir = r'C:\Users\píchau\Documents\TCC\dataset\labels\val'
num_classes = 1

def check_and_correct_annotations(annotations_dir):
    # Lists all files in the directory
    for filename in os.listdir(annotations_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(annotations_dir, filename)
            lines_to_write = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    parts = line.strip().split()
                    if len(parts) != 5:
                        print(f'Arquivo {filename}: Linha inválida (esperado 5 partes): {line.strip()}')
                        continue

                    # Verifies if the class ID is valid
                    class_id = int(parts[0])
                    if class_id < 0 or class_id >= num_classes:
                        print(f'Arquivo {filename}: ID de classe inválido: {class_id} na linha: {line.strip()}')
                        parts[0] = '0'  # Changes the class ID to 0

                    # Verifies if the bounding box coordinates are valid
                    try:
                        center_x = float(parts[1])
                        center_y = float(parts[2])
                        width = float(parts[3])
                        height = float(parts[4])

                        if not (0 <= center_x <= 1):
                            print(f'Arquivo {filename}: center_x fora do intervalo [0, 1]: {center_x} na linha: {line.strip()}')
                        if not (0 <= center_y <= 1):
                            print(f'Arquivo {filename}: center_y fora do intervalo [0, 1]: {center_y} na linha: {line.strip()}')
                        if not (0 <= width <= 1):
                            print(f'Arquivo {filename}: width fora do intervalo [0, 1]: {width} na linha: {line.strip()}')
                        if not (0 <= height <= 1):
                            print(f'Arquivo {filename}: height fora do intervalo [0, 1]: {height} na linha: {line.strip()}')
                    except ValueError:
                        print(f'Arquivo {filename}: Erro ao converter valores para float na linha: {line.strip()}')

                    # Adds the corrected line to the list
                    lines_to_write.append(" ".join(parts) + "\n")

            # Writes the corrected annotations to the file
            with open(file_path, 'w') as file:
                file.writelines(lines_to_write)
            print(f'Arquivo {filename}: Anotações corrigidas e salvas.')

if __name__ == '__main__':
    check_and_correct_annotations(annotations_dir)
