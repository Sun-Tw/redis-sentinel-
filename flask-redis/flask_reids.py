import redis
from flask import Flask
from config import init_redis

redis_conn = None
redis_conn = init_redis()

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    global redis_conn
    try:
        result = redis_conn.set("foo","bar")
        print("set",result)
    except redis.exceptions.ConnectionError:
        redis_conn = init_redis()
        return "redis runerr"
    return 'Hello World!'

@app.route("/get")
def get_redis():
    global redis_conn
    try:
        result = redis_conn.get("foo")
    except redis.exceptions.ConnectionError:
        redis_conn = init_redis()
        return "redis runerr"
    return str(result)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9000)

