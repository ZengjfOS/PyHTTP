from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<a href="/user/zengjf">Hello zengjf</a>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
