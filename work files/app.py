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

    # try:
    app.config["IMAGE_UPLOADS"] = os.path.join("Upload","xray")
        #extract the data 
    extract.extractor(app.config["IMAGE_UPLOADS"])

        #transform the data
    predictions = transform.transformer()
        #load the data
    load.loader()
    # except Exception as e:
    #     print(e)
    normal = predictions[0][0]
    sick = predictions[0][1]

    
    if normal-sick > 0.5:
        result = "very confident of a healthy result"
    elif normal-sick > 0.35:
        result = "confident of a healthy result"
    elif normal-sick < 0.35 & normal-sick > 0.50:
        result = "tendency towards a healthy result"
    elif sick - normal > 0.5:
        result = "very confident of a sick result"
    elif sick - normal > 0.35:
        result = "confident of a sick result"
    elif sick - normal < 0.35 & normal-sick > 0.50:
        result = "tendency towards a sick result"

    return render_template("index2.html", predictions_data = predictions, result=result)

#################################################

@app.route("/stats")
def stats():
    return render_template("stats.html")

#################################################

# @app.route("/predictions")
# def predictions():
#     return 1

if __name__ == '__main__':
    app.run(debug=True)
    
