import codecs
from importlib import reload
from collections import defaultdict
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8') 

#reload(sys)  
#sys.setdefaultencoding('utf8')

punct = [".", ",", "-", "...", "....", "!", "?", "--", ";", ":"]
theta = 2.44

def non_terminal_punctuation(sentence):
    index = 1
    count = 0
    nonTerminalOccurence = False
    for word in range(0,len(sentence)):
        if sentence[word] in punct:
            if (index < len(sentence)):
                count = count + 1
        index += 1
    return count

            
#n-gram
def mood_to_phrase_2gram(file):
    nonterminal_punct_by_mood = defaultdict(float)
    mood_to_sent_count = defaultdict(float)
    most_common_words_happy = defaultdict(lambda:2.2)
    most_common_words_sad = defaultdict(lambda:2.2)
    most_common_words_funny = defaultdict(lambda:1.2)
    openFile = open(file, "r", encoding="utf-8")
    readlines = openFile.readlines()
    print(len(readlines))
    for line in readlines:
        mood_sentence = line.split(":")
        mood = mood_sentence[0]
        sentence = mood_sentence[1].split(" ")
        if (non_terminal_punctuation(sentence) > 0):           
            nonterminal_punct_by_mood[mood] += 1
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
            if (mood.lower() == "funny" and sentence[index] != "SENT-HEAD"):
                most_common_words_funny[sentence[index].lower()] += 1
            mood_to_sent_count[bigram] += 1
            index = index + 1
    openFile.close()
    return mood_to_sent_count, most_common_words_happy, most_common_words_sad, most_common_words_funny, nonterminal_punct_by_mood
            
def mood_to_phrase_3gram(file):
    nonterminal_punct_by_mood = defaultdict(float)
    mood_to_sent_count = defaultdict(float)
    most_common_words_happy = defaultdict(lambda:1.5)
    most_common_words_sad = defaultdict(lambda:1.5)
    most_common_words_funny = defaultdict(lambda:0.9)
    openFile = open(file, "r", encoding="utf-8")
    readlines = openFile.readlines()
    print(len(readlines))
    for line in readlines:
        mood_sentence = line.split(":")
        mood = mood_sentence[0]
        sentence = mood_sentence[1].split(" ")
        if (non_terminal_punctuation(sentence) > 0):           
            nonterminal_punct_by_mood[mood] += 1
        sentence.insert(0, "SENT-HEAD")
        sentence[len(sentence)-1] = sentence[len(sentence)-1].strip("\n")
        sentence.append("SENT-TAIL")
        index = 0
        sentLen = len(sentence)
        while(sentence[index+1] != "SENT-TAIL"):
            trigram = (mood.upper(), sentence[index].lower(), sentence[index+1].lower(), sentence[index+2].lower())
            if (mood.lower() == "happy" and sentence[index] != "SENT-HEAD" ):
                most_common_words_happy[sentence[index].lower()] += 1
            if (mood.lower() == "sad" and sentence[index] != "SENT-HEAD"):
                most_common_words_sad[sentence[index].lower()] += 1
            if (mood.lower() == "funny" and sentence[index] != "SENT-HEAD"):
                most_common_words_funny[sentence[index].lower()] += 1
            mood_to_sent_count[trigram] += 1
            index = index + 1
    openFile.close()
    return mood_to_sent_count, most_common_words_happy, most_common_words_sad, most_common_words_funny, nonterminal_punct_by_mood

def normalize_dict2(m_to_s):
    norm_dict = defaultdict(float)
    copy_dict = m_to_s.copy()
    #mood = ["HAPPY", "SAD"]
    for key, value in m_to_s.items():
        #print("CURRLEN: m_to_s.items: ", len(m_to_s.items()))
        opp = getOpposite(key[0])
        total = value
        others = []
        for o in opp:
            newBigram = (o, key[1], key[2])
            others.append(newBigram)
        for oth in others:
            nVal = copy_dict[oth]
            total = total + nVal
        norm_dict[key] = value/total
        norm_dict[others[0]] = copy_dict[others[0]]/total
        norm_dict[others[1]] = copy_dict[others[1]]/total
    return norm_dict
        
