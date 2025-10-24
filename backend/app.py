from flask import Flask, render_template
from routes.crypto_routes import crypto_bp
from dotenv import load_dotenv
import os

load_dotenv()   #Load env variables from .env

app = Flask(__name__)
app.register_blueprint(crypto_bp, url_prefix="/api/crypto")

@app.route("/")
def home():
    # HTML page with buttons that link to your API routes
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)