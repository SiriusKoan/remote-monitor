import os
import redis


class Redis:
    def __init__(self):
        # when no flask
        self.host = os.getenv("REDIS_HOST", "localhost")
        self.port = os.getenv("REDIS_PORT", 6379)
        self.client = redis.Redis(host=self.host, port=self.port, db=0)

    def init_app(self, app):
        self.host = app.config.get("REDIS_HOST", "localhost")
        self.port = app.config.get("REDIS_PORT", 6379)
        self.client = redis.Redis(host=self.host, port=self.port, db=0)

    def set(self, host, func, value):
        self.client.hset(host, func, value)

    def get(self, host, func):
        return self.client.hget(host, func)


r = Redis()


def get_record(host, func):
    res = r.get(host, func)
    return res if res else ""


def set_record(host, func, value):
    r.set(host, func, value)
