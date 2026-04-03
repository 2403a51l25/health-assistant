from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)

health_tips = {
    "Flu": "Take rest, drink warm water.",
    "Common Cold": "Drink warm fluids and rest.",
    "Allergy": "Avoid dust and allergens.",
    "Migraine": "Rest in a quiet dark room.",
    "Stress": "Relax, sleep well.",
    "Typhoid": "Drink clean water, consult doctor.",
    "Dengue": "Consult doctor immediately.",
    "Weakness": "Eat healthy food.",
    "Diabetes": "Avoid sugar, exercise daily.",
    "Body Pain Issue": "Take rest.",
    "Fever Infection": "Drink fluids and rest.",
    "Throat Infection": "Do salt water gargle."
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    fever = 1 if 'fever' in request.form else 0
    cough = 1 if 'cough' in request.form else 0
    headache = 1 if 'headache' in request.form else 0
    fatigue = 1 if 'fatigue' in request.form else 0
    bodypain = 1 if 'bodypain' in request.form else 0
    cold = 1 if 'cold' in request.form else 0

    result = predict_disease([fever, cough, headache, fatigue, bodypain, cold])
    result = str(result)

    advice = health_tips.get(result, "Consult doctor.")

    # BP
    bp = request.form.get("bp")
    if bp and "/" in bp:
        try:
            bp_val = int(bp.split("/")[0])
            if bp_val > 140:
                advice += " | High BP"
            elif bp_val < 90:
                advice += " | Low BP"
        except:
            pass

    # Temperature
    temp = request.form.get("temp")
    if temp:
        try:
            temp = float(temp)
            if temp > 100:
                advice += " | High temperature (fever)"
        except:
            pass

    # Heart Rate
    hr = request.form.get("hr")
    if hr:
        try:
            hr = int(hr)
            if hr > 100:
                advice += " | High heart rate"
            elif hr < 60:
                advice += " | Low heart rate"
        except:
            pass

    # Sugar
    sugar = request.form.get("sugar")
    if sugar:
        try:
            sugar = int(sugar)
            if sugar > 140:
                advice += " | High sugar"
        except:
            pass

    advice += " | Consult doctor for proper treatment."

    return render_template("index.html", prediction=result, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)