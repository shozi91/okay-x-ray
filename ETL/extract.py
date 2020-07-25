def extractor(method, file_dir):
    
    from flask import request
    from werkzeug.utils import secure_filename   
    import os   

    if method == 'POST':
        image = request.files['file']
        filename = secure_filename(image.filename)
        image.save(os.path.join(file_dir, filename))