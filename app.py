########################################################
# this file calls etl modules
########################################################
from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file
from ETL import extract2, transform, load
from werkzeug.utils import secure_filename
import os

archived_folder= os.path.join('archived')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
app.config['archived'] = archived_folder

@app.route('/image/<filename>')
def get_image(filename):
    return send_file('archived/'+filename)

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
            filename = extract2.extractor(app.config["IMAGE_UPLOADS"])
            #print(file_path)    
            #transform the data
            predictions = transform.transformer()
            #load the data
            load.loader()
            #except Exception as e:
            #    print(e)
            normal = predictions[0][0]
            sick = predictions[0][1]
            result = 'Too close to predict!'


            if normal-sick > 0.5:
                result = "Very confident of a healthy result."
            elif normal-sick > 0.35:
                result = "Confident of a healthy result."
            elif normal-sick > 0.20:
                result = "Tendency towards a healthy result."
            elif sick - normal > 0.5:
                result = "Very confident of a sick result."
            elif sick - normal > 0.35:
                result = "Confident of a sick result."
            elif sick - normal > 0.2:
                result = "Tendency towards a sick result."

            return render_template("index2.html", predictions_data = predictions, result=result, img_path = filename)
            #return redirect(url_for("index3.html", predictions_data = predictions, result=result, img_path = file_path))          
    
    
    
    return render_template("index3.html", predictions_data = ['',''], result='' )

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
    
