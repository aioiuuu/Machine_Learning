from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

RAW_DATA_DIR=ROOT_DIR/"data"/"raw"
PROCESSED_DATA_DIR=ROOT_DIR/"data"/"processed"
LOGS_DIR=ROOT_DIR/"logs"
MODELS_DIR=ROOT_DIR/"models"

SEQ_LEN=5
BATCH_SIZE=128
EMBEDDING_DIM=128
HIDDEN_SIZE=256
LEARNING_RATE=0.001
EPOCHS=5
NUM_WORKERS=2

# 数据采样配置（用于快速训练）
TRAIN_SAMPLE_RATIO=0.3  # 只使用30%的训练数据
