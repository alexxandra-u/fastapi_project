# ml_model.py
import pickle
import pandas as pd
from pathlib import Path
import reflex as rx

# Глобальная переменная для модели (загружается 1 раз при импорте)
_MODEL = None

def load_model():
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

def preprocess(df):
    print(df.columns)
    return df

def predict(features: dict) -> dict:
    model = load_model()
    
    df = pd.DataFrame([features], columns = ['Name', 'email', 'gender', 'age', 'property', 'car'])
    
    df = preprocess(df)
    
    try:
        probability = model.predict(df)[0]
        score = float(probability)
        prediction = "approved" if score >= 0.5 else "rejected"

        
        return {
            'score': round(score, 4),
            'prediction': prediction,
            'probability': round(probability * 100, 2)
        }
    
    except Exception as e:
        rx.logger.error(f"Ошибка при предсказании: {e}")
        raise ValueError(f"Не удалось выполнить предсказание: {e}")