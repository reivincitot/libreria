from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'titulo': 'index',
    }
    return render_template('index.html', data=data)

# @app.errorhandler(404)


def page_not_found(error):
    return render_template('/errores/404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
