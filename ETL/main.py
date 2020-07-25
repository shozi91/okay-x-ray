########################################################
# this file calls etl modules
########################################################
from flask import Flask, jsonify, request, render_template
from extract import extractor
from transform import transformer
from load import loader
import os

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder='../templates/')

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

#################################################

@app.route("/etl", methods = ['GET', 'POST'])
def etl():

    #extract the data
    app.config["IMAGE_UPLOADS"] = os.path.join(os.path.dirname(os.getcwd()), "Upload", "saved", "normal")
    extractor(request.method, app.config["IMAGE_UPLOADS"])

    #transform the data
    predictions, y_class = transformer()
    #load the data
    loader(predictions, y_class)

    return render_template("index.html")

#################################################

@app.route("/stats")
def stats():
    return 1

#################################################

@app.route("/predictions")
def predictions():
    return 1

if __name__ == '__main__':
    app.run(debug=True)
    