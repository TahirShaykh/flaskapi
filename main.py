from flask import Flask


app = Flask(__name__)

@app.route("/joke", methods = ["GET"])
def givejoke():
    return "knock knock.. who is there!"

@app.route("/", methods = ["GET"])
def status():
    return "Your API is running hooray!!!"

if __name__ == "__main__":
    app.run()
