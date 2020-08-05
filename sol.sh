#!/bin/sh
# filename="pairs.txt"

# splitIndex=-1
# s=""
# strindex() {
#   x="${1%%$2*}"
#   [ "$x" = "$1" ] && echo -1 || splitIndex="${#x}"
# }

# while read line; do
# strindex "$line" "="
# STRLENGTH=`echo -n $line | wc -m`
# beg=$(echo "$line" | cut -c1-$splitIndex)
# after=$((splitIndex+2))
# end=$(echo "$line" | cut -c$after-$STRLENGTH)
#   if [ $1 = $beg ]; then
#     cd "questions/"
#     javac $end.java
#     java $end
#     cd ..
#     break
#   fi
# done < $filename
cd "questions/"
FILE="$1.java"

if [ -f $FILE ]; then
  echo "\n\nCompiling your Code\n\n"
else
  echo "\n\n$FILE does not exist\n\n"
  exit
fi

javac $1.java
java $1
cd ..


