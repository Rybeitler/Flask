from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/success")
def success():
    return "success"

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return f"hello {name * num}"

@app.route('/users/<username>/<id>')
def show_user(username, id):
    print(username)
    print(id)
    return f"Username: {username} || ID: {id}"

if __name__ == "__main__":
    app.run(debug = True)
