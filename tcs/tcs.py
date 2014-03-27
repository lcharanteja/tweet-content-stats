# -*- coding: utf-8 -*-
from classifiers import *

class Classifier(object):
	"""tweet content classifier"""
	def __init__(self):
		super(Classifier, self).__init__()
		self.reset()
	
	counter = []

	def classify(self, tweet):
		tweetClass = []

		dedectorNames = [
			'image',
			'video',
			'link',
			'checkIn',
			'favorite',
			'retweet'
		]
		
		for detectorName in dedectorNames:
			detector = globals()[detectorName]
			classes = detector.detect(tweet)
			tweetClass.extend(classes)
			if len(classes) > 0:
				self.counter[detectorName] += 1
		
		tweet["ct"] = tweetClass

		# bein marked as classified
		tweet["st"]["ct"] = 1

		return tweet

	def getStats(self):
		return self.counter

	def reset(self):
		self.counter = {
			"image":0,
			"video":0,
			"link":0,
			"checkIn":0,
			"favorite":0,
			"retweet":0
		}

