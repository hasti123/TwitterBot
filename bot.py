#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py

# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Housekeeping: do not edit
import tweepy
import time
import operator
from tweetService import *
from stopWordService import *


# initially, the script will assume that the last tweet was a null value
lasttweet = None

# this is the function that does most of the work of the bot
def runBot():

    global lasttweet

    #mostrecenttweet = api.user_timeline('BernieSanders')[0]
    tweetHashMap = {}
    result = []
    flattenedResult = []

    for i in range(20):
        result.append(api.user_timeline('BernieSanders')[i].text)

    for tweet in result:
        tweet = re.sub('[^a-zA-Z0-9 \n\.]', '', tweet)
        flattenedResult += tweet.split()

    noStopWords = removeStopWords(flattenedResult)

    for word in noStopWords:
        if word in tweetHashMap: 
            tweetHashMap[word] += 1
        else:
            tweetHashMap[word] = 1

    sorted_tweetHashMap = sorted(tweetHashMap.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_tweetHashMap[:20]

runBot()