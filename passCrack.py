#!/usr/bin/env python2.7
import mincemeat
import hashlib
import sys

data=[]
# Don't forget to start a client!
# ./mincemeat.py -l -p changeme
inp=sys.argv[1]
def shuffle(length, possibles):
  ret = []
  if length == 1:
    return list(possibles)
  else:
    subs = shuffle(length -1, possibles)
    for ch in possibles:
      for sub in subs:
        ret.append(str(ch) + str(sub))
        
  return ret  

data1=shuffle(1,"abcdefghijklmnopqrstuvwxyz0123456789")
data2=shuffle(2,"abcdefghijklmnopqrstuvwxyz0123456789")
data3=shuffle(3,"abcdefghijklmnopqrstuvwxyz0123456789")
data4=shuffle(4,"abcdefghijklmnopqrstuvwxyz0123456789")

data = data1+data2+data3+data4

# The data source can be any dictionary-like object


temp = ''
counter = 0
datasource = {}
for line in data:
  temp = temp +  line.rstrip() + ' '
  if counter % 1000 == 0:
    temp=temp+inp
    datasource[counter] = temp
    temp = ''
  counter += 1
datasource[counter] = temp


def mapfn(k, v):
    import md5
    z= v.split()
    hashstr =z[-1]
    for word in z:
      word = word.strip()
      p = md5.new(word).hexdigest()
      if p[:5]==hashstr:
       yield word,hashstr 

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results
