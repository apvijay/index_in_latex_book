#!/usr/bin/python

infile = 'words_double_uniq.txt'
outfile = 'words_double_uniq_out.txt'
f = open(infile,'r')
g = open(outfile,'w')

for line in f:
  line_words = line.split(',')
  new_line = line_words[0] + ',' + 'XKCD'.join(line_words[1].split(' '))
  g.write(new_line)

g.close()
f.close()
