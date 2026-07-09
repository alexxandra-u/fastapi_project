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
    
    print('Модель загрузилась')
    return _MODEL

def preprocess(df):
    df['CODE_GENDER'] = df['gender'].replace({'Male': 'M', 'Female': 'F'})
    df['FLAG_OWN_CAR'] = df['car'].replace({'Yes': 'Y', 'No': 'N'})
    df['FLAG_OWN_REALTY'] = df['property'].replace({'Yes': 'Y', 'No': 'N'})
    df['FLAG_MOBIL'] = df['mob_phone'].notnull()
    df['FLAG_WORK_PHONE'] = df['work_phone'].notnull()
    df['FLAG_PHONE'] = df['FLAG_MOBIL'] | df['FLAG_WORK_PHONE']
    df['FLAG_EMAIL'] = df['email'].notnull()
    df['DAYS_BIRTH'] = (pd.Timestamp.now() - pd.to_datetime(df['date_of_birth'])).dt.days
    df['DAYS_EMPLOYED'] = (pd.Timestamp.now() - pd.to_datetime(df['date_of_emp'])).dt.days
    df['CNT_CHILDREN'] = df['children']
    df['AMT_INCOME_TOTAL'] = df['income_amount']
    df['NAME_INCOME_TYPE'] = df['income_type']
    df['NAME_EDUCATION_TYPE'] = df['education']
    df['NAME_FAMILY_STATUS'] = df['marital_status']
    df['NAME_HOUSING_TYPE'] = df['housing']
    df['OCCUPATION_TYPE'] =  df['occupation']
    df['CNT_FAM_MEMBERS'] = df['family'].astype(int)
    return df

def predict(features: dict) -> dict:
    model = load_model()
    
    names = ["name", "email", "gender", "age", "date_of_birth", "mob_phone", "work_phone", "property", "car", "education", "income_type", "income_amount", "date_of_emp", "occupation", "marital_status", "children", "family", "housing"]
    print(len(features), len(names))
    df = pd.DataFrame([features], columns = names)

    print('here 1')
    df = preprocess(df)

    print('here 2')
    cat_features = ['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','OCCUPATION_TYPE']
    for feat in cat_features:
        df[feat] = df[feat].astype('category')

    print('here 3')

    try:
        probability = model.predict_proba(df[model.feature_names_in_])[0][0]
        print(probability)
        score = float(probability)
        prediction = "approved" if score >= 0.5 else "rejected"

        
        return {
            'score': round(score, 4),
            'prediction': prediction,
            'probability': round(probability * 100, 2)
        }
    
    except Exception as e:
        print(f"Ошибка при предсказании: {e}")
        raise ValueError(f"Не удалось выполнить предсказание: {e}")