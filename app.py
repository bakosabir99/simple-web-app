from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is a unique version of the web app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
