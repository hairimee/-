year = int(input())

# 4배수를 표현할 때, year를 4로 나눴을 때 나머지가 0이면 됨
# 400배수를 표현할 때, 100배수를 표현할 때도 동일함
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')
