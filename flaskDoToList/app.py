from flask import Flask
app= Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"

@app.route('/siuu')
def siu():
    return "Hello world! siuu"

if __name__ == "__main__":
    app.run(debug=True)