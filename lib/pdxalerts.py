import httplib, urllib, urllib2, base64, requests, json, datetime, time


class PdxAlerts:

    def __init__(self, start_date = None, token = None, channel = "#portland"):
        self.tweets = []
        self.new_tweets = []
        self.latest_tweet_date = start_date
        self.channel = channel
        self.token = token
        self.bearer_token = None
        self.token_url = 'https://api.twitter.com/oauth2/token'
        self.username = "pdxalerts"
        self.twitter_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=10&screen_name='
    
    def run(self):
        time.sleep(10)
        while True:
            self.tweets = self.build_tweets(self.get_alerts())

            if self.latest_tweet_date is None:
                self.latest_tweet_date = self.tweets[0].date

            for item in self.tweets:
                if (item['date'] > self.latest_tweet_date):
                    self.new_tweets.append(item)
            
            if self.new_tweets:
                self.latest_tweet_date = self.new_tweets[0]['date']

            time.sleep(60)

    def get_bearer_token(self):
        send_token = base64.b64encode(self.token)
        url = self.token_url
        headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Authorization": 'Basic ' + send_token}
        params = urllib.urlencode({'grant_type':'client_credentials'})
        r = requests.post(url, data=params, headers=headers)
        return r.json()

    def get_alerts(self):
        url = self.twitter_url + self.username
        if self.bearer_token is None:
            self.bearer_token = self.get_bearer_token()['access_token']
        headers = {"Authorization": 'Bearer ' + self.bearer_token}
        r = requests.get(url, headers=headers)
        return r.json()

    def build_tweets(self, response):
        tweets = [];
        format = '%a %b %d %H:%M:%S +0000 %Y'
        for item in response:
            tweet = {'id': item['id'], 'text': item['text'], 'date': datetime.datetime.strptime(item['created_at'], format), 'url': 'https://twitter.com/pdxalerts/status/{}'.format(item['id'])}
            tweets.append(tweet)
        return tweets
