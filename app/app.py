from flask import Flask
import os

app = Flask(__name__)

ENV = os.getenv("ENV", "dev")

@app.route("/")
def home():
    return f"DevSecOps Pipeline Running - {ENV.upper()} Environment"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
