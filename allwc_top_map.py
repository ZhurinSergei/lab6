#!/usr/bin/env python
import sys

if __name__ == "__main__":
    topWord = []
    N = 20
    for line in sys.stdin:
        topWord.append(line.rstrip().split("\t"))
    topWord.sort(key = lambda x: int(x[1]), reverse = True)
    if len(topWord) < N:
        N = len(topWord)
    for i in range(N):
        print '%s\t%s\t%s' % (7, topWord[i][0], topWord[i][1])
