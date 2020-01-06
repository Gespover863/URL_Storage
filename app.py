# coding=utf-8

from flask import Flask
from flask import redirect
import random
import redis
import re

app = Flask(__name__)
_redis = redis.Redis()


def encode(url):
    if not re.search('\w+\.\w+', url):
        return 'error: This url is non-correct - %s' % url
    else:
        if not re.findall(r'https?://\w+\.\w+', url):
            url = 'https://' + url
        if not _redis.exists(url):
            code = random.randint(100000, 999999)
            _redis.mset({url: code,
                         code: url})
        else:
            code = _redis.get(url)
        return {'url': url.encode('utf-8'), 'code': str(code)}


def decode(code):
    if _redis.exists(code):
        url = _redis.get(code).decode('utf-8')
        return url
    else:
        return 'error: This code does not exist - %s' % code


@app.route('/url/<url>', methods=['POST'])
def web_encode(url):
    dict_result = encode(url)
    return dict_result


@app.route('/<int:code>', methods=['GET'])
def web_decode(code):
    string_result = decode(code)
    if re.match('error', string_result):
        return string_result
    else:
        return redirect(string_result)


def cli_interface(url_or_code, func):
    if func == 'encode':
        dict_result = encode(url_or_code)
        return dict_result
    elif func == 'decode':
        string_result = decode(url_or_code)
        return string_result
    else:
        return 'Something incredible just happened.'


if __name__ == '__main__':
    app.run()
