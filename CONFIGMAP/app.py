import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    first = os.getenv("FIRST_NAME", "Unknown")
    last = os.getenv("LAST_NAME", "Unknown")
    db_url = os.getenv("DATABASE_URL", "Not Set")
    return (
        f"👋 Hello, {first} {last}!<br>"
        f"🔗 Connected to database: {db_url}"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
