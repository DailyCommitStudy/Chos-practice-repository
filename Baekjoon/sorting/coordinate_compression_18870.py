n = int(input())
coor = list(map(int, input().split()))
compression = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if coor[i] > coor[j]:
            compression[i] += 1

print(*compression)