from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template('index.html')

@app.route('/increment', methods=["POST"])
def increment():
    if "counter" in session:
        temp = session["counter"]
        temp +=2
        session["counter"] = temp 
    else:
        session["counter"] = 2
    return redirect('/')

@app.route('/clear-session')
def clear_session():
    session.clear()
    return redirect("/")

@app.route('/increment-by', methods=["POST"])
def increment_by():
    print(request.form)
    if "counter" in session:
        temp = session["counter"]
        temp += int(request.form['num'])
        session["counter"] = temp 
    else:
        session["counter"] = int(request.form['num'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)