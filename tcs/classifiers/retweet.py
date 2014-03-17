# -*- coding: utf8 -*-

def detect(tweet):
	"""
	This module checks tweet statuses. If tweet has any retweeted, 
	it classifies tweet as "rt". 
			
	>>> detect({"retweeted_status":{"retweet_count":"12" }})
	['rt']
	>>> detect({"retweeted_status":{"retweet_count":"1" }})
	['rt']
	>>> detect({"retweeted_status":{"retweet_count":None}})
	[]
	>>> detect({"mtd":{"urls":[] }})
	[]
	"""
	category = []
	try:
		if tweet["retweeted_status"]["retweet_count"] != None:
			category.append("rt")

	except:
		pass
	return category

