import os
import sys
import json
import pickle
import redis
from bson.json_util import dumps



# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import mongodb_client
import news_recommendation_service_client

NEWS_TABLE_NAME = "news"
NEWS_LIST_BATCH_SIZE = 10
NEWS_LIMIT = 200
USER_NEWS_TIME_OUT_IN_SECONDS = 60


REDIS_HOST = "localhost"
REDIS_PORT = 6379

LOG_CLICKS_TASK_QUEUE_URL = "amqp://ckfbjqkn:1cpBY4LuQ-awS4kiW0a_wXbiEN8jpu9b@termite.rmq.cloudamqp.com/ckfbjqkn"
LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def getOneNews():
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))

def getNewsSummariesForUser(user_id, page_num):
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE

    sliced_news = []

    if redis_client.get(user_id) is not None:
        total_new_digests = pickle.loads(redis_client.get(user_id))
        sliced_news_digests = total_new_digests[begin_index:end_index]
        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest' : {'$in': sliced_news_digests}}))
    else:
        db = mongodb_client.get_db()
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))
        total_news_digest = [x['digest'] for x in total_news]
        redis_client.set(user_id, pickle.dumps(total_news_digest))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index:end_index]
    
    # Get preference for the user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'
            
    return json.loads(dumps(sliced_news))

def logNewsClickForUser(user_id, news_id):
    # Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    cloudAMQP_client.sendMessage(message);