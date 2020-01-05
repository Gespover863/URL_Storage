from flask import Flask
from flask import request, json, redirect, url_for
import redis
import re

app = Flask(__name__)
r = redis.Redis()


@app.route('/url', methods=['GET', 'POST'])
def url_to_hash():
    url = request.args['url']
    if r.exists(url) == 0:
        code = hash(url)
        r.set(url, code)
        r.set(code, url)
    return json.jsonify({url: r.get(url).decode('utf-8')})


@app.route('/code', methods=['GET', 'POST'])
def to_website():
    url = r.get(request.args['code']).decode('utf-8')
    if re.findall(r'https://\w+.\w+', url) == []:
        url = 'https://' + url
    return redirect(url, code=302)


if __name__ == '__main__':
    app.run()