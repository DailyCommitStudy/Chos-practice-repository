N = int(input())
sorted_list = sorted(list(int(input()) for _ in range(N)))

for i in range(N):
    print(sorted_list[i])