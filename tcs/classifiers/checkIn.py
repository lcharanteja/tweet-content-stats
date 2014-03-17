# -*- coding: utf8 -*-

def detect(tweet):
	"""
	This module searches url for url has any check in information.

	When it found any check in in url. It classifies tweet as
	"ci". 
			
	>>> detect({"mtd":{"urls":["http://4sq.com"] }})
	['ci']
	>>> detect({"mtd":{"urls":["http://4sq.com/basdajdb"] }})
	['ci']
	>>> detect({"mtd":{"urls":["http://blabla.bmp"] }})
	[]
	>>> detect({"mtd":{"urls":["http://blabla.unknown"] }})
	[]
	"""
	category = [] 	
	keywords = ["4sq", "foursquare"]

	try:
		for url in tweet["mtd"]["urls"]: 
			if any(keyword in url for keyword in keywords):
				category.append("ci")
			
	except:
		pass

	return category

