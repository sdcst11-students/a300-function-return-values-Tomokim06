#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
import math
def isInteger(x):
  if x-(math.floor(x)) == 0:
    return True
  else:
    return False


if __name__ == "__main__":
  assert isInteger( 9.5 ) == False
  assert isInteger( -2 ) == True    
  assert isInteger(0) == True
