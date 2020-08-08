#!/bin/sh

cd "questions/"
COMPILE_OPTION="java"

FILE=""

if [ $1 = '-p' ];then
  FILE="$2.py"
  COMPILE_OPTION="python"; shift
elif [ $1 = '-j' ]; then
  FILE="$2.java";shift
elif [ $1 = '-js' ]; then
  FILE="$2.js";shift
  COMPILE_OPTION="javascript";
else
  FILE="$1.java"
fi



if [ -f $FILE ]; then
  echo "\n\nCompiling your Code\n\n"
else
  echo "\n\n$FILE does not exist\n\n"
  exit
fi

if [ $COMPILE_OPTION = "python" ]; then
  python $1.py
elif [ $COMPILE_OPTION = "javascript" ]; then
  node $1.js
else
  javac $1.java
  java $1
fi
cd ..


