def loader():

    from sqlalchemy import create_engine
    # from config import postgres_conn_str, upload_database

    #create database connection
    #engine = create_engine(f'postgresql://{postgres_conn_str}{upload_database}')
    #insert df into postgres
    #<DATAFRAME>.to_sql(name='country_rankings', con=engine, if_exists='replace', index=False)

    import glob
    import shutil
    from sqlalchemy import create_engine
    import traceback
    from PIL import Image
    import os

    image_list = []
    for filename in glob.glob(os.path.join('Upload','xray','*')):
        im=Image.open(filename)
        image_list.append(im)
        im.close()
        try:
            shutil.copy(filename, 'archived')
            os.remove(filename)
        except:
            traceback.print_exc()