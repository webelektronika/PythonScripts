#!/usr/bin/env python3

import hashlib
from datetime import datetime


hashValue = input("* Enter a string to hash: ")
hatar = 10000000

dtMD5_1 = datetime.now()
for i in range(1, hatar):
	hashObj1 = hashlib.md5()
	hashObj1.update(hashValue.encode())
dtMD5_2 = datetime.now()
dtDeltaMD5 = dtMD5_2 - dtMD5_1
print("MD5: " + str(dtDeltaMD5))

dtSHA1_1 = datetime.now()
for i in range(1, hatar):
	hashObj2 = hashlib.sha1()
	hashObj2.update(hashValue.encode())
dtSHA1_2 = datetime.now()
dtDeltaSHA1 = dtSHA1_2 - dtSHA1_1
print("SHA1: " + str(dtDeltaSHA1))

dtSHA224_1 = datetime.now()
for i in range(1, hatar):
	hashObj3 = hashlib.sha224()
	hashObj3.update(hashValue.encode())
dtSHA224_2 = datetime.now()
dtDeltaSHA224 = dtSHA224_2 - dtSHA224_1
print("SHA224: " + str(dtDeltaSHA224))

dtSHA256_1 = datetime.now()
for i in range(1, hatar):
	hashObj4 = hashlib.sha256()
	hashObj4.update(hashValue.encode())
dtSHA256_2 = datetime.now()
dtDeltaSHA256 = dtSHA256_2 - dtSHA256_1
print("SHA256: " + str(dtDeltaSHA256))

dtSHA384_1 = datetime.now()
for i in range(1, hatar):
	hashObj5 = hashlib.sha384()
	hashObj5.update(hashValue.encode())
dtSHA384_2 = datetime.now()
dtDeltaSHA384 = dtSHA384_2 - dtSHA384_1
print("SHA384: " + str(dtDeltaSHA384))

dtSHA512_1 = datetime.now()
for i in range(1, hatar):
	hashObj6 = hashlib.sha512()
	hashObj6.update(hashValue.encode())
dtSHA512_2 = datetime.now()
dtDeltaSHA512 = dtSHA512_2 - dtSHA512_1
print("SHA512: " + str(dtDeltaSHA512))

dtSHA3_224_1 = datetime.now()
for i in range(1, hatar):
	hashObj7 = hashlib.sha3_224()
	hashObj7.update(hashValue.encode())
dtSHA3_224_2 = datetime.now()
dtDeltaSHA3_224 = dtSHA3_224_2 - dtSHA3_224_1
print("SHA3_224: " + str(dtDeltaSHA3_224))

dtSHA3_256_1 = datetime.now()
for i in range(1, hatar):
	hashObj8 = hashlib.sha3_256()
	hashObj8.update(hashValue.encode())
dtSHA3_256_2 = datetime.now()
dtDeltaSHA3_256 = dtSHA3_256_2 - dtSHA3_256_1
print("SHA3_256: " + str(dtDeltaSHA3_256))

dtSHA3_384_1 = datetime.now()
for i in range(1, hatar):
	hashObj9 = hashlib.sha3_384()
	hashObj9.update(hashValue.encode())
dtSHA3_384_2 = datetime.now()
dtDeltaSHA3_384 = dtSHA3_384_2 - dtSHA3_384_1
print("SHA3_384: " + str(dtDeltaSHA3_384))

dtSHA3_512_1 = datetime.now()
for i in range(1, hatar):
	hashObj10 = hashlib.sha3_512()
	hashObj10.update(hashValue.encode())
dtSHA3_512_2 = datetime.now()
dtDeltaSHA3_512 = dtSHA3_512_2 - dtSHA3_512_1
print("SHA3_512: " + str(dtDeltaSHA3_384))

print("MD5: " + hashObj1.hexdigest())
print("SHA1: " + hashObj2.hexdigest())
print("SHA224: " + hashObj3.hexdigest())
print("SHA256: " + hashObj4.hexdigest())
print("SHA384: " + hashObj5.hexdigest())
print("SHA512: " + hashObj6.hexdigest())
print("SHA3_224: " + hashObj7.hexdigest())
print("SHA3_256: " + hashObj8.hexdigest())
print("SHA3_384: " + hashObj9.hexdigest())
print("SHA3_512: " + hashObj10.hexdigest())
