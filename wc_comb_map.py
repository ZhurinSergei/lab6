#!/usr/bin/env python
import sys

for line in sys.stdin:
    words = line.rstrip().lower().split()
    articleID = words[0].rstrip()
    
    for i in range(1, len(words)):
        print '%s\t%s\t%s' % (words[i].rstrip(), articleID, 1)
