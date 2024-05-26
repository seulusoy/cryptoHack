from Crypto.Util.number import *
testMessage = "HELLO"

testAscii = []
for i in testMessage:
    testAscii.append(ord(i))
print(testAscii)
testAsciiIn = [72, 69, 76, 76, 79]

for i in testAscii:
    print(hex(i), end=", ")
print()
testHexIn = [0x48, 0x45, 0x4c, 0x4c, 0x4f]

testInt = 0x0
for i in testAscii:
    testInt *= 0x100
    testInt += i
print(hex(testInt))
testHexIntIn = 0x48454c4c4f

print(testInt)
testDecIntIn = 310400273487

message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
messageString = long_to_bytes(message)
print(messageString)
messageR = bytes_to_long(messageString)
print(messageR)