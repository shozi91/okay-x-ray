def extractor(file_dir):
    
    from flask import request
    from werkzeug.utils import secure_filename   
    from datetime import datetime
    import os
    import re
    import uuid

    image = request.files['file']
    nameArray = os.path.splitext(image.filename)
    replaceName = re.sub('\:|\.','_', str(datetime.now()))
    filename = secure_filename(f'{replaceName}_{uuid.uuid4().hex}{nameArray[1]}')
    file_path = os.path.join(file_dir, filename)
    image.save(file_path)
