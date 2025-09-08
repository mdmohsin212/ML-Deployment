from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello, I am Mohsin")

@app.route('/page2')
def page():
    return("This is page 2")

@app.route('/admin')
def hello_2():
    return("I am Admin!!")

app.run(debug=True)
