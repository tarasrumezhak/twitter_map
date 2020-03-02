import tweepy


def get_friends_locations(username):
    auth = tweepy.OAuthHandler("0PlKlKMbNYWL9UeVuC6DPxX4B",
                               "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN")
    auth.set_access_token("963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC",
                          "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R")

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        user = api.get_user(username)
    except:
        return None
    friends_locs = {}

    for friend in user.friends():
        friends_locs[friend.screen_name] = friend.location

    return friends_locs

# print(get_friends_locations("gehebhbg"))