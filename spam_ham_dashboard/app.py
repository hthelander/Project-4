from flask import Flask, request, render_template

from tensorflow import keras
from cleandata import preprocess



app = Flask(__name__)

model1 = keras.models.load_model("../h5/success1.h5") 
model1.compile()
@app.route("/api/classify", methods = ["POST"])
def classify():
    if request.method == 'POST':
        text = request.form["text"]
        print(text)

      
        # PRE - CLASS
        processed_text = preprocess(text)
     

        
        # X No of models you have
        result1= model1.predict(processed_text)
        if result1 > .65:
            classification = 'Spam'
        else:
            classification = 'Ham'
             
        
        return render_template("index.html", result={
            "text": text,
            "classification": classification, 
           

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result={})
        


if __name__ == '__main__':
   app.run(debug = True)
