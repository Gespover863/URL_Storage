# coding=utf-8

from flask import Flask
from flask import redirect, jsonify
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
        return [url, str(code)]


def decode_func(code):
    if _redis.exists(code):
        url = _redis.get(code)
        return [url.decode('utf-8'), '']
    else:
        return 'error: This code does not exist - %s' % code


@app.route('/url/<url>', methods=['POST'])
def web_encode(url):
    answer = encode(url)
    if isinstance(answer, str):
        return answer
    else:
        return jsonify(code=answer[1], url=answer[0])


@app.route('/<int:code>', methods=['GET'])
def web_decode(code):
    answer = decode_func(code)
    if isinstance(answer, str):
        return answer
    else:
        return redirect(answer[0].decode('utf-8'))


def cli_encode(url):
    answer = encode(url)
    if isinstance(answer, unicode):
        return answer
    else:
        return '%s %s' % (answer[0], answer[1])


def cli_decode(code):
    answer = decode_func(code)
    if isinstance(answer, unicode):
        return answer
    else:
        return '%s %s' % (answer[0], answer[1])


if __name__ == '__main__':
    app.run()
