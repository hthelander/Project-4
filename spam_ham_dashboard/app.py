from flask import Flask, request, render_template

app = Flask(__name__)

# model1 = keras.loads("model1.h5") X no of models you have

@app.route("/")
def index():
    return render_template("index.html", result={})
        
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
 

if __name__ == '__main__':
   app.run(debug = True)
