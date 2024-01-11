n = int(input())
num_list = list(int(input()) for _ in range(n))

num_list.sort()

for i in range(n):
    print(num_list[i])