def normalize_dict3(m_to_s):
    norm_dict = defaultdict(float)
    copy_dict = m_to_s.copy()
    #mood = ["HAPPY", "SAD"]
    for key, value in m_to_s.items():
        #print("CURRLEN: m_to_s.items: ", len(m_to_s.items()))
        opp = getOpposite(key[0])
        total = value
        others = []
        for o in opp:
            newBigram = (o, key[1], key[2], key[3])
            others.append(newBigram)
        for oth in others:
            nVal = copy_dict[oth]
            total = total + nVal
        norm_dict[key] = value/total
        norm_dict[others[0]] = copy_dict[others[0]]/total
        norm_dict[others[1]] = copy_dict[others[1]]/total
    return norm_dict

def getOpposite(mood):
    if (mood == "HAPPY"):
        return ["SAD", "FUNNY"]
    elif (mood == "SAD"):
        return ["HAPPY", "FUNNY"]
    return ["SAD", "HAPPY"]

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

datum2, mcwh2, mcws2, mcwf2, ntp2= mood_to_phrase_2gram("sentient_data.txt")
norm_dict2 = normalize_dict2(datum2)
datum3, mcwh3, mcws3, mcwf3, ntp3 = mood_to_phrase_3gram("sentient_data.txt")
norm_dict3 = normalize_dict3(datum3)

#print("&&&&")
#print(ntp2)
#print("&&&&")
#print(ntp3)

def testing2(sentencez, detailed):
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
        funnyScore = 100.00
        cap = 0
        total_punct = 0.0
        for val in ntp2.values():
            total_punct += val
        while (sentence[index+cap] != "SENT-TAIL"):
            hap_bigram = ("HAPPY", sentence[index].lower(), sentence[index+1].lower())
            #print(hap_bigram)
            sad_bigram = ("SAD", sentence[index].lower(), sentence[index+1].lower())
            funny_bigram = ("FUNNY", sentence[index].lower(), sentence[index+1].lower())
            hapScor = norm_dict2[hap_bigram]
            sadScor = norm_dict2[sad_bigram]
            fScor = norm_dict2[funny_bigram]
            if (hapScor == 0):
                firstWord = sentence[index].lower()
                secondWord = sentence[index+1].lower()
                #thirdWord = sentence[index+2].lower()
                happy_index = mcwh2[firstWord] + mcwh2[secondWord]
                sad_index = mcws2[firstWord] + mcws2[secondWord]
                funny_index = mcwf2[firstWord] + mcwf2[secondWord]
                #happy_index = mcwh[firstWord] + mcwh[secondWord] + mcwh[thirdWord]
                #sad_index = mcws[firstWord] + mcws[secondWord] + mcws[thirdWord]
                hapScor = max(hapScor, happy_index)/ (happy_index + sad_index+ funny_index)
                sadScor = max(sadScor, sad_index)/ (sad_index+ happy_index+ funny_index)
                fScor = max(fScor, funny_index)/ (sad_index+ happy_index+ funny_index)
                #hapScor = 0.5
                #sadScor = 0.5
            happyScore = happyScore * hapScor
            sadScore = sadScore * sadScor
            funnyScore = funnyScore * fScor
            index = index + 1
        #print("happy score: ", happyScore)
        #print("sad score: ", sadScore)
        verdict = ""
        if (non_terminal_punctuation(sentence) > 0):
            happyScore = (happyScore + (theta * ntp2["Happy"]/total_punct))/2
            sadScore = (sadScore + (theta * ntp2["Sad"]/total_punct))/2
            funnyScore = (funnyScore + (theta * ntp2["Funny"]/total_punct))/2
        if (max(happyScore, sadScore,funnyScore) == funnyScore):
            verdict = "funny"
        elif (max(happyScore, sadScore,funnyScore) == happyScore):
            verdict = "happy"
        else:
            verdict = "sad"
        if (sent[0].lower() == verdict):
            correct.append(sent[1])
        else:
            wrong.append(sent[1])
    accuracy = float(len(correct))/float(len(sentencez))
    print("You got ", (accuracy * 100), "% correct")
    if (detailed == True):
        print("Incorrect Sentences: ")
        for wr in wrong:
            print("----")
            print(wr)

