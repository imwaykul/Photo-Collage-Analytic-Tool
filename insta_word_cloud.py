import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import codecs 
import matplotlib.pyplot as plt
#%matplotlib inline

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10 
mpl.rcParams['savefig.dpi']=100             #72 
mpl.rcParams['figure.subplot.bottom']=.1 


def getWords(file):
    fileOpen = codecs.open(file, 'r')
    words = []
    for line in fileOpen.readlines():
        space_limited = line.split(" ")
        for items in space_limited:
            items = items.lower()
            words.append(items)
    return words
    

datum= getWords("laugh-kookaburra.txt")
##
wordcloud = WordCloud(
                          background_color='white',
                          stopwords=datum,
                         max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(str(datum))

#print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
##fig.savefig("insta_prep_wordcloud.png", dpi=900)


    
