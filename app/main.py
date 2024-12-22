import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt
import joblib
import numpy as np

class MentalFitnessTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mental Fitness Tracker")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.form_layout = QFormLayout()
        self.age_input = QLineEdit()
        self.form_layout.addRow("Age:", self.age_input)
        # Add other input fields for habits and other data as needed

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.predict)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.result_label)

    def predict(self):
        age = int(self.age_input.text())
        # Collect other data from form inputs

        # Load models
        rf_model = joblib.load('app/models/random_forest.pkl')
        gb_model = joblib.load('app/models/gradient_boosting.pkl')

        # Prepare input data for prediction
        input_data = np.array([[age]])  # Add other features as needed

        # Predict using models
        rf_prediction = rf_model.predict(input_data)
        gb_prediction = gb_model.predict(input_data)

        # For now, just showing the RandomForest prediction
        prediction = rf_prediction[0]

        self.result_label.setText(f"Overall Prevalence: {prediction:.2f}")

def main():
    app = QApplication(sys.argv)
    window = MentalFitnessTracker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()