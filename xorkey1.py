message = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
messageByte = bytes.fromhex(message)
pTinit = "crypto{"

key = []
for i in range(7):
    print(pTinit[i], " ", messageByte[i])
    key.append(int(ord(pTinit[i]) ^ messageByte[i]))
# for key in range(121,122):
key.append(ord('y'))
for i in key:
    print(chr(i), end='')
print()
answer = ""
for i in range(len(messageByte)):
    answer += chr(key[i % 8] ^ messageByte[i])
print(answer)
