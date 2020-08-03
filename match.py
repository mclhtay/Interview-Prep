import os
import random

def clean_list(participants):
  for i in range(len(participants)):
    participants[i] = participants[i].lower().capitalize()


def make_rotate(l):
  n = []
  for i in range(1, len(l)):
    n.append(l[i])
  n.append(l[0])
  return n

def make_tuple(ps):
  pair_list = []

  random.shuffle(ps)
  shifted_list = make_rotate(ps)
  
  for a,b in zip(ps, shifted_list):
    pair_list.append((a, b))
  return pair_list


def set_os_params(tl):
  open("pairs.txt", "w").close()
  f = open("pairs.txt", "w")
  for t in tl:
    f.write(t[0]+"="+t[1]+"\n")
  f.close()


participant_list = os.environ['PLIST']

participant_list = str.split(participant_list)
clean_list(participant_list)
make_tuple(participant_list)
pairs = make_tuple(participant_list)
set_os_params(pairs)

print("Pair matching completed")
for tup in pairs:
  print(tup[0]+" = "+tup[1])