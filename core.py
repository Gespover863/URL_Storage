from redis import from_url
import random
import string
import re
import os

redis = from_url(os.environ.get('redis://localhost:6379'))

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
