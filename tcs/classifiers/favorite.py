# -*- coding: utf8 -*-



def detect(tweet):
	"""
	This module checks tweet statuses. If tweet has any favorite, 
	it classifies tweet as "f". 
			
	>>> detect({"retweeted_status":{"favorite_count":"12" }})
	['f']
	>>> detect({"retweeted_status":{"favorite_count":"1" }})
	['f']
	>>> detect({"retweeted_status":{"favorite_count":None}})
	[]
	>>> detect({"mtd":{"urls":[] }})
	[]
	"""
	category = []
	try:
		if tweet["retweeted_status"]["favorite_count"] != None:
			category.append("f")

	except:
		pass
	return category

