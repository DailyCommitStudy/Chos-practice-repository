n = int(input())
divisor = sorted(list(map(int, input().split())))

if n == 1:
    print(divisor[0]*divisor[0])
else:
    print(divisor[0]*divisor[-1])