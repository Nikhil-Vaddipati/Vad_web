import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'wav'}

app.config['UPLOAD_FOLDER'] = "content"


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/download')
def down():
    return render_template("download.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(subprocess.check_output(['python','script.py',file.filename]))
            x=subprocess.check_output(['python','script.py',file.filename])
            
            return x
    return render_template("uploading.html")
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''

if __name__ == '__main__':
    app.run(debug=True)

