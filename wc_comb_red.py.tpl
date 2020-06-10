#!/usr/bin/env python3
# coding=utf8
import sys
import numpy
import re

N = 10

result_count = DOCUMENTS_COUNT
regexForDelete = r"^(regexForDelete)$"
word = None
count = 0
articleID = None

pairArticleID_CountWord  = []
tmp_result_count = 0
result_key = None
result = []
match = None

for line in sys.stdin:
    data = line.split('\t')
    if len(data) < 3:
        continue
    
    currentWord = data[0]
    currentArticleID = data[1]
    currentCount = int(data[2])

    if word == None:
        word = currentWord

    if currentWord == word:
        count += currentCount
        pairArticleID_CountWord.append([currentArticleID, currentCount])
        articleID = currentArticleID
    else:
        pairArticleID_CountWord.sort(key = lambda x: int(x[0]), reverse = True)

        for i in pairArticleID_CountWord :
            if articleTMP == None:
                articleTMP = i[0]
                
            if articleTMP == i[0]:
                countTMP += i[1]
            else:
                result.append([articleTMP, countTMP, -1])
                articleTMP = i[0]
                countTMP = i[1]
                
        if len(pairArticleID_CountWord ) > 0:
            result.append([articleTMP, countTMP, -1])
            
        idf = float(numpy.log10(float(result_count) / float(count)))
        for i in range(len(result)):
            result[i][2] = result[i][1] * idf
            
        result.sort(key = lambda x: x[2], reverse = True) 
        N = 10
        if N > len(result):
            N = len(result)

        match = None
        match = re.match(regexForDelete, word);
        if match == None:
            sys.stdout.write(str(word))
            sys.stdout.write("\t")
            
            for i in range(N):
                sys.stdout.write(str(result[i][0]))
                sys.stdout.write(",")
                sys.stdout.write(str(result[i][2]))
                sys.stdout.write("\t")  
            sys.stdout.write("\n")
            
        word = currentWord
        pairArticleID_CountWord = []
        result = []
        articleTMP = None
        countTMP = 0
        count = currentCount
        pairArticleID_CountWord.append([currentArticleID, currentCount])
        articleID = currentArticleID

pairArticleID_CountWord.sort(key = lambda x: int(x[0]), reverse = True)

for i in pairArticleID_CountWord :
    if articleTMP == None:
        articleTMP = i[0]
        
    if articleTMP == i[0]:
        countTMP += i[1]
    else:
        result.append([articleTMP, countTMP, -1])
        articleTMP = i[0]
        countTMP = i[1]
        
if len(pairArticleID_CountWord ) > 0:
    result.append([articleTMP, countTMP, -1])
    
idf = float(numpy.log10(float(result_count) / float(count)))

for i in range(len(result)):
    result[i][2] = result[i][1] * idf
    
result.sort(key=lambda x: x[2], reverse=True)
N = 10
if N > len(result):
    N = len(result)
    
match = None
match = re.match(regexForDelete, word, 0);
if match == None:
    sys.stdout.write(str(word))
    sys.stdout.write("\t")
    
    for i in range(N):
        sys.stdout.write(str(result[i][0]))
        sys.stdout.write(",")
        sys.stdout.write(str(result[i][2]))
        sys.stdout.write("\t")  
        
    sys.stdout.write("\n")