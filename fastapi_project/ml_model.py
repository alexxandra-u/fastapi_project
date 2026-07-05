# ml_model.py
import pickle
import pandas as pd
from pathlib import Path
import reflex as rx

# Глобальная переменная для модели (загружается 1 раз при импорте)
_MODEL = None

def load_model():
    """Загружает модель из assets/ с проверкой наличия файла"""
    global _MODEL
    if _MODEL is not None:
        return _MODEL
    
    model_path = Path(__file__).parent.parent / "assets" / "model.pkl"
    
    if not model_path.exists():
        raise FileNotFoundError(f"Модель не найдена: {model_path}")
    
    with open(model_path, "rb") as f:
        _MODEL = pickle.load(f)
    
    rx.logger.info(f"Модель успешно загружена из {model_path}")
    return _MODEL

def predict(features: dict) -> dict:
    """
    Принимает словарь с признаками, возвращает результат предсказания.
    
    Args:
        features: {
            'age': 30,
            'gender': 'male',
            'salary': 50000,
            'education': 'higher'
        }
    
    Returns:
        {
            'score': 0.85,
            'prediction': 'approved',
            'probability': 0.92
        }
    """
    model = load_model()
    
    # 1. Преобразуем входные данные в DataFrame
    # (Здесь зависит от твоей модели - может потребоваться one-hot encoding)
    df = pd.DataFrame([features])
    
    # 2. Предобработка (если нужно)
    # Например: df = preprocess(df)
    
    # 3. Предсказание
    try:
        # Вариант 1: Если модель возвращает вероятность
        probability = model.predict_proba(df)[0][1]  # Для бинарной классификации
        score = float(probability)
        prediction = "approved" if score >= 0.5 else "rejected"
        
        # Вариант 2: Если просто predict
        # prediction = model.predict(df)[0]
        # score = float(model.predict_proba(df)[0][1])
        
        return {
            'score': round(score, 4),
            'prediction': prediction,
            'probability': round(probability * 100, 2)
        }
    
    except Exception as e:
        rx.logger.error(f"Ошибка при предсказании: {e}")
        raise ValueError(f"Не удалось выполнить предсказание: {e}")