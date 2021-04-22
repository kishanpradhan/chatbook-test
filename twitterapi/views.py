from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from twitterapi.twitterwrapper import Twitter
from twitterapi import rediswrapper as cache



class TwitterViewSet(ViewSet):
    twitter = Twitter.newInstane()
    user_id = "user" # Get this from auth # 231747189

    def list(self, request):
        # 1384829201539338244, 1385180498201255936
        ids = cache.get_latest_tweets(self.user_id)
        data = []
        if (len(ids) > 0):
            tweets = self.twitter.listTweets(ids)
            for tweet in tweets:
                data.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "user": {
                        "id": tweet.user.id,
                        "name": tweet.user.name
                    }
                })

        return Response(data)
    
    def create(self, request):
        is_valid, msg = self._validate(request.data)
        
        if not is_valid:
            return Response({ 'msg': msg }, status=status.HTTP_400_BAD_REQUEST)

        response = self.twitter.tweet(request.data["text"])
        tweet_id =response.id
        
        cache.save_tweet(self.user_id, tweet_id)

        # data = {"id": tweet_id, "text": request.data["text"]}
        data = {"id": tweet_id, "text": response.text}
        return Response(data)

    def _validate(self, data):
        if 'text' not in data:
            return (False, "Request does not contain key 'text'")
        
        return (True, None)

