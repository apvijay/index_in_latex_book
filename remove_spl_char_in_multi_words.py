#!/usr/bin/python

import sys
infile = sys.argv[1]
outfile = sys.argv[2]

f = open(infile,'r')
g = open(outfile,'w')

for line in f:
  line_words = line.split(',')
  new_line = line_words[0] + ',' + 'XKCD'.join(line_words[1].split(' '))
  g.write(new_line)

g.close()
f.close()
