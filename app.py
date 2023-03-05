from app import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import engine, create_engine, func, inspect



app = Flask(__name__)
engine = sqlalchemy.create_engine("sqlite:///nps.sqlite",echo=False)
print(inspect(engine).get_table_names())


@app.route("/")
def welcome():
  return render_template('index.html')

@app.route("/api/v1.0/")
def parks():
    
    results = engine.execute("select * from clean_df")
    return jsonify([dict(_) for _ in results])