#!/bin/sh

pList=""
PERSONALIZE=""


if [ $1 = '-u' ]; then
  PERSONALIZE=$1; shift
fi

if  [ "$#" -lt 2 ];then
  echo "At least 2 args must be provided"
  exit
fi


echo "Matching pairs...."

for var in "$@"
do
  pList="$pList $var"
done

export PLIST="$pList"

cd Scripts/
python match.py
cd ..