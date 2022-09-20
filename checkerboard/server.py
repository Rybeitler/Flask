from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<int:num>")
@app.route("/<int:num1>/<int:num2>")
@app.route("/<int:num1>/<int:num2>/<string:color1>")
@app.route("/<int:num1>/<int:num2>/<string:color1>/<string:color2>")
def index(num1=8, num2=8, color1="black", color2="red"):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)


@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug = True)