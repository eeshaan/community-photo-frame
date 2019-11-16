import os

from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

app = Flask(__name__)
bootstrap = Bootstrap(app)
dropzone = Dropzone(app)

app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'thanks'

app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # handle image upload from Dropzone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            filename = photos.save(
                file,
                name=file.filename
            )
    return render_template('index.html')

@app.route('/thanks')
def thanks():
  return render_template('thanks.html')

if __name__ == "__main__":
    app.run("0.0.0.0")
