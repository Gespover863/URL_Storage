from redis import Redis  # , from_url
import random
import string
import urlparse
import re
import os

redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse('redis://localhost:6379/')

redis = Redis(host=url.hostname, port=url.port, db=0, password=url.password)


# redis = from_url(os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379/'))

def encode(url):
    if not re.search('\w+\.\w+', url):
        raise Exception('error: This url is non-correct - %s' % url)
    else:
        if not re.findall(r'https?://\w+\.\w+', url):
            url = 'https://' + url
        if not redis.exists(url):
            code = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            redis.mset({url: code,
                        code: url})
        else:
            code = redis.get(url)
        return str(code)


def decode(code):
    if redis.exists(code):
        url = redis.get(code).decode('utf-8')
        return url
    else:
        raise Exception('error: This code does not exist - %s' % code)
