from flask import Flask, request, render_template
from tensorflow import keras
from cleandata import preprocess, spam_response, ham_response
import random

model1 = keras.models.load_model("../h5/success1.h5") 
model1.compile()

app = Flask(__name__)

@app.route("/api/classify", methods = ["POST"])
def classify():
    if request.method == 'POST':
        text = request.form["text"]
        print(text)
     
        processed_text = preprocess(text)
     
        result1= model1.predict(processed_text)
        if result1 > .65:
            classification = 'Spam'
        else:
            classification = 'Ham'
        if classification =='Spam':
            response = random.choice(spam_response)
        if classification == 'Ham':
            response = random.choice(ham_response)
        
        return render_template("spam.html", result={
            "text": text,
            "classification": classification,
            "response": response
            })
    
@app.route("/spam/")
def spam_detector():
    return render_template("spam.html", result = {}
    )

@app.route("/")
def index():
    return render_template("index.html", result = {}
    )


           







if __name__ == '__main__':
   app.run(debug = True)
