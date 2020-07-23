from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/demo/test")
def test():
    return "ok from test"


@app.route("/_ah/warmup")
def warmup():
    return "OK"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
