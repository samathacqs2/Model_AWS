# ☁️ Model_AWS — Simple Regression Model Deployment Example

This repository contains a minimal example of loading and using a trained regression model in Python. The model is saved as a `.pkl` file and used for local inference. This setup can later be adapted for deployment on cloud services like **AWS Lambda**, **SageMaker**, or **EC2**.

---

## 📦 Project Contents

```
├── model.py                 # Script to load the model and make a prediction
├── modelo_regresion.pkl     # Trained regression model using scikit-learn
```

---

## 🚀 How It Works

The script loads a pre-trained regression model using `joblib` and performs a prediction on a fixed set of input features.

### 🔢 Example Features Used

```python
features = [[20, 8, 5, 50, 50, 8, 70, 20, 3, 1, 7]]
```

> These values could represent any numeric features (e.g., medical, environmental, etc.), depending on how the model was trained.

### 🧠 Prediction Logic

```python
import joblib

# Load model
modelo = joblib.load("modelo_regresion.pkl")

# Input features
features = [[20, 8, 5, 50, 50, 8, 70, 20, 3, 1, 7]]

# Predict
prediccion = modelo.predict(features)
print("Predicción:", prediccion[0])
```

---

## 🛠 Requirements

- Python 3.7+
- scikit-learn
- joblib

Install dependencies with:

```bash
pip install -r requirements.txt
```

*(You may need to create `requirements.txt` with the following content if not included yet)*:

```text
scikit-learn
joblib
```

---

## 🌐 Cloud Deployment Note

This simple structure is ideal for wrapping into:

- **AWS Lambda** (for real-time inference via API Gateway)
- **SageMaker endpoint**
- **Dockerized microservice** for EC2 or Fargate

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or reach out on GitHub.

---

