#!/usr/bin/env python
import sys

countArticle = 0
currentArticleID = None

for line in sys.stdin:
    data = line.split('\t')
    articleID = data[0]

    if currentArticleID != articleID:
        currentArticleID = articleID
        countArticle += 1

print '%s' % (countArticle)
