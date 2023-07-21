#!/usr/bin/env python3

import hashlib

print("Available hash versions in hashlib:")
for i in  hashlib.algorithms_available:
	print(i)
