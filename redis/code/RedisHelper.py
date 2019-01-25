"""

This module encapsulates the operation of the redis, very convenient
please open redis-server
sudo redis-server /usr/local/redis-5.0.3/redis.conf

"""

from redis import *

class RedisHelper(object):
    def __init__(self, host='localhost', port=6379):
        self.redis = StrictRedis(host, port)

    '''set key value'''
    def set(self, key, value):
        self.redis.set(key, value)

    '''get key'''
    def get(self, key):
        return self.redis.get(key)

    def exists(self, key):
        return self.redis.exists(key)