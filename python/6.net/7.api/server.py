import flask
from infos import info_list

app = flask.Flask(__name__)


# Json的404自定义处理
@app.errorhandler(404)
def not_found(error):
    return flask.make_response(
        flask.jsonify({
            "data": "Not Found",
            "status": 404
        }), 404)


# 运行Get和Post请求
@app.route("/api/v1.0/servers/<name>", methods=["GET", "POST"])
def get_info(name):
    infos = list(filter(lambda item: item["name"] == name, info_list))
    if len(infos) == 0:
        flask.abort(404)
    # 基于json.dumps的封装版
    return flask.jsonify({"infos": infos})  # 返回Json字符串


if __name__ == "__main__":
    app.run(port=8080)
