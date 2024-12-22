import joblib
import numpy as np

def load_models():
    rf_model = joblib.load('C:/Users/Surem/Documents/mental_fitness_tracker/app/models/random_forest_model.pkl')
    gb_model = joblib.load('C:/Users/Surem/Documents/mental_fitness_tracker/app/models/gradient_boosting_model.pkl')
    return rf_model, gb_model

def predict(age, rf_model, gb_model):
    input_data = np.array([[age]])  # Add other features as needed
    rf_prediction = rf_model.predict(input_data)
    gb_prediction = gb_model.predict(input_data)
    return rf_prediction[0], gb_prediction[0]
