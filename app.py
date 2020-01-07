from flask import Flask
from flask import redirect, request
from core import encode, decode
import re

app = Flask(__name__)


@app.route('/url', methods=['POST'])
def web_encode():
    url = request.form.get('url')
    return encode(url)


@app.route('/<int:code>', methods=['GET'])
def web_decode(code):
    url = decode(code)
    if re.match('error', url):
        return url
    else:
        return redirect(url)


if __name__ == '__main__':
    app.run()
