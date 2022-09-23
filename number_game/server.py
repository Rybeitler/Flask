from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1, 100)
    print(session)
    return render_template("index.html")

@app.route("/guess", methods = ["POST"] )
def guess():
    print(request.form)
    if int(request.form['guess']) > int(session['rand_num']):
        session['result'] = "Too high!"
        
    elif int(request.form['guess']) < int(session['rand_num']):
        session['result'] = "Too low!"
        
    elif int(request.form['guess']) == int(session['rand_num']):
        session['result'] = "Correct!"
    else:
        print("broken")
    if "counter" in session:
        temp = session["counter"]
        temp +=1
        session["counter"] = temp 
    else:
        session["counter"] = 1
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)