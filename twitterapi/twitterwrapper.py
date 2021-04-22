import tweepy

from chatbook import settings


class Twitter:

    def __init__(self, api):
        self.api = api

    def tweet(self, data):
        return self.api.update_status(data)

    def listTweets(self, ids):
        return self.api.statuses_lookup(ids)

    @staticmethod
    def newInstane():
        auth = tweepy.OAuthHandler(settings.TWITER_API_KEY, settings.TWITER_API_SECRET_KEY)
        auth.set_access_token(settings.TWITER_ACCESS_TOKEN, settings.TWITER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except Exception as e:
            print("Error during authentication")
            raise e
        return Twitter(api)
