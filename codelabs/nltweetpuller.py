#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import json
import os

def pull():
    # Twitter API credentials
    currentPath = os.path.dirname(__file__)
    credentialsPath = 'credentials'
    file = 'twitter_credentials.json'
    with open(os.path.join(currentPath, credentialsPath, file)) as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']

    # Create the api endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    # mention to search for
    mention = "@sfmta_muni"

    # convert mention to parameters for query
    parameters = mention.replace(", ", " OR ")

    results = []

    for tweet_info in tweepy.Cursor(api.search, q=parameters,
                            tweet_mode='extended').items():
        results.append(tweet_info)
    
    print ('Extracted ' + str(len(results)) 
        + ' tweets with ' + mention)
    
    return results