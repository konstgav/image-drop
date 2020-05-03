import os
from video import Video
import json
from filepath import filepath
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "."
ALLOWED_EXTENSIONS = {'avi', 'mov', 'mp4', 'param'}
user = 'konst'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
fpath = filepath(UPLOAD_FOLDER, user)

@app.route('/')
def index():
    return 'test'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fpath.set_videofilename(filename)
            file.save(fpath.to_video_file(filename))
            return render_template('hello.html')
    return render_template('upload.html')

#TODO: убрать говнокод
#TODO: переделать
@app.route('/process/<case>',  methods=['GET', 'POST'])
def process(case):
    if request.method == 'POST':
        fpath.set_case(case)
        json_file = open(fpath.to_param_file(), 'r')
        videoParams = json.load(json_file)
        video = Video(videoParams, fpath)
        video.Run()
        video.AverageNUFFT()
        video.compute_fractal_dimension()
    return render_template('process.html')

@app.route('/uploaded/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')