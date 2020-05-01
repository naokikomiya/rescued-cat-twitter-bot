# %%
from requests_oauthlib import OAuth1Session
import json

from config import settings


def tweet_search(search_word):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "15"
    }

    oath = OAuth1Session(settings.CONSUMER_KEY,
                         settings.CONSUMER_SECRET,
                         settings.ACCESS_TOKEN,
                         settings.ACCESS_TOKEN_SECRET)

    responce = oath.get(url, params=params)
    if responce.status_code != 200:
        print("Error code: %d" % (responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

# Functions


def main():
    tweets = tweet_search("#python")
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        print("tweet_id:", tweet_id)
        print("text:", text)
        print("created_at:", created_at)
        print("user_id:", user_id)
        print("user_desc:", user_description)
        print("screen_name:", screen_name)
        print("user_name:", user_name)
    return


# Execute
if __name__ == "__main__":
    main()


# %%
