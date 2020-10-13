from flask import *

app = Flask(__name__, template_folder="/home/voven4ek")


@app.route('/')
def redactor():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
