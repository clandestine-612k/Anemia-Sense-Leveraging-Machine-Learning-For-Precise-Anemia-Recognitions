import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from PIL import Image
from flask import Flask, request, render_template
import os

# Load the tabular model
model = pickle.load(open('model.pkl', 'rb'))

# Load the TFLite image model
interpreter = tf.lite.Interpreter(model_path="model_anemia.tflite")
interpreter.allocate_tensors()

# Get input and output details of TFLite model
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Check the expected input shape of the TFLite model
input_shape = input_details[0]['shape']
print(f"Input shape of the model: {input_shape}")  # For debugging, to know the input size

# Flask app setup
app = Flask(__name__, static_url_path='/Anemia Sense Leveraging Machine Learning For Precise Anemia Recognitions/static')

# Route: Home
@app.route("/")
def home():
    return render_template("index.html")

# Route: Tabular prediction form
@app.route("/prediction")
def predictpage():
    return render_template("predict.html")

# Route: Handle tabular form prediction
@app.route("/predict", methods=['POST'])
def predict():
    Gender = float(request.form["Gender"])
    Hemoglobin = float(request.form["Hemoglobin"])
    MCH = float(request.form["MCH"])
    MCHC = float(request.form["MCHC"])
    MCV = float(request.form["MCV"])

    features_values = np.array([[Gender, Hemoglobin, MCH, MCHC, MCV]])
    df = pd.DataFrame(features_values, columns=['Gender', 'Hemoglobin', 'MCH', 'MCHC', 'MCV'])

    prediction = model.predict(df)
    result = prediction[0]

    if result == 0:
        message = " you don't have any Anemic Disease"
    else:
        message = " you have Anemic Disease"

    text = "Result: Hence, based on calculation"
    return render_template('predict.html', prediction_text=text + str(message))

# Route: Upload form for image-based prediction
@app.route("/photo_prediction")
def photo_predict_page():
    return render_template("photo_predict.html")

# Helper: Preprocess image (adjusted to match the model's input shape)
def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    # Resize to the input shape of the model (adjusted to (64, 64) based on model input)
    img = img.resize((64, 64))  # Adjust size if the model expects a different size
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Route: Handle image prediction
@app.route("/predict_photo", methods=["POST"])
def predict_photo():
    if "photo" not in request.files:
        return "No file uploaded", 400

    file = request.files["photo"]
    if file.filename == "":
        return "No file selected", 400

    save_path = os.path.join("static/uploads", file.filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    file.save(save_path)

    input_data = preprocess_image(save_path)
    interpreter.set_tensor(input_details[0]["index"], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]["index"])
    prediction = output_data[0][0]  # Assuming the model returns a scalar

    result = "You have Anemic Disease" if prediction < 0.5 else "You don't have Anemic Disease"
    return render_template("result.html", prediction_text=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
