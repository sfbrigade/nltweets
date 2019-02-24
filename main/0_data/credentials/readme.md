# Caution
This folder is for your personal API keys used by applications that query data from 3rd party services, like Twitter. You don't want these keys to be public, so any files you add to this folder in your local repo be sure to add to the .gitignore file in the root folder. That way when you push your code to GitHub, you'll upload all changes but not your credentials. So if you have a file holding your Twitter API keys named "twitter_credentials.json" that looks like this:

```
{
    "ACCESS_KEY": "1234567887654321",
    "ACCESS_SECRET": "abcdefghijk567898765lmnopqrstuvwxyz",
    "CONSUMER_KEY": "1P3S8V5M9R3S35BQ82GOR20"
    "CONSUMER_SECRET": "r3jd83jg73kdhvn83l29rpq73nc"
}
```

You'll add "twitter_credentials.json" inside your ".gitignore" file and it might look like this:

```
*ipynb_checkpoints*
twitter_credentials.json
```

Your code will be able to use your credentials when run on your local machine. Make sure the notebook uses a relative path if credentials file is stored in data folder. This snippet in ["tweets3.ipynb"](https://github.com/sfbrigade/nltweets/blob/master/twitter/tweet3.ipynb) demonstates how to use the credentials file:

```
/# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

/# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
```
