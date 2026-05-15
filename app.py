from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Portfolio Analyzer</h1>
    <h2>מנתח החלטה למחר</h2>
    <p>המערכת פעילה</p>
    """
