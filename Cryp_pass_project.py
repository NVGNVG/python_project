#Made by:NVG
# Python 3 code: Hash creator
# Get hash generator (string >> hexadecimal)

import hashlib

#Input and initializing
print('Word to convert to hash:')
x = input()
print('Word: ' + x) 
  
# encoding using encode()
# then sending to md5()
result = hashlib.md5(x.encode())
result_512 = hashlib.sha512(x.encode())
result_b2b = hashlib.blake2b(x.encode())  

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 hash is : ", end ="")
print(result.hexdigest())
print("The hexadecimal equivalent of SHA512 hash is : ", end ="")
print(result_512.hexdigest())
print("The hexadecimal equivalent of BLAKE2b hash is : ", end ="")
print(result_b2b.hexdigest())