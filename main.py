from flask import Flask


app = Flask(__name__)

@app.route("/joke", methods = ["GET"])
def givejoke():
    return "knock koncok.. whatever fk"

@app.route("/", methods = ["GET"])
def status():
    return "Your API is running"

if __name__ == "__main__":
    app.run()