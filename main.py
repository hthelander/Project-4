from flask import Flask, request, render_template

app = Flask(__name__)

# model1 = keras.loads("model1.h5") X no of models you have

@app.route("/api/classify", methods = ["POST"])
def classify():
    if request.method == 'POST':
        text = request.form["text"]
        print(text)

        
        # PRE - CLASS
        from testfunction import preprocess
        processed_text = preprocess(text)
        

        """
        # X No of models you have
        result1= model1.predict(processed_text)
         """    
        result1 = {
            "classifcation": "SPAM",
            "acc": 90,
            "NAme": "NN",
            "processed": processed_text
        }
                   
        
        return render_template("index.html", result={
            "text": text,
            "classification": "spam or ham",
            "groucho": "I've had a wonderful evening, but this wasn't it",
            "model1": "model1 result",
            "result": result1
        })

@app.route("/")
def index():
    return render_template("index.html", result={})
        

   

if __name__ == '__main__':
   app.run(debug = True)
