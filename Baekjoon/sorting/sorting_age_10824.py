n = int(input())
coor_list = [list(input().split()) for _ in range(n)]

for i in range(n):
    coor_list[i][0] = int(coor_list[i][0])

for i in sorted(coor_list, key=lambda x : x[0]):
    print(*i)