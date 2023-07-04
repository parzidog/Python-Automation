from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur </p>"


@app.route("/api/v1/<in_cur>-<out_cur>")
def currency(in_cur, out_cur):
    return f"<h1>Getting {in_cur} and converting it to {out_cur}</h1>"


app.run()
