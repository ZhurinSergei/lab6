#!/usr/bin/env python
import sys

word = None
count = 0

for line in sys.stdin:
    data = line.split('\t')
    currentWord = data[0]
    currentCountWord = int(data[1])

    if currentWord == word:
        count += currentCountWord
    else:
        if word:
            print '%s\t%s' % (word, count)
        count = currentCountWord
        word = currentWord

print '%s\t%s' % (word, count)