def testing3(sentencez, detailed):
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
        funnyScore = 100.00
        cap = 1
        total_punct = 0.0
        for val in ntp3.values():
            total_punct += val
        while (sentence[index+cap] != "SENT-TAIL"):
            hap_bigram = ("HAPPY", sentence[index].lower(), sentence[index+1].lower(), sentence[index+2].lower())
            #print(hap_bigram)
            sad_bigram = ("SAD", sentence[index].lower(), sentence[index+1].lower(), sentence[index+2].lower())
            funny_bigram = ("FUNNY", sentence[index].lower(), sentence[index+1].lower())
            hapScor = norm_dict3[hap_bigram]
            sadScor = norm_dict3[sad_bigram]
            funScor = norm_dict3[funny_bigram]
            if (hapScor == 0):
                firstWord = sentence[index].lower()
                secondWord = sentence[index+1].lower()
                thirdWord = sentence[index+2].lower()
#                happy_index = mcwh[firstWord] + mcwh[secondWord]
#                sad_index = mcws[firstWord] + mcws[secondWord]
                happy_index = mcwh3[firstWord] + mcwh3[secondWord] + mcwh3[thirdWord]
                sad_index = mcws3[firstWord] + mcws3[secondWord] + mcws3[thirdWord]
                funny_index = mcwf3[firstWord] + mcwf3[secondWord] + mcwf3[thirdWord]
                hapScor = max(hapScor, (happy_index))/ (happy_index +funny_index + sad_index)
                sadScor = max(sadScor, (sad_index))/ (sad_index+ funny_index + happy_index)
                funScor = max(funScor, (funny_index))/ (sad_index+ funny_index + happy_index)
                #hapScor = 0.5
                #sadScor = 0.5
            happyScore = happyScore * hapScor
            sadScore = sadScore * sadScor
            funnyScore = funnyScore * funScor
            index = index + 1
        total = happyScore + sadScore + funnyScore
        chanceHappy = (happyScore*100)/total
        chanceSad = (sadScore*100)/total
        chanceFunny = (funnyScore*100)/total
        verdict = ""
        
        if (non_terminal_punctuation(sentence) > 0):
            happyScore = (happyScore + (theta* ntp3["Happy"]/total_punct))/2
            sadScore = (sadScore + (theta* ntp3["Sad"]/total_punct))/2
            funnyScore = (funnyScore + (theta * ntp3["Funny"]/total_punct))/2
        
        if (max(happyScore, sadScore,funnyScore) == funnyScore):
            verdict = "funny"
        elif (max(happyScore, sadScore,funnyScore) == happyScore):
            verdict = "happy"
        else:
            verdict = "sad"
        if (sent[0].lower() == verdict):
            correct.append(sent[1])
        else:
            wrong.append(sent[1])
    accuracy = float(len(correct))/float(len(sentencez))
    print("You got ", (accuracy * 100), "% correct")
    if (detailed == True):
        print("Incorrect Sentences: ")
        for wr in wrong:
            print("----")
            print(wr)
        
def add2Data(fileName, sentence, mood):
    file = open(fileName, "a")
    newsent = mood +": "  + sentence + "\n"
    file.write(newsent)
    file.close()
                           
