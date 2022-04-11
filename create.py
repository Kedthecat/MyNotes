#!/usr/bin/env python3

from __future__ import print_function

#tart with 00 and add any others you find
bad = "00 a0 ad be de ef".split()

#turns them into a nice string to copy into python
print("badchars = ")
for x in range(1, 256):
	if "{:02x}".format(x) not in bad: 
		print("\\x" + "{:02x}".format(x), end='')

#creates a nice string to use in Mona
print("\n\nfor mona")
for byte in bad:
	print("\\x{}".format(byte), end='')
print()

#00 a0 a1 ad ae be bf de df ef f0