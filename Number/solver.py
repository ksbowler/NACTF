import base64
enc = [111,98,100,117,103,124,98,116,100,50,50,96,89,67,53,83,68,83,54,126]
print(enc)
flag = ""
for i in enc: flag += chr(i-1)
#print(base64.b64decode(flag.encode()))
print(flag)
