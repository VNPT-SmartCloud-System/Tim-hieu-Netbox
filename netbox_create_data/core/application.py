import os, sys
from flask import Flask, flash, request, redirect, render_template
from flask.wrappers import Response
from werkzeug.utils import secure_filename
import run
import review_excel
import time

app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Không có tệp được tải lên')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            link_src = UPLOAD_FOLDER +"/" + filename
            file_dst = UPLOAD_FOLDER +"/" + 'netbox_info.xlsx'
            try:
                os.remove(file_dst)
            except Exception as ex:
                print(ex)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.rename(link_src, file_dst)
            flash('File successfully uploaded')
            return redirect('/run')
        else:
            flash('Error!! Chỉ có tệp xlsx được phép')
            return redirect(request.url)

@app.route('/content')
def content():
    def run_netbox():
        sys.stdout
        sys.stdout = open('log.txt', 'w')
        run.main()
        sys.stdout.close()
        return
    def inner():
        run_netbox()
        read_log = open("log.txt", "r")
        for i in read_log:
            time.sleep(1)
            yield str(i) + '<br/>\n'
        os.remove("log.txt")
    return Response(inner(), mimetype='text/html')

@app.route('/run')
def run_netbox():
    return render_template('run.html')  #Response(inner(), mimetype='text/html')

@app.route('/run', methods=['POST'])
def run_file():
    return render_template('content.html.jinja')

@app.route('/check')
def run_check():
    def run_netbox():
        sys.stdout
        sys.stdout = open('log.txt', 'w')
        review_excel.main()
        sys.stdout.close()
        return
    def inner():
        run_netbox()
        read_log = open("log.txt", "r")
        for i in read_log:
            time.sleep(1)
            yield str(i) + '<br/>\n'
        os.remove("log.txt")
    return Response(inner(), mimetype='text/html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5001, debug = False)