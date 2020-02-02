#!/bin/bash

# Write a bash script to calculate the frequency of each word in a text file words.txt.

# For simplicity sake, you may assume:

# words.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.

# 1. grab the full document
# 2. move each word onto its own line
# 3. sort the lines such that the same line appears side by side with others 
# 4. remove recurring spaces
# 5. count the unique lines
# 6. swap the two columns to adhere to the problem requirements
# 7. Sort in reverse order by the value of the second column
cat words.txt | tr ' ' '\n' | sort | sed -r '/^\s*$/d' | uniq -c | awk '{t = $1; $1 = $2; $2 = t; print;}' | sort -k2 -n -r