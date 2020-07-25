def extractor(method, file_dir):
    
    from flask import request
    from werkzeug.utils import secure_filename   
    from datetime import datetime
    import os
    import re

    if method == 'POST':
        image = request.files['file']
        nameArray = os.path.splitext(image.filename)
        replaceName = re.sub('\:|\.','\-', str(datetime.now()))
        filename = secure_filename(replaceName + nameArray[1])
        image.save(os.path.join(file_dir, filename))