# 🔍 YOLOv4 - Detecção de Objetos com Dataset Customizado

Este projeto executa a detecção de objetos com **YOLOv4**, utilizando imagens rotuladas manualmente com o LabelMe. Ele inclui todo o pipeline: da rotulagem à conversão, treinamento e avaliação.

---

## 📦 Estrutura do Projeto

yolo_custom/

├── data/

│ ├── images/train/ & val/ # Imagens divididas

│ ├── labels/train/ & val/ # Rótulos .txt no formato YOLO

│ ├── obj.names # Nomes das classes

│ ├── obj.data # Configuração do dataset

│ ├── train.txt / val.txt # Listagem de imagens

├── weights/ # Pesos pré-treinados

│ └── yolov4.conv.137

├── yolov4-custom.cfg # Arquivo de config da rede

├── scripts/

│ ├── convert_labelme_to_yolo.py # Converte JSONs para YOLO

│ ├── generate_data_files.py # Divide dataset e cria .txt

│ └── train_yolo.py # Roda o treinamento via subprocess

└── README.md


---

## 🧰 Requisitos

- Python 3.8+
- `Pillow`
- `labelme2yolo` (ou JSON parser manual)
- [Darknet](https://github.com/AlexeyAB/darknet) compilado com GPU
- CUDA/cuDNN (para uso de GPU)

---

## 🖼️ Etapas

### 1. 📌 Rotulagem com LabelMe

Baixe o LabelMe: http://labelme.csail.mit.edu/Release3.0/  
Rotule imagens criando dois ou mais objetos (ex: `garrafa`, `copo`). Exporte os arquivos `.json`.

### 2. 🔁 Conversão para YOLO

python scripts/convert_labelme_to_yolo.py

### 3. 📁 Divisão do Dataset

python scripts/generate_data_files.py


### 4. 🧠 Treinamento com YOLOv4

Prepare o arquivo yolov4-custom.cfg ajustando:

filters = (num_classes + 5) * 3

classes = 2

max_batches = 4000

steps = 3200, 3600

- Inicie o treinamento:
-  python scripts/train_yolo.py

---

🧪 Resultados Esperados

Durante o treinamento, as seguintes métricas serão exibidas:

Loss (box, obj, cls)

mAP (mean Average Precision)

IoU (Intersection over Union)

---

📊 Estimativa de Treinamento

500 imagens, 2 classes, batch=64

~10–20 min em GPU (Colab ou local com CUDA)

Resultados razoáveis a partir de 4000 iterações
