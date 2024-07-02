x = int(input())
y = int(input())

# =과 괄호는 딱히 없어도 될 것 같기도 ?
if (x >= 0) and (y >= 0):
    print('1')
elif (x <= 0) and (y >= 0):
    print('2')
elif (x <= 0) and (y <= 0):
    print('3')
else:
    print('4')
