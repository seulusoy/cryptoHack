def gcd(a:int, b:int) -> int:
    if(b<2):
        return a
    return gcd(b, a%b)

print(gcd(66528, 52920))