from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = "so_secret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0

    return render_template('index.html')

@app.route('/process-money', methods=['POST'])
def process_money():
    print(request.form)

    if request.form['option'] == 'farm':
        num = random.randint(10,20)
        session['gold'] += num
    elif request.form['option'] == 'cave':
        num = random.randint(5,10)
        session['gold'] += num
    elif request.form['option'] == 'house':
        num = random.randint(2,5)
        session['gold'] += num
    elif request.form['option'] == 'casino':
        num = random.randint(-50,50)
        session['gold'] += num
    
    if 'log' not in session:
        session['log'] = []
    
    if num >= 0:
        session['log'].append(f"<li class='green'>Earned {num} gold from the {request.form['option']}</li>")
    else:
        session['log'].append(f"<li class='red'>Lost {abs(num)} gold at the {request.form['option']}</li>")
    print(session)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, )
