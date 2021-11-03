from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import zipfile
import os

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      print(f)
      # f.save(f.filename)
      os.makedirs("tmp", exist_ok=True)
      os.makedirs("workspace", exist_ok=True)
      f.save("tmp/" + secure_filename(f.filename))

      if zipfile.is_zipfile("tmp/" + f.filename):
         print("unzip")
         with zipfile.ZipFile("tmp/" + f.filename, 'r') as zip_ref:
            zip_ref.extractall("workspace")

      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
