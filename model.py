import joblib
# Datos fijos para prueba
features = [[20, 8, 5, 50, 50, 8, 70, 20, 3, 1, 7]]
# Cargar el modelo
modelo = joblib.load("modelo_regresion.pkl")
# Hacer la predicción
prediccion = modelo.predict(features)
print("Predicción:", prediccion[0])
