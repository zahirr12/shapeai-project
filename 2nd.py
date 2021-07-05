import hashlib

strData = input("Enter the string data : ")

#sha256
shaHashObj = hashlib.sha256(strData.encode('utf-8'))
sha256 = shaHashObj.hexdigest()
print("=> The sha256 of " + strData + " is : " + sha256 + "\n")


#Blake2b
blakeHashObj = hashlib.blake2b(strData.encode('utf-8'))
blake2b = blakeHashObj.hexdigest()
print("=> The blake2b of " + strData + " is : " + blake2b + "\n")


#shake_256
shakeHashObj = hashlib.shake_256(strData.encode('utf-8'))
shake256 = shakeHashObj.hexdigest(64)
print("=> The shake256 of " + strData + " is : " + shake256 + "\n")