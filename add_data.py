import io
from fastapi import FastAPI, File
from PIL import Image

app = FastAPI()

@app.post("/add-data")
async def add_receipt_data(file: bytes = File(), label: str = ""):
    # 이미지를 train 폴더에 저장, gt_train.txt 에 라인 추가

@app.post("/train")
async def train():
    # CUDA_VISIBLE_DEVICES=0 python3 ./deep-text-recognition-benchmark/train.py \
    # --train_data ./deep-text-recognition-benchmark/ocr_data/train \
    # --valid_data ./deep-text-recognition-benchmark/ocr_data/validation \
    # --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction CTC \
    # --batch_size 512 --batch_max_length 200 --data_filtering_off --workers 0 \
    # --num_iter 100000 --valInterval 100
    # --saved_model ./saved_models/TPS-ResNet-BiLSTM-CTC.pth
