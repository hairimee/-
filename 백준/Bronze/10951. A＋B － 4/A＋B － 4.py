#while은 다양한 조건문을 내부에 추가하여 사용 가능

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break