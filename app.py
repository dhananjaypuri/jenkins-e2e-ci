from flask import Flask

app = Flask(__name__);

@app.route('/')
def home():
    return "<h1>Welcome to first Jenkins CICD deployment</h1>";

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0');
