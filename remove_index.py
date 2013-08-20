#!/usr/bin/python

import sys
import os

wordsfile = sys.argv[1]
texfile = sys.argv[2]

f1 = open(wordsfile, 'r')

for line in f1:
  print line.strip()
  if '#' in line: 
    # skip comments-like lines
    continue
  words = line.split(',')
  old_word = words[0].strip()
  new_word = words[1].strip()

  if new_word == 'REMOVE_THIS': 
    # to remove index
    run_cmd = r"sed -i 's/ \\index{" + old_word + r"}//g' " + texfile
  else: 
    # to replace old with new index
    run_cmd = r"sed -i 's/\\index{" + old_word + r"}/\\index{" + new_word +\
                                       "}/g' " + texfile
  os.system(run_cmd)

f1.close()
