'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
text = "hello hello there its me dana dana"
wordcloud = WordCloud().generate(text)

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("../Desktop/tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
print(len(tweetData))
print(list(tweetData[0].keys()))
#['created_at', 'favorite_count', 'hashtags', 'id', 'id_str', 'lang', 'retweet_count', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
favorite_count = 0

for i in range(0,len(tweetData)):
	if "favorite_count" in tweetData[i]:

		favorite_count += tweetData[i]['favorite_count']

		# like += likes int('favorite_count')
tweets = []
for t in range(0,len(tweetData)):
	if "text" in tweetData [t]:
		#print(tweetData[0]['text'])
		#tweets += tweetData[t]["text"]
		tweets.append(tweetData[t]["text"])
#print(tweets)
print(tweets[0])
Avg = favorite_count/len(tweetData)
print(Avg)

polaritylist = []
for item in tweets:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	polaritylist.append(polar1)
print(polaritylist)



text = []
polarity_list = [0.0,0.9]
leest = []
for i in range (0, len(tweetData)):
	dictionaree = {}
	dictionaree["id"] = tweetData[i]["id"]
	dictionaree['polarity'] = polaritylist[i]
	dictionaree['text'] = tweets[i]
	leest.append(dictionaree)

for i in range (0,len(tweetData)):
	text.append(tweetData[i]['text'])
	polarity_list.append(TextBlob(tweetData[i]['text']).polarity)

#giant_string = ""

tweetstring = ""
for tweet in tweets:
	tweet +=tweet + " "
	tweetstring += tweet
print(tweetstring)

wordcloud = WordCloud().generate(tweetstring)
plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
plt.savefig("alischart.png")

a_counter = 0
b_counter = 0

# We can close the file now that we have locally stored the data.
tweetFile.close()

#tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)

#..............

#import matplotlib.pyplot as plt:

#plt.bar([1,3,5,7,9],[5,2,7,8,2],)




# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
