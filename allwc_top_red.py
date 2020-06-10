#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
    topWord = []
    N = 20
    
    for line in sys.stdin:
        topWord.append(line.rstrip().split("\t"))
    topWord.sort(key = lambda x: int(x[2]), reverse = True)
    
    if len(topWord) < N:
        N = len(topWord)
        
    for i in range(N):
        topWord[i][1] = re.sub(r'\|', "\\\\\\\\|", topWord[i][1])
        topWord[i][1] = re.sub(r"\*", "\\\\\\\\*", topWord[i][1])
        topWord[i][1] = re.sub(r"\+", "\\\\\\\\+", topWord[i][1])
        topWord[i][1] = re.sub(r"\.", "\\\\\\\\.", topWord[i][1])
        topWord[i][1] = re.sub(r"\(", "\\\\\\\\(", topWord[i][1])
        topWord[i][1] = re.sub(r"\)", "\\\\\\\\)", topWord[i][1])
        if i == (N - 1):
            sys.stdout.write(topWord[i][1].rstrip("\n\r\t"))
        else:
            sys.stdout.write(topWord[i][1].rstrip("\n\r\t"))
            sys.stdout.write("|")
