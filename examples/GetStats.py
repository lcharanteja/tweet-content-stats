# -*- coding: utf8 -*-
import tsc

def main():
	conn = MongoClient()
	db = conn["test"]
	tweets = db.tweets.find()
	stats = tsc.getStats(tweets)
	print stats

if __name__ == "__main__":
	main()
