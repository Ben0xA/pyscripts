#!/usr/bin/python

# Binary Flip
# Author: Ben0xA

# Description: Flips a binary file from it's last byte to it's first.

import sys

def main():
  #get the file to flip and file to save as
  fin = sys.argv[1]
  fout = sys.argv[2]
  
  #read in the file as binary
  b = bytearray(open(fin, "rb").read())
  
  #clone the array to overwrite
  nb = bytearray(b)
  
  #go through the byte array backward
  idx = -1  
  for i in range(len(b)-1,-1,-1):
    idx += 1
    nb[idx] = b[i] #copys the last byte of b to the first byte of nb and so on.
  
  #write out new byte array to new file
  open(fout, "wb").write(nb)
  
  #profit!
  print "Created new file " + fout + " successfully"
  
if __name__ == "__main__":
  main()
