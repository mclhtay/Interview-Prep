#!/bin/sh

pList=""
if  [ "$#" -lt 2 ];then
  echo "At least 2 args must be provided"
  exit
fi


echo "Matching pairs...."

for var in "$@"
do
  pList="$pList $var"
  touch "questions/$var.java"
  echo 'public class '$var'{\n\tpublic static void main(String [] args){\n\t\tSystem.out.println("'$var' running");\n\t}\n}' > questions/$var.java
done

export PLIST="$pList"

python match.py

