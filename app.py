from core import encode, decode
from flask import redirect
import re


@app.route('/url/<url>', methods=['POST'])
def web_encode(url):
    return encode(url)


@app.route('/<int:code>', methods=['GET'])
def web_decode(code):
    url = decode(code)
    if re.match('error', url):
        return url
    else:
        return redirect(url)