def trySent():
    count = 0
    correct = []
    wrong = []
    while (input("Would you like to continue \n ?") == "y"):
        sent = input("Welcome! Enter a sentence and we'll tell you the mood \n")
        actualMood = input("What's the mood?: ")
        if (actualMood.lower() == "h" or actualMood.lower() == "happy"):           
            add2Data("sentient_data.txt", sent, "Happy")
        elif (actualMood.lower() == "s" or actualMood.lower() == "sad"):
            add2Data("sentient_data.txt", sent, "Sad")
        else:
            add2Data("sentient_data.txt", sent, "Funny")
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
        funnyScore = 100.00
        cap = 0
        while (sentence[index+cap] != "SENT-TAIL"):
            #hap_bigram = ("HAPPY", sentence[index].lower(), sentence[index+1].lower(), sentence[index+2].lower())
            #print(hap_bigram)
            hap_bigram = ("HAPPY", sentence[index].lower(), sentence[index+1].lower())
            #sad_bigram = ("SAD", sentence[index].lower(), sentence[index+1].lower(), sentence[index+2].lower())
            sad_bigram = ("SAD", sentence[index].lower(), sentence[index+1].lower())
            funny_bigram = ("FUNNY", sentence[index].lower(), sentence[index+1].lower())
            hapScor = norm_dict2[hap_bigram]
            sadScor = norm_dict2[sad_bigram]
            fScor = norm_dict2[funny_bigram]
            if (hapScor == 0):
                firstWord = sentence[index].lower()
                secondWord = sentence[index+1].lower()
                #thirdWord = sentence[index+2].lower()
                happy_index = mcwh2[firstWord] + mcwh2[secondWord]
                sad_index = mcws2[firstWord] + mcws2[secondWord]
                funny_index = mcwf2[firstWord] + mcwf2[secondWord]
 #               happy_index = mcwh[firstWord] + mcwh[secondWord] + mcwh[thirdWord]
#                sad_index = mcws[firstWord] + mcws[secondWord] + mcws[thirdWord]
                hapScor = max(hapScor, (happy_index))/ (happy_index + sad_index + funny_index)
                sadScor = max(sadScor, (sad_index))/ (sad_index+ happy_index + funny_index)
                fScor = max(fScor, (funny_index))/ (funny_index + happy_index + sad_index)
                #hapScor = 0.5
                #sadScor = 0.5
            happyScore = happyScore * hapScor
            sadScore = sadScore * sadScor
            funnyScore = funnyScore * fScor
            index = index + 1
        total = happyScore + sadScore + funnyScore
        chanceHappy = happyScore/total
        chanceSad = sadScore/total
        chanceFunny = funnyScore/total
        verdict = ""
        print(chanceHappy*100, "% chance it's happy")
        print(chanceFunny*100, "% chance it's funny")
        print(chanceSad*100, "% chance it's sad")
            
        
    

sampleSentences = [("Happy", "I feel so perfect today"), ("Happy", "The sun is shining today"),
                   ("Happy", "I will not give up today"), ("Sad", "Yeah I really do not care"),
                   ("Happy", "I would love to help you"), ("Sad", "I hate this situation"),
                   ("Happy", "Positivity is the most important aspect in life"), ("Sad", "Being negative is what life is all about"),
                   ("Happy", "This was a wonderful gift"), ("Sad", "This is the ugliest piece of crap I have ever seen"),
                   ("Sad", "Go bother someone else please"), ("Sad", "why is life so bad")
                   ,("Happy", "Life has been great to me"), ("Sad", "I want to kill myself"),
                   ("Happy", "Please take care of yourself"), ("Sad", "That test went bad"),
                   ("Happy", "I am living a great lifestyle"), ("Sad", "I dread my existence"), ("Sad", "Is there a point in living"),
                   ("Happy", "I can't wait to see the movie"), ("Happy", "This is going to be so much fun!"), ("Happy", "I want to see you be happy"), ("Happy", "I cannot wait for tomorrow"),
                   ("Happy", "The world is filled with opportunities"), ("Sad", "They never got a fair share in life"),
                   ("Sad", "I think we should break up now"), ("Happy", "Be happy with what you have"),
                   ("Happy", "I loved that movie School of Rock"), ("Sad", "I won't be able to go tonight"), ("Funny", "Welcome to Willy Wonka's wacky world !"), ("Funny", "They didnt even like me ! Sad!")]
                   

print("BIGRAM RESULTS: ")
testing2(sampleSentences, False)
print("...............")

print("TRIGRAM RESULTS: ")
testing3(sampleSentences, False)

    
    

    
    
