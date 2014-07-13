#!/usr/bin/python

from sys import exit
from operator import xor
import time

now = time.strftime('%m%d%Y%H%M%S')

def getaccess(mask, ditdah, salt):
  fn = []
  tn = []
  ditdah = ditdah.replace(" ", "")
  idx = -1
  ddidx = -1
  tidx = -1
  if(int(now[-2:]) < 30):
    nstr = time.strftime('%m%d%Y%H%M') + "00" + str(salt)
  else:
    nstr = time.strftime('%m%d%Y%H%M') + "30" + str(salt)

  for ltr in mask:
    idx += 1
    ddidx += 1
    tidx +=1
    if(ddidx >= len(ditdah)):
      ddidx = 0
    if(tidx >= len(nstr)):
      tidx = 0

    fn.append(chr(xor(xor(ord(ltr), ord(ditdah[ddidx:ddidx+1])), ord(nstr[tidx:tidx+1]))))
  fnstr = "".join(map(str, fn))
  return fnstr
  
def main():
  firsthacker = "Nevil Maskelyn"
  rats = ".-. .- - ..."
  year = "1903"
  print getaccess(firsthacker, rats, year)
  
if __name__ == "__main__":
  main()
