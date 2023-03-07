from flask import Flask, request, render_template
from tensorflow import keras



app = Flask(__name__)

model1 = keras.models.load_model("h5/hannahs_model.h5") 
model1.compile()
@app.route("/api/classify", methods = ["POST"])
def classify():
    if request.method == 'POST':
        text = request.form["text"]
        print(text)

      
        # PRE - CLASS
        # processed_text = process(text)
     

        
        # X No of models you have
        result1= model1.predict(text)
        result1 = {
            "classifcation": "SPAM",
            "acc": 90,
            "NAme": "NN"
        }               
        
        return render_template("index.html", result={
            "text": text,
            "classification": "SPAM OR HAM",
            "model1": "model1 result"
        })

@app.route("/")
def index():
    return render_template("index.html", result={})
        

   

if __name__ == '__main__':
   app.run(debug = True)
