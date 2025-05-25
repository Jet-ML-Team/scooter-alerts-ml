import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# === Базовая директория проекта (jet_alerts/)
BASE_DIR = Path(__file__).resolve().parent

# === Добавим корень проекта в sys.path (для импорта из notebooks)
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# === Загрузка .env
load_dotenv(dotenv_path=BASE_DIR / ".env")

# === Базовые папки
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# === Автоматическое создание директорий (если их нет)
for directory in [DATA_DIR, MODELS_DIR, NOTEBOOKS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# === Функции для получения путей
def data_path(filename: str) -> Path:
    return DATA_DIR / filename

def model_path(filename: str) -> Path:
    return MODELS_DIR / filename

def notebook_path(filename: str) -> Path:
    return NOTEBOOKS_DIR / filename

# === Конфиг подключения к БД
DB_URI = (
    f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}'
    f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
    f'?sslmode={os.getenv("DB_SSLMODE")}'
)
