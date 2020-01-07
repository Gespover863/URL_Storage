from flask import Flask
import random
from redis import Redis
import re

app = Flask(__name__)
redis = Redis()


def encode(url):
    if not re.search('\w+\.\w+', url):
        return 'error: This url is non-correct - %s' % url
    else:
        if not re.findall(r'https?://\w+\.\w+', url):
            url = 'https://' + url
        if not redis.exists(url):
            code = random.randint(100000, 999999)
            redis.mset({url: code,
                        code: url})
        else:
            code = redis.get(url)
        return {'url': url.encode('utf-8'), 'code': str(code)}


def decode(code):
    if redis.exists(code):
        url = redis.get(code).decode('utf-8')
        return url
    else:
        return 'error: This code does not exist - %s' % code


if __name__ == '__main__':
    app.run()
