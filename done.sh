#!/bin/sh

if [ -f $1  ]; then
  echo "Argument name must be provided"
  exit
fi

touch PastQuestions/$1.txt

for n in questions/*.java; do
  cat $n >> PastQuestions/$1.txt
  echo "\n\n" >> PastQuestions/$1.txt
done

rm -rf questions/*
cp /dev/null pairs.txt