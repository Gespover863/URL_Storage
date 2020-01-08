from flask import Flask
from flask import redirect, request
from core import encode, decode

app = Flask(__name__)


@app.route('/url', methods=['POST'])
def web_encode():
    url = request.form.get('url')
    try:
        data = encode(url).split(' - ')
        return {
            'url': data[0],
            'code': data[1]
        }
    except Exception as error:
        return str(error)


@app.route('/<string:code>', methods=['GET'])
def web_decode(code):
    try:
        url = decode(code)
        return redirect(url)
    except Exception as error:
        return str(error)


if __name__ == '__main__':
    app.run()
