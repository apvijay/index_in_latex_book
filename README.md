These files are created to add indices to a book prepared in LaTeX.

1. Prepare list of indices. Prepare two files for single words and 
   multi words with the following format. First word before comma is 
   the word to be searched, the second word is the index name which 
   will appear in the index page.

-- File contents --
arakkan,arakkan\n
bodhi,bodhi\n
chennai,chennai\n
dry fruits, dry fruit\n
-- end --
   
2. Edit the file runme.sh and give the list of tex files and 
   word files (prepared in step 1).

3. Run runme.sh.

4. To remove any indices, prepare a word list file and run remove_index.sh.
