import matplotlib.pyplot as plt
from matplotlib import cm
import csv
import numpy as np

from os import path
from wordcloud import WordCloud


#  PARAM
#  @account_link: link to scrape
#  RETURN VAL
#  +acc_info: [username, num_followers, num_following]
def getBasicData(account_link):
    acc_info = []
    return acc_info


#  PARAM
#  @account_link: link to instagram userpage
#  RETURN VAL
#  +return a dictionary which contains a jpg that maps to number of likes
def getMostPopularPosts(account_link):
    post_to_like = {}
    pass

#  PARAM
#  @account_link: link to instagram userpage
#  RETURN VAL
#  +return a dictionary which contains a jpg that maps to number of likes
def getBestFollowers(account_link):
    #maps top(10,20, 100)? users based on how many posts they've liked
    followers_to_likes = {}
    csvfile = open(account_link, 'r') 
    linereader = csv.reader(csvfile)
    numLines = 0
    labels = []
    sizes = []
    for row in linereader:
        labels.append(row[0])
        sizes.append(int(row[1].strip()))
        numLines += 1
    #a=np.random.random(40)
    colors=cm.Set1(np.arange(numLines)/float(numLines))
    explode = []
    explode.append(0.1)
    for x in range(0, numLines-1):
        explode.append(0)
 
    # Plot
    plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=0)
 
    plt.axis('equal')
 #   plt.show()

def word_cloud(file):
    d = path.dirname(__file__)

# Read the whole text.
    text = open(file, "r")
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
word_cloud("laugh-kookaburra.txt")

#getBestFollowers("testuserData.csv")

