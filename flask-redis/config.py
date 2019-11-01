import redis
from redis.sentinel import Sentinel


def init_redis():
    sentinel_list = [("127.0.0.1",26379),("127.0.0.1",26380),("127.0.0.1",23681)]
    sentinel = Sentinel(sentinel_list,socket_timeout=0.5)

    master = sentinel.discover_master("mymaster")
    print(master)

    slave = sentinel.discover_slaves("mymaster")
    print(slave)

    redis_conn = sentinel.master_for('mymaster', socket_timeout=0.5)
    return redis_conn
