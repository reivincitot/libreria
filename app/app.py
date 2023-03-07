from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ print(request.method)
        print(request.form['usuario'])
        print(request.form['password'])"""
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['password'] == '123456':
         # print(request.form['usuario'])
         # print(request.form['password'])
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')


def page_not_found(error):
    return render_template('/errores/404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
