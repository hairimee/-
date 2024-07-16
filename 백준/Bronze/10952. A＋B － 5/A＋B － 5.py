#while은 조건이 끝날 때까지 계속

while 1:
    a,b = map(int, input().split())
    if (a==0 and b==0):
        break
    else:
        print(a+b)