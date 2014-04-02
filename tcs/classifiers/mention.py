# -*- coding: utf8 -*-



def detect(tweet):
	"""
	This module searches tweets content for mention.

	If tweet text has any  "@" and don't have any url information which has foursquare 
	or 4sq if classifies message as mentin and return "m" as an array

	
	>>> detect({"text":"@person bla bla bla" })
	['m']
	>>> detect({"text":"empty empty empty" })
	[]
	>>> detect({"text":" I'm at @4sqcafe" ,"mtd":{"urls":["http://4sq.com"] }})
	[]
	>>> detect({"text":" I am a person like @haciBiBak" })
	['m']
	"""
	keywords = ["4sq","foursquare"]
	category = []	
	if "@" in tweet["text"]:
		try:
			for url in tweet["mtd"]["urls"]: 
				if any(keyword in url for keyword in keywords):
					pass	
		except:
			category.append("m")

	return category
