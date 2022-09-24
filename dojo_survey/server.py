from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def collect_data():
    print(request.form)
    session["data"] = request.form
    print(session["data"])
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)