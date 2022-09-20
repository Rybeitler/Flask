from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<string:color>")
def index(num=3, color="skyblue"):
    return render_template("index.html", num=num, color=color)


@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug = True)