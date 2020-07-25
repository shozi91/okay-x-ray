########################################################
# this file calls etl modules
########################################################
from flask import Flask, jsonify, request, render_template
from ETL import extract, transform, load
import os
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

#################################################

@app.route("/etl", methods = ['POST'])
def etl():
    try:
        app.config["IMAGE_UPLOADS"] = os.path.join("Upload","xray")
        #extract the data 
        extract.extractor(app.config["IMAGE_UPLOADS"])

        #transform the data
        predictions = transform.transformer()
        #load the data
        load.loader()
    except Exception as e:
        print(e)

    return render_template("index.html", predictions_data = predictions)

#################################################

@app.route("/stats")
def stats():
    return render_template("stats.html")

#################################################

@app.route("/predictions")
def predictions():
    return 1

if __name__ == '__main__':
    app.run(debug=True)
    
