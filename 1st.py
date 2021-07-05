import hashlib

strData = input("Enter the string data : ")
hashObj = hashlib.md5(strData.encode('utf-8'))
md5 = hashObj.hexdigest()
print("The md5 of given string is " + md5)