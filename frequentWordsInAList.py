#returns top 3 words in a list.

import re
def top_3_words(text):
    wordcount = {}
    arr = re.split('[^a-zA-Z\d\']',text.lower())
    print (arr)
    #look through every item in arr
    for word in arr:
        #if item is in wordcount, add 1 to that key
        if word in wordcount:
            wordcount[word] = wordcount[word]+1
        #else, add item
        else:
            wordcount[word] = 1
    if "" in wordcount:
        del wordcount[""] #remove random spaces
    if "'" in wordcount:
        del wordcount["'"]
    if "'''" in wordcount:
        del wordcount["'''"]
    print(wordcount)
    top3 = []
    if len(wordcount)>=3:
        rng = 3
    else:
        rng = len(wordcount)
    for i in range(rng):
        Keymax = max(zip(wordcount.values(), wordcount.keys()))[1]
        top3.append(Keymax)
        print(wordcount)
        del wordcount[Keymax]
    print(wordcount)
    print(top3)
    return top3