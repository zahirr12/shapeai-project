import hashlib
import time

strData = input("Enter the string data : ")
timestamp = time.time();


##### md5 Salting & Iteration #####
# Salting #
md5HashObj = hashlib.md5(str(timestamp).encode('utf-8')) #creating the time stamp for salt
timeStampHash = md5HashObj.hexdigest()
salt = timeStampHash + strData # Combining time stamp with string to create a salted string

# Iteration #
for x in range(5):
	saltMd5HashObj = hashlib.md5(salt.encode('utf-8')) # creating hash and iterating new hash throughout loop for 5 times
	salt = saltMd5HashObj.hexdigest()
print("=> The salted and iterated string (md5) is : " + salt)


print("\n\n")


##### sha256 Salting & Iteration #####
# Salting #
shaHashObj = hashlib.sha256(str(timestamp).encode('utf-8')) #creating the time stamp for salt
timeStampHash = shaHashObj.hexdigest()
salt = timeStampHash + strData # Combining time stamp with string to create a salted string

# Iteration #
for x in range(5):
	saltShaHashObj = hashlib.sha256(salt.encode('utf-8')) # creating hash and iterating new hash throughout loop for 5 times
	salt = saltShaHashObj.hexdigest()
print("=> The salted and iterated string (sha256) is : " + salt)


print("\n\n")


##### blake2b Salting & Iteration #####
# Salting #
blakeHashObj = hashlib.blake2b(str(timestamp).encode('utf-8')) #creating the time stamp for salt
timeStampHash = blakeHashObj.hexdigest()
salt = timeStampHash + strData # Combining time stamp with string to create a salted string

# Iteration #
for x in range(5):
	saltBlakeHashObj = hashlib.blake2b(salt.encode('utf-8')) # creating hash and iterating new hash throughout loop for 5 times
	salt = saltBlakeHashObj.hexdigest()
print("=> The salted and iterated string (blake2b) is : " + salt)


print("\n\n")


##### shake_256 Salting & Iteration #####
# Salting #
shakeHashObj = hashlib.shake_256(str(timestamp).encode('utf-8')) #creating the time stamp for salt
timeStampHash = shakeHashObj.hexdigest(64)
salt = timeStampHash + strData # Combining time stamp with string to create a salted string

# Iteration #
for x in range(5):
	saltShakeHashObj = hashlib.shake_256(salt.encode('utf-8')) # creating hash and iterating new hash throughout loop for 5 times
	salt = saltShakeHashObj.hexdigest(64)
print("=> The salted and iterated string (shake_256) is : " + salt)