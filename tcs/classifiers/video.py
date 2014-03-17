# -*- coding: utf8 -*-

def detect(tweet):
	"""
	This module searches url for url has any video content.

	When it found any video content in url. It classifies tweet as
	"v". 
			
	>>> detect({"mtd":{"urls":["http://youtube.com"] }})
	['v']
	>>> detect({"mtd":{"urls":["http://dailymotion.com"] }})
	['v']
	>>> detect({"mtd":{"urls":["http://blabla.bmp"] }})
	[]
	>>> detect({"mtd":{"urls":["http://blabla.unknown"] }})
	[]
	"""
	category = [] 	
	keywords = ["youtube", "dailymotion", "facebook.com/photo.php?v=", "vimeo", "vine" ]

	try:
		for url in tweet["mtd"]["urls"]: 
			if any(keyword in url for keyword in keywords):
				category.append("v")
				break
	except:
		pass

	return category