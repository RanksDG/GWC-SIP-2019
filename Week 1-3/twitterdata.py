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
tweetFile = open("twitterdata.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
tweetFile.close()
# print(len(tweetData))
# print(list(tweetData[0].keys()))
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
# print(tweets[0])
Avg = favorite_count/len(tweetData)
# print(Avg)

polaritylist = []
for item in tweets:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	polaritylist.append(polar1)
# print(polaritylist)



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

# print(polarity_list)
# print(min(polarity_list))
# print(max(polarity_list))
#n,bins,patches = plt.hist(polarity_list)
# plt.axis([-0.55,1.05,0,50])

#giant_string = ""

tweetstring = ""
for tweet in tweets:
	tweet +=tweet + " "
	tweetstring += tweet
# print(tweetstring)

wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
# plt.figure(figsize = (10, 10), facecolor = None)
# plt.imshow(wordcloud, interpolation = "bilinear")
# plt.axis("off")
# plt.show()
#plt.savefig("alischart.png")

a_counter = 0
b_counter = 0



def countletter(string,letter):
	counter = 0
	for let in string:
		if let.lower()== letter:
			counter += 1
	return counter

# alefbet = sorted('qwertyuiopasdfghjklzxcvbnm')
# occurences = []
# for i in alefbet:
# 	occurences.append(countletter(tweetstring,i))
# 	print(f'letter: {i} occurences: {countletter(tweetstring, i)}')
# print(occurences)
# We can close the file now that we have locally stored the data.
def wordcount(tweetString,string1):
	counter = 0
	string1 = string1.lower()
	wordList = tweetString.split(" ")
	for i in wordList:
		if i == string1:
			counter += 1
	return counter

wordCountList = []
for item in tweets:
	wordoccurence = wordcount(item,"the")
	wordCountList.append(wordoccurence)
print(wordCountList)
print(len(wordCountList))

print(wordCountList)
print(min(wordCountList))
print(max(wordCountList))
n,bins,patches = plt.hist(wordCountList)
plt.axis([-1,4,0,90])
plt.grid(True)
plt.show()

#tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)

#..............

#import matplotlib.pyplot as plt:

#plt.bar([1,3,5,7,9],[5,2,7,8,2],)

# n, bins, patches = plt.hist(polarity_list, 50, normed=1, facecolor='g', alpha=0.75)


# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()


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
