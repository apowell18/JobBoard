from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/login")
def login():
    return "<h1>login Page</h1>"

@app.route("/signup")
def signUp():
    return "<h1>signup Page</h1>"

@app.route("/createBoard")
def createBoard():
    return "<h1>Create Job Board Page</h1>"

@app.route("/")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
