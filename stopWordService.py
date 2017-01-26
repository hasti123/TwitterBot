#Remove Stop Words script
import re

stop = ["and","or","the","but","it","are","is","to","of","if","in","up","that","be","for","a","we","should","will","on","our","they","he","has","how","with","wont","well","rt","not","this","was","amp","more","going","by"]

def removeStopWords(textToFilter):
    result = []
    for word in textToFilter:
        if word.lower() not in stop:
            result.append(word)

    return result
