# -*- coding: utf-8 -*-
from classifiers import *

def getStats(tweets):
	counter = {
		"image":0,
		"video":0,
		"link":0,
		"checkIn":0,
		"favorited":0,
		"retweeted":0
		}

	for tweet in tweets:
		if image.detect(tweet):
			counter["image"] += 1
		if video.detect(tweet):
			counter["video"] += 1
			#print tweet["mtd"]
		if link.detect(tweet):
			counter["link"] += 1
		if checkIn.detect(tweet):
			counter["checkIn"] += 1
		if favorite.detect(tweet):
			counter["favorited"] += 1
		if retweet.detect(tweet):
			counter["retweeted"] += 1
	
	return counter
