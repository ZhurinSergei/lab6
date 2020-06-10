#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
	articleID = ""
	for line in sys.stdin:
		line = line.rstrip()
		data = line.split("\t")
		match = re.match(r'\d*<uniqid>', data[0])
		line = re.sub(r'<uniqid>', "", line)
		if match:
			if re.sub(r'<uniqid>', "", match.group(0)) != articleID:
				articleID = re.sub(r'<uniqid>', "", match.group(0))
			print '%s' % (line)
		else:
			print '%s\t%s' % (articleID, line)
