from flask import Flask
import hashlib

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <p>This is my heroku web, dont try to hack it!</p>
    """
@app.route("/name/<name>")
def hello_there(name: str = "General Kenobi"):
    return f"<p>Hello there, {name}!</p>"

@app.route("/ksi/<challenge>")
def ksi_challenge(challenge: str):
    # This function is here to allow you to get a trophy!
    return hashlib.sha256(f"{challenge}-KSI".encode("utf8")).hexdigest()


if __name__ == '__main__':
    app.run(threaded=True, port=443)
