from tcs import tcs

tweet = {
   "text": "RT @TwiterSonDakika: Polis Ankara'da olagan ustu hal ilan eti.Onlarca yarali. Bu da Ankara'da Cebeci Kampusu girisi http:\/\/t.co\/zQLn81xJgk",
   "retweeted_status": {
     "entryId": "443779513429032960",
     "retweet_count": "25",
     "favorite_count": "4",
     "user": "TwiterSonDakika" 
  },
  "mtd": {
    "media": {
      "url": "http:\/\/pbs.twimg.com\/media\/BiiVfRXCUAAyofD.jpg",
      "type": "photo" 
      }
  },
  "st": {
     "ln": 0,
     "lc": 0,
     "pl": 1,
     "ct": 0
  }
}

c = tcs.Classifier()
print c.classfy(tweet)
print c.classfy(tweet)
print c.getStats()

