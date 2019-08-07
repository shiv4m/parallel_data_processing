#!/usr/bin/env python
"""mapper.py"""

import sys

top_words = ["said","baseball","season","time","game","first","season","would","league","years"]

for line in sys.stdin:
	line = line.strip()
	temp = []
	for word in line.split():
		if word in top_words:
			temp.append(word)

	for words in line.split():
		for i in temp:
			if words != i and len(words.strip()) > 0:
				if i < words:
					print '%s\t%s' % (i + "," + words, 1)
				else:
					print '%s\t%s' % (words + "," + i, 1)
		

			