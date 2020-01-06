from flask import Flask
from flask import request, json, redirect
import random
import redis
import re

app = Flask(__name__)
_redis = redis.Redis()


@app.route('/', methods=['POST'])
def encode():
    url = request.args['url']
    if not re.search('\w+\.\w+', url):
        return json.jsonify({'error': f'Была введена некорректная ссылка {url}'})
    else:
        if not _redis.exists(url):
            if not re.findall(r'https?://\w+\.\w+', url):
                url = 'https://' + url
            code = random.randint(100000, 999999)
            _redis.mset({url: code,
                         code: url})
        return json.jsonify({url: _redis.get(url).decode('utf-8')})


@app.route('/<int:code>', methods=['GET'])
def decode(code):
    if _redis.exists(code):
        url = _redis.get(code)
        return redirect(url, code=302)
    else:
        return json.jsonify({'error': f'{code} кода не существует в базе данных'})


if __name__ == '__main__':
    app.run()
