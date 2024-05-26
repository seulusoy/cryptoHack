message = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
messageByte = bytes.fromhex(message)
key = ord('c') ^ messageByte[0]
answer = ""
for i in messageByte:
    answer += chr(key ^ i)
print(answer)
