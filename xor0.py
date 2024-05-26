message = "label"
output = ""
for i in message:
    output += chr(ord(i)^13)
print(output)