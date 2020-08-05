import os
import random

def clean_list(participants):
  for i in range(len(participants)):
    participants[i] = participants[i][0].capitalize() + participants[i][1:]


def make_rotate(l):
  n = []
  for i in range(1, len(l)):
    n.append(l[i])
  n.append(l[0])
  return n

def add_question(a, b):
  cur_path = os.path.dirname(__file__)
  to_write_in = os.path.relpath(f'../Interview-Prep/questions/{a}.java', cur_path)
  to_write_from = os.path.relpath(f'../Interview-Prep/Descriptions/{b}.txt',cur_path)

  f1 = f2 = ""

  with open(to_write_in, 'r') as fp1:
    f1 = fp1.read()
  with open(to_write_from, 'r') as fp2:
    f2 = fp2.read()

  f2 = f'/* {f2} */'
  f3 = f1 + f2
  with open(to_write_in, 'w') as f:
    f.write(f3)

def make_tuple(ps):
  pair_list = []

  random.shuffle(ps)
  shifted_list = make_rotate(ps)
  
  for a,b in ps, shifted_list:
    pair_list.append([a, b])

  for i in range(len(pair_list)):
    a = pair_list[i]
    add_question(a[0], a[1])

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
pairs = make_tuple(participant_list)
set_os_params(pairs)

print("Pair matching completed")
for tup in pairs:
  print(tup[0]+" = "+tup[1])