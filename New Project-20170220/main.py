# Hello World program in Python
import numpy as np

scale=16
numofbits=8
hexmess='AFC04D'
message=bin(int(hexmess,scale))[2:]
print message
length=len(message)
hexkey='C92B39'
key=bin(int(hexkey,scale))[2:]
tempmessage=list(message)
tempkey=list(key)
intmessage=np.array(tempmessage)
intkey=np.array(tempkey)
print intmessage
print intkey
cipher=[]
for i in range(0,len(message)):
    j=int(intmessage[i])
    k=int(intkey[i])
    cipher[i]=j^k
    print cipher
print cipher
