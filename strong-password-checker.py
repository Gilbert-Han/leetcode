# https://leetcode.com/problems/strong-password-checker/
# https://www.dropbox.com/home/2021-interview-prep
# C:\Users\Gilbert\Dropbox\2021-interview-prep

import string

def distToRange(length, min=6, max=20):
  '''
  >>> distToRange(6, min=6, max=20)
  0
  >>> distToRange(0, min=6, max=20)
  -6
  >>> distToRange(24, min=6, max=20)
  4
  '''
  if length < min:
    return length-min
  if length > max:
    return length-max
  return 0

def hasLower(s: str):
  '''
  >>> hasLower('asdf')
  True
  >>> hasLower('ASDF')
  False
  >>> hasLower('ASdf')
  True
  >>> hasLower('')
  False
  '''
  return bool(set(s).intersection(string.ascii_lowercase))
  
def hasUpper(s: str):
  '''
  >>> hasUpper('asdf')
  False
  >>> hasUpper('ASDF')
  True
  >>> hasUpper('ASdf')
  True
  >>> hasUpper('')
  False
  '''
  return bool(set(s).intersection(string.ascii_uppercase))

def hasDigit(s: str):
  '''
  >>> hasDigit('asDF')
  False
  >>> hasDigit('0123')
  True
  >>> hasDigit('asDF012')
  True
  >>> hasDigit('')
  False
  '''
  return bool(set(s).intersection(string.digits))

def hasRepeating(s, runLength=3):
  if len(s) == 0:
    return False
  char = s[0]
  count = 1
  for ch in s[1:]:
    if ch == char:
      count += 1
    else:
      char = ch
      count = 1
    if count == runLength:
      return True
  return False
  
class Solution:
  def strongPasswordChecker(self, password: str) -> int:
    print(hasLower(password))
    print(hasUpper(password))
    print()
