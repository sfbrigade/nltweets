#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json
import pandas as pd
import os

# Parameter should be formatted with @mention or #mention. Multiple parameters should be split with commas
def pull(mention):
    # Twitter API credentials
    credentialsPath = r'..\0_data\credentials'
    with open(os.path.join(credentialsPath, 'twitter_credentials.json')) as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']

    # Create the api endpoint

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    # paramaters to search for
    parameters = mention.replace(", ", " OR ")

    results = []

    for tweet_info in tweepy.Cursor(api.search, q=parameters,
                            tweet_mode='extended'):
        results.append(tweet_info)

    dataframe = toDataFrame(results)

    outputPath = r'..\0_data\manual'
    filePath = os.path.join(outputPath,'tweets_with_' + 'mention_' + mention + '.csv')
    if not os.path.isfile(filePath):
        dataframe.to_csv(filePath, index=False)
    else:
        with open(filePath, 'a') as file:
            dataframe.to_csv(file, index = False)
    print ('Extracted ' + str(len(results)) 
        + ' tweets with ' + mention)


# Convert to data frame
def toDataFrame(tweets):
    DataSet = pd.DataFrame()
    
    # Get tweet information
    tweetIDs = []
    for tweet in tweets:
        tweetIDs.append(tweet.id)              
    DataSet['Tweet ID'] = [ID for ID in tweetIDs]
        
    tweetsText = []
    for tweet in tweets:
            if 'retweeted_status' in  dir(tweet):
                tweetsText.append(tweet.retweeted_status.full_text.encode('utf-8'))                
            else:
                tweetsText.append(tweet.full_text.encode('utf-8'))  
    DataSet['Text'] = [text for text in tweetsText]
    
    # Get user information
    DataSet['User'] = [tweet.user.name.encode('utf-8') for tweet in tweets]
    
    DataSet['User ID'] = [tweet.user.id for tweet in tweets]
    
    # Get media
    tweetsImages = []
    for tweet in tweets:
        if 'media' in tweet.entities:
            for image in tweet.entities['media']:
                tweetsImages.append(image['media_url'])
        else:
            tweetsImages.append('')  
    DataSet['Image Urls'] = [image for image in tweetsImages]
          
    # Get location    
    tweetsLongitudes = []
    for tweet in tweets:
        if tweet.coordinates is not None:
            tweetsLongitudes.append(tweet.coordinates["coordinates"][0])
        else:
            tweetsLongitudes.append('')
    DataSet['Longitude'] = [longitude for longitude in tweetsLongitudes]
    
    tweetsLatitudes = []
    for tweet in tweets:
        if tweet.coordinates is not None:
            tweetsLatitudes.append(tweet.coordinates["coordinates"][1])
        else:
            tweetsLatitudes.append('')
    DataSet['Latitude'] = [latitude for latitude in tweetsLatitudes]
    
    tweetLocations = []
    for tweet in tweets:
        if tweet.user.location is not None:
            tweetLocations.append(tweet.user.location.encode('utf-8'))
        else:
            tweetLocations.append('')            
    DataSet['Location'] = [loc for loc in tweetLocations]
    
    # Get other fields  
    tweetsPosted = []
    for tweet in tweets:
        tweetsPosted.append(tweet.created_at)
    DataSet['Created'] = [created for created in tweetsPosted]
    
    return DataSet