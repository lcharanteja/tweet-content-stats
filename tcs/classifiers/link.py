# -*- coding: utf8 -*-


def detect(tweet):
	"""
	This module checks tweet content for url. If tweet has any url, 
	it classifies tweet as "l". 
			
	>>> detect({"mtd":{"urls":["http://youtube.com"] }})
	['l']
	>>> detect({"mtd":{"urls":["http://dailymotion.com"] }})
	['l']
	>>> detect({"mtd":{"urls":["http://blabla.bmp"] }})
	['l']
	>>> detect({"mtd":{"urls":[] }})
	[]
	"""
	category = [] 	
	
	try:
		if len(tweet["mtd"]["urls"]) != 0:
			category.append("l")
	except:
		pass

	return category


