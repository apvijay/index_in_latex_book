#!/bin/bash

file_list=("introduction.tex")
wordsfile="words_double_uniq_out.txt"
words2file="words_uniq.txt"

for i in ${!file_list[*]}
do
   infile="${file_list[$i]}.in"
   outfile="${file_list[$i]}.out"
   out2file="${file_list[$i]}.out2"
   out3file="${file_list[$i]}.out3"
  
   printf "cp %s %s\n" "${file_list[$i]}" "$infile"
   cp "${file_list[$i]}" "$infile"
   
   printf "./add_index_to_tex.py %s %s %s\n" "$wordsfile" "$infile" "$outfile"
   ./add_index_to_tex.py "$wordsfile" "$infile" "$outfile"
   
   printf "./add_index_to_tex.py %s %s %s\n" "${words2file}" "$outfile" "${out2file}\n"
   ./add_index_to_tex.py "${words2file}" "$outfile" "${out2file}"

   printf "cp %s %s\n" "${out2file}" "${out3file}\n"  
   cp "${out2file}" "${out3file}"

   printf "sed -i \'s\/XKCD\/ \/g\' %s" "${out3file}\n"
   sed -i 's/XKCD/ /g' "${out3file}"

   printf "\n" 
   printf "________"
   printf "\n"
done