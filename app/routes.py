from flask import Blueprint, render_template, request
import joblib
import numpy as np

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/input_form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # Collect all the form data
        age = int(request.form['age'])
        exercise_frequency = int(request.form['exercise_frequency'])
        sleep_hours = int(request.form['sleep_hours'])
        stress_level = int(request.form['stress_level'])
        diet_quality = int(request.form['diet_quality'])
        social_interaction = int(request.form['social_interaction'])
        screen_time = int(request.form['screen_time'])
        meditation_practice = int(request.form['meditation_practice'])

        # Create the input data array
        input_data = np.array([[age, exercise_frequency, sleep_hours, stress_level, diet_quality, social_interaction, screen_time, meditation_practice]])

        print("Input data: ", input_data)  # Debugging line

        return predict(input_data)
    return render_template('input_form.html')

@main.route('/predict', methods=['POST'])
def predict(input_data):
    # Load models
    rf_model = joblib.load('C:/Users/Surem/Documents/mental_fitness_tracker/app/models/random_forest_model.pkl')
    gb_model = joblib.load('C:/Users/Surem/Documents/mental_fitness_tracker/app/models/gradient_boosting_model.pkl')

    # Predict using models
    rf_prediction = rf_model.predict(input_data)
    gb_prediction = gb_model.predict(input_data)

    print("RF Prediction: ", rf_prediction)  # Debugging line
    print("GB Prediction: ", gb_prediction)  # Debugging line

    # For now, just showing the RandomForest prediction
    prediction = rf_prediction[0]

    return render_template('prediction.html', prediction=prediction)