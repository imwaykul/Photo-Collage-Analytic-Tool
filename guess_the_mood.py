import codecs
from importlib import reload
from collections import defaultdict
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8') 

#reload(sys)  
#sys.setdefaultencoding('utf8')

#n-gram
def mood_to_phrase(file, n):
    mood_to_sent_count = defaultdict(float)
    most_common_words_happy = defaultdict(lambda:1.6)
    most_common_words_sad = defaultdict(lambda:1.6)
    openFile = open(file, "r", encoding="utf-8")
    readlines = openFile.readlines()
    print(len(readlines))
    for line in readlines:
        mood_sentence = line.split(":")
        mood = mood_sentence[0]
        sentence = mood_sentence[1].split(" ")
        sentence.insert(0, "SENT-HEAD")
        sentence[len(sentence)-1] = sentence[len(sentence)-1].strip("\n")
        sentence.append("SENT-TAIL")
        index = 0
        sentLen = len(sentence)
        while(sentence[index] != "SENT-TAIL"):
            bigram = (mood.upper(), sentence[index].lower(), sentence[index+1].lower())
            if (mood.lower() == "happy" and sentence[index] != "SENT-HEAD" ):
                most_common_words_happy[sentence[index].lower()] += 1
            if (mood.lower() == "sad" and sentence[index] != "SENT-HEAD"):
                most_common_words_sad[sentence[index].lower()] += 1
            mood_to_sent_count[bigram] += 1
            index = index + 1
    return mood_to_sent_count, most_common_words_happy, most_common_words_sad
            
            
def normalize_dict(m_to_s):
    norm_dict = defaultdict(float)
    copy_dict = m_to_s.copy()
    #mood = ["HAPPY", "SAD"]
    for key, value in m_to_s.items():
        #print("CURRLEN: m_to_s.items: ", len(m_to_s.items()))
        opp = getOpposite(key[0])
        newBigram = (opp, key[1], key[2])
        nVal = copy_dict[newBigram]
        total = nVal + value
        norm_dict[key] = value/total
        if (nVal == 0):
            nVal = 0.25
        norm_dict[newBigram] = nVal/total
    return norm_dict
        
        
        #print(opp_score)

def getOpposite(mood):
    if (mood == "HAPPY"):
        return "SAD"
    return "HAPPY"

def paragraphAnalyzer(sentences, factor):
    total = 0.0
    power = 1.0
    for sentence in sentences:
        #Find out the mood
        #if mood is sad, power is negative
        #
        total = total + power
        power = power * factor
        pass
    
    
    
    


        

#st = "bomdiggy\n"
#st = st.strip("\n")
#print(st)

datum, mcwh, mcws = mood_to_phrase("sentient_data.txt", 2)
norm_dict = normalize_dict(datum)

def testing(sentencez):
    count = 0
    correct = []
    wrong = []
    #print(s
    for sent in sentencez:
        #sent = input("Welcome! Enter a sentence and we'll tell you the mood \n")
        sentence = sent[1].split(" ")
        #print(sent[0])
        #print(sentence)
        index = 0
        #PREPROCESS
        sentence.insert(0,"SENT-HEAD")
        sentence[len(sentence)-1] = sentence[len(sentence)-1].strip("\n")
        sentence.append("SENT-TAIL")
        happyScore = 100.00
        sadScore = 100.00
        while (index < len(sentence)-1):
            hap_bigram = ("HAPPY", sentence[index].lower(), sentence[index+1].lower())
            #print(hap_bigram)
            sad_bigram = ("SAD", sentence[index].lower(), sentence[index+1].lower())
            hapScor = norm_dict[hap_bigram]
            sScor = norm_dict[sad_bigram]
            if (hapScor == 0):
                firstWord = sentence[index].lower()
                secondWord = sentence[index+1].lower()
                happy_index = mcwh[firstWord] + mcwh[secondWord]
                sad_index = mcws[firstWord] + mcwh[secondWord]
                hapScor = happy_index/ (happy_index + sad_index)
                sadScor = sad_index/ (sad_index+ happy_index)
                #hapScor = 0.5
                #sadScor = 0.5
            happyScore = happyScore * hapScor
            sadScore = sadScore * sadScor
            index = index + 1
        #print("happy score: ", happyScore)
        #print("sad score: ", sadScore)
        verdict = ""
        if (happyScore > sadScore):
            #print("You're in a Happy Mood")
            verdict = "happy"
        elif (happyScore == sadScore):
            verdict = "neutral"
        else:
            #print("Why the sad face?")
            verdict = "sad"
        if ((sent[0].lower() == "happy" and verdict == "happy") or (sent[0].lower() == "sad" and verdict == "sad")):
            correct.append(sent[1])
        else:
            wrong.append(sent[1])
    accuracy = float(len(correct))/float(len(sentencez))
    print("You got ", (accuracy * 100), "% correct")
    print("Incorrect Sentences: ")
    for wr in wrong:
        print("----")
        print(wr)
                           
            
            
        
    

sampleSentences = [("Happy", "I feel so perfect today"), ("Happy", "The sun is shining today"),
                   ("Happy", "I will not give up today"), ("Sad", "Yeah I really do not care"),
                   ("Happy", "I would love to help you"), ("Sad", "I hate this situation"),
                   ("Happy", "Positivity is the most important aspect in life"), ("Sad", "Being negative is what life is all about"),
                   ("Happy", "This was a wonderful gift"), ("Sad", "This is the ugliest piece of crap I have ever seen"),
                   ("Sad", "Go bother someone else please"), ("Sad", "why is life so bad")
                   ,("Happy", "Life has been great to me"), ("Sad", "I want to kill myself"),
                   ("Happy", "Please take care of yourself"), ("Sad", "That test went bad"),
                   ("Happy", "I am living a great lifestyle"), ("Sad", "I dread my existence"), ("Sad", "Is there a point in living"),
                   ("Happy", "I can't wait to see the movie"), ("Happy", "This is going to be so much fun!"), ("Happy", "I want to see you be happy")]
                   


testing(sampleSentences)

    
    

    
    
