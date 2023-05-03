from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the flask apps. This is the great option"

@app.route('/checks')
def checks():
    return "let's use the flask for web development"


if __name__=='__main__':
    app.run(debug = True)