from flask import Flask, request, render_template
<<<<<<< HEAD
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
        # result1 = {
        #     "classification": "SPAM",
        #     "acc": 90,
        #     "NAme": "NN"
        # }               
        
        return render_template("index.html", result={
            "text": text,
            "classification": classification, 
            # "model1": result1
        })
=======

app = Flask(__name__)

# model1 = keras.loads("model1.h5") X no of models you have
>>>>>>> d3c9ea1616f69d87902b99b3fac0502109dd7154

@app.route("/")
def index():
    return render_template("index.html", result={})
        
<<<<<<< HEAD

   
=======
@app.route("/api/classify/<message>")
def classify(message=None):  
    
    print("========== /api/classify =========")
    print(message)
    print("==================================")
        
    if message == "hello":
        result = "SPAM" 
    else:
       result = "HAM" 
             
    return ({"result": result})
 
>>>>>>> d3c9ea1616f69d87902b99b3fac0502109dd7154

if __name__ == '__main__':
   app.run(debug = True)
