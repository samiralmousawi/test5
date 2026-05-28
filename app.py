from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Returned msg"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
