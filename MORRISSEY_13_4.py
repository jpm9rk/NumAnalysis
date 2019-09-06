# James Morrissey
# computingID: jpm9rk

import math
import sys


# rounding machine precision assumed

# definition of some counters to be used later
i = 1.0
k = 0.0


# calculates machine precision-> the loop determines to how many sig digits the computer can tell the difference between
# numbers.
while 1.0 + i != 1:
    i = i/2.0   # for different base number systems, need to substitute 2.0 with the base
    k += 1

print('machine precision for my system is: ', i, ', the '
'computer is  capable of representing ', k,' significant digits')  # output what the machine precision is,
                                                                   # could also say machine precision is 2**-k


## definition of some counters to be used later
j = 1.0
h = 0.0


# calculates the smallest positive number is for a base 2 computer system
while j!= 0:
      j=j/2.0  # first instance of this gives B^-1
               # for different base number systems, need to substitute 2.0 with the base
      if j == 0:
          print('the smallest possible value is: ', 2**(-h))  # output what the smallest possible value is
      h += 1










