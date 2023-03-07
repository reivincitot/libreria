from flask import Flask, render_template, request

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
        print(request.form['usuario'])
        print(request.form['password'])
        return 'Ok'
    else:
        return render_template('auth/login.html')


def page_not_found(error):
    return render_template('/errores/404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
