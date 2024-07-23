from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response

    return render_template('form.html', title='Форма отправки', header='Введите Имя и адрес электронной почты')


@app.route('/welcome')
def welcome():
    username = request.cookies.get('username', 'Гость')
    return render_template('welcome.html', username=username, title='Ваши данные получены',
                           header='Привет, ' + username)


@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)