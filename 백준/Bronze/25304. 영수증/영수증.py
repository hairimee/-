"""
    구매한 각 물건의 가격과 개수
    구매한 물건들의 총 금액
    => 가격과 개수로 총 금액 맞는지 확인해보기  
"""
X = int(input())
N = int(input())

S = 0

for i in range(N):
    a, b = map(int, input().split())
    S += a * b

if S == X:
    print("Yes")
else:
    print("No")
