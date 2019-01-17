import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "<h1>This is Restful API Test</h1>" # 相应的body


if __name__ == "__main__":
    app.run(port=8080)