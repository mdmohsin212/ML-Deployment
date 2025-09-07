from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["radius_mean"]),
        float(request.form["texture_mean"]),
        float(request.form["perimeter_mean"]),
        float(request.form["smoothness_mean"]),
        float(request.form["compactness_mean"])
    ]
    
    prediction = model.predict([features])[0]
    
    proba = None
    if prediction == 1:
        proba = model.predict_proba([features])[0][1]
    
    return render_template(
        "home.html",
        prediction="Malignant" if prediction == 1 else "Benign",
        proba=proba
    )

if __name__ == "__main__":
    app.run(debug=True) 