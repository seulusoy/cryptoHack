import base64
input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf".encode()
output = base64.b64encode(input)
print(output)