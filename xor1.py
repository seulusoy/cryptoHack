KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY21 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAGKEY132 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
FLAG = FLAGKEY132 ^ KEY23 ^ KEY1
FLAGstr = hex(FLAG)
print(FLAGstr)
print(bytes.fromhex(FLAGstr[2:]))