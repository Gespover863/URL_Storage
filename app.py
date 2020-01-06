from flask import Flask
from flask import request, json, redirect
import redis
import re

app = Flask(__name__)
_redis = redis.Redis()


@app.route('/url', methods=['GET', 'POST'])
def url_to_hash():
    url = request.args['url']
    if not re.search('\w+\.\w+', url):
        return json.jsonify({'Была введена некорректная ссылка': url})
    else:
        if not _redis.exists(url):
            if not re.findall(r'https?://\w+\.\w+', url):
                url = 'https://' + url
            code = hash(url)
            _redis.set(url, code)
            _redis.set(code, url)
        return json.jsonify({url: _redis.get(url).decode('utf-8')})


@app.route('/code', methods=['GET', 'POST'])
def to_website():
    if _redis.exists(request.args['code']):
        url = _redis.get(request.args['code']).decode('utf-8')
        return redirect(url, code=302)
    else:
        return json.jsonify({'Данного кода не существует в базе данных': request.args['code']})


if __name__ == '__main__':
    app.run()
