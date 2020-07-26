########################################################
# this file calls etl modules
########################################################
from flask import Flask, jsonify, request, render_template, redirect, url_for
from ETL import extract2, transform, load
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        #check to see if post request has a file
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        #if user does not select file
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #try:
            app.config["IMAGE_UPLOADS"] = os.path.join("Upload","xray")
                #extract the data 
            file_path = extract2.extractor(app.config["IMAGE_UPLOADS"])
            #print(file_path)    
            #transform the data
            predictions = transform.transformer()
            #load the data
            load.loader()
            #except Exception as e:
            #    print(e)
            normal = predictions[0][0]
            sick = predictions[0][1]

    
            if normal-sick > 0.5:
                result = "very confident of a healthy result"
            elif normal-sick > 0.35:
                result = "confident of a healthy result"
            elif 0.35 <  (normal-sick) > 0.01:
                result = "tendency towards a healthy result"
            elif sick - normal > 0.5:
                result = "very confident of a sick result"
            elif sick - normal > 0.35:
                result = "confident of a sick result"
            elif 0.35 <  (sick - normal) > 0:
                result = "tendency towards a sick result"
            return render_template("index2.html", predictions_data = predictions, result=result, img_path = file_path)
            #return redirect(url_for("index3.html", predictions_data = predictions, result=result, img_path = file_path))          
    
    return render_template("index3.html", predictions_data = ['',''], result='', img_path = '')

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
    
