#!/usr/bin/env python
import sys

prevCountArticle = None
for line in sys.stdin:
    words = line.rstrip().lower().split()
    countArticle = words[0].rstrip()
    
    if prevCountArticle != countArticle:
        print '%s\t%s' % (countArticle, 7)
        prevCountArticle = countArticle
