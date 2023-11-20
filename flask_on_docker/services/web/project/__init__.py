from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("flask_on_docker.services.web.project.config.Config")

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    return jsonify(hello="world")


# @app.route("/static/<path:filename>")
# def staticfiles(filename):
#     # return send_from_directory(app.config["STATIC_FOLDER"], filename)
#     # 这个是无法生效的, 对于 /static 来说, 这个路由前缀对于 flask 来说有特殊的含义, 估计是内部已经有实现了
#     return jsonify(hello="world")

@app.route("/static-data/<path:filename>")
def staticfiles(filename):
    # return send_from_directory(app.config["STATIC_FOLDER"], filename)
    # 对于这个路由 /static-data 来说, 用户是可以自己控制的, 可以控制返回文件, 或者返回一个自定义的字符串都行
    return jsonify(hello=f"fn={filename}")
