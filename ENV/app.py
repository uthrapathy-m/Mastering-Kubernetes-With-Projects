import os
from flask import Flask
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("ENVIRONMENT", "development")
    return f"✅ Running in {env} mode!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
