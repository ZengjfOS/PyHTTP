from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import zipfile
import os
from flask import json
import shutil

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      print(request)
      print(request.form)
      print(request.form["category"])
      print(request.form["function"])
      print("file: " + f.filename)
      if len(f.filename.strip()) > 0:
         # f.save(f.filename)
         shutil.rmtree("tmp", ) 
         shutil.rmtree("workspace") 
         os.makedirs("tmp", exist_ok=True)
         os.makedirs("workspace", exist_ok=True)
         f.save("tmp/" + secure_filename(f.filename))

         if zipfile.is_zipfile("tmp/" + f.filename):
            print("unzip")
            with zipfile.ZipFile("tmp/" + f.filename, 'r') as zip_ref:
               zip_ref.extractall("workspace")
         else:
            shutil.move("tmp/" + f.filename, "workspace/" + f.filename)

         rawData = []
         if f.filename == "data.txt":
            with open("workspace/data.txt") as file:
               for line in file:
                  rawData.append(line.strip())

            data = {"status": "success", "data": rawData}
            response = app.response_class(
               response=json.dumps(data),
               status=200,
               mimetype='application/json'
            )
         else:
            data = {"status": "success", "data": "file uploaded successfully"}
            response = app.response_class(
               response=json.dumps(data),
               status=200,
               mimetype='application/json'
            )

         return response
      else:
         # return redirect("/", code=302)
         data = {"status": "success", "data": "file is empty"}
         response = app.response_class(
             response=json.dumps(data),
             status=200,
             mimetype='application/json'
         )

         return response
   else:
         data = {"status": "success", "data": "must post method"}
         response = app.response_class(
             response=json.dumps(data),
             status=200,
             mimetype='application/json'
         )

         return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
