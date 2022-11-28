from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def url_prediction():
    url = request.form['text']
    create_csv(url)
    prepare_data()
    prediction = apply_model()
    
    # Predict with model
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
