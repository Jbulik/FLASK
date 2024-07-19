from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/next')
def next_page():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)

