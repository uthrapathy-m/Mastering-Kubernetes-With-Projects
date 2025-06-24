import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    db_user = os.getenv("DB_USER", "not set")
    db_pass = os.getenv("DB_PASS", "not set")
    return (
        f"🔐 Connected to DB as: {db_user}<br>"
        f"🔑 Password: {db_pass}"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
