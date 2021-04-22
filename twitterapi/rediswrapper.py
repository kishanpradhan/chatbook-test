import time

import redis

from chatbook.settings import REDIS_HOST, REDIS_PORT


rClient = redis.Redis(REDIS_HOST, REDIS_PORT)


def _generate_key(user):
    current_time = int(time.time() * 1000)
    return f"{user}_{current_time}"

def save_tweet(user_id, tweet_id):
    rClient.set(_generate_key(user_id), tweet_id)

def get_latest_tweets(user_id, n = 10):
    keys = rClient.keys(f"{user_id}*")
    keys.sort(reverse=True)
    ids = rClient.mget(keys[:n])
    return [str(id, 'utf-8') for id in ids]
