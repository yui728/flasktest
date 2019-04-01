from flask import Flask, render_template  # Flaskモジュールのインポート

app = Flask(__name__)  # Flaskアプリのインスタンス作成


@app.route("/")  # URLのパス
def hellow_world():
    return "Hellow World!"


@app.route("/ja")
def hellow_world_ja():
    return "こんにちは 世界！"


@app.route("/about")
def about():
    return "<h1>About:</h1>"


@app.route("/hello/<whom>")
def hello(whom):
    return render_template("hello.html", whom=whom)


@app.route("/100_plus/<int:n>")
def adder(n):
    return f"100+{n}={100+n}"


if __name__ == "__main__":
    app.run()
