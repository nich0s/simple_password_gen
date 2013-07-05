#!/usr/bin/python2.7

'''
passwd
generates a password based off of a common attribute across the
computing platform at <insert company name here>

todo:
- add argparse / optparse to eliminate the fragile req'd arguments

auth: nich0s
date: 06262013
'''

import sys

def getMD5(commonAttribute, systemType):
  salt = "salt goes here"
  try: 
    import hashlib
  except Exception as err:
    print "Error:", err
    sys.exit(2)
  try:
    hash = hashlib.md5()
    saltedCommonAttribute = (commonAttribute + salt).upper()
    hash.update(saltedCommonAttribute)
    if systemType == "workstation":
      obsfuscatedTextPrepend = '!'
      obsfuscatedTextAppend = 'A'
      passwordHash = str(hash.hexdigest().lower())[:8]
      transformedString = obsfuscatedTextPrepend + passwordHash + obsfuscatedTextAppend
      return transformedString
    elif systemType == "server":
      obsfuscatedTextPrepend = 'a'
      obsfuscatedTextAppend = '!'
      passwordHash = str(hash.hexdigest().upper())[:8]
      transformedString = obsfuscatedTextPrepend + passwordHash + obsfuscatedTextAppend
      return transformedString
  except Exception as err:
    print "Error:", err
    sys.exit(2)

def printUsage():
  print """
Simple Password Generator
auth: nich0s

usage:
./passwd.py <commonAttribute> <systemType>

valid systemTypes: workstation, server
"""
  sys.exit(2)

def main():
  if len(sys.argv) < 3 and len(sys.argv) > 0:
    printUsage()
  elif len(sys.argv) == 3: # Sweet, sweet req'd arguments
    commonAttribute = sys.argv[1]
    systemType = sys.argv[2]
    if systemType == "workstation" or systemType == "server":
      finalProduct = getMD5(commonAttribute, systemType)
      print str(finalProduct)
  else:
    printUsage()

if __name__ == '__main__':
  main()

