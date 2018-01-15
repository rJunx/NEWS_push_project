"""News Monitor"""
import hashlib
import redis
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import news_api_client
from cloudAMQP_client import CloudAMQPClient

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://phefaemd:C7R7_u62X2LJt0VHDLVJEYs8P6qFChbk@termite.rmq.cloudamqp.com/phefaemd"
SCRAPE_NEWS_TASK_QUEUE_NAME = "top-news-scrape-news-task-queue"

NEWS_SOURCES = "cnn"
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:
    # Connect with NEWS API
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    number_of_news = 0

    for news in news_list:
        news_diget = hashlib.md5(news['title'].encode('utf-8')).hexdigest()
        # Connect with Redis and check if it's in Redis
        if redis_client.get(news_digest) is None:
            number_of_news += 1
            # Deal with publishAt problems
            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            # Save into Redis
            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)
