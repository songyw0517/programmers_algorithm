def GCD(a, b): # 최대공약수
    while True:
        r = a%b
        if r==0:
            return b
        a = b
        b = r
def LCM(a, b): # 최소공배수
    return a*b // GCD(a,b)