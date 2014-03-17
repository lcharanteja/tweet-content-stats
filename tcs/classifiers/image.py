# -*- coding: utf8 -*-



def detect(tweet):
	"""
	This module searches tweets content for image files.

	Firstly it looks ("mtd"."media"."type") path. When it found an image 
	in media object, it classifies tweet as "i" (image) in category.

	If it didn't find any media content. It goes to ("mtd"."urls") path.
	And it scans url information for check is it image url?. If it found an image 
	format in url, it classifies tweet as "i" (image) in category 
	
	>>> detect({"mtd":{"media":{"type":"photo"} }})
	['i']
	>>> detect({"mtd":{"media":{"type":"notphoto"} }})
	[]
	>>> detect({"mtd":{"urls":["http://blabla.jpg"] }})
	['i']
	>>> detect({"mtd":{"urls":["http://blabla.png"] }})
	['i']
	>>> detect({"mtd":{"urls":["http://blabla.bmp"] }})
	['i']
	>>> detect({"mtd":{"urls":["http://blabla.unknown"] }})
	[]
	"""
	category = [] 	
	

	try:
		if  tweet["mtd"]["media"]["type"] == "photo":
			category.append("i")
	except:
		pass

	try:
		if len(category) == 0:
			for url in tweet["mtd"]["urls"]: 
				if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png')  or url.endswith('.bmp'):
					category.append("i")
					break
	except:
		pass

	return category








