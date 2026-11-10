from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Cloud Computing!</h1>
    <h2>Python Flask Application</h2>
    <p>My application is running successfully.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)