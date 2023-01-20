from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/marco/<polo>")
def marco(polo):
    return "my %s" % polo

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)
