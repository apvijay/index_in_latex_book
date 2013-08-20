#!/usr/bin/python

import sys
import re

#wordsfile = 'words_uniq.txt'
#infile = 'introduction_in_1.tex'
#outfile = 'introduction_out.tex'

wordsfile = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]

f1 = open(infile, 'r')
f2 = open(outfile, 'w')

for line in f1:
##  print line
  line_new = ' ' + line + ' '
  g = open(wordsfile, 'r')
##  print line_new.split()
  for gline in g:
##    print gline
    if '#' not in gline:
      tmp = gline.split(',')
##      print tmp[0], tmp[1]
      word = tmp[0].lstrip()
      repl = ' \index{' + tmp[1].rstrip() + '}'
##      print word + '::' + repl + '\n'
      
      word_regex = r'([. | |\s|, |{|.\s|(]' + word + r')' +  r'([. | |\s|, |}|.\s|)])'
      p = re.compile(word_regex,re.IGNORECASE)
      
      repl_regex = r'\1' + repl + r'\2'
#      print line_new
      line_new = p.sub(repl_regex, line_new)
#      print line_new
    
  f2.write(line_new.strip() + '\n')
  g.close()

f2.close()
f1.close()
#g.close()

    
