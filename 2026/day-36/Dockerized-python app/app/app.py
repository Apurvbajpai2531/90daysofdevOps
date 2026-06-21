from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

db = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

cache = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    visits = cache.incr("counter")
    return f"🚀 Dockerized Python Backend | Visits: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

