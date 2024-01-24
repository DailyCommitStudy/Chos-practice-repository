n = int(input())
words = sorted(set(input() for _ in range(n)))
words = sorted(words, key=lambda x : len(x))

for i in words:
    print(i)
