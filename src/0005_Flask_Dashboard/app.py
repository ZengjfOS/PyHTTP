from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import zipfile
import os

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
