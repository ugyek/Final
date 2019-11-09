from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)


