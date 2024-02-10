n = int(input())
deque = []

for _ in range(n):
    cmd = list(input().split())

    if cmd[0] == '1': deque.insert(0, cmd[1])
    elif cmd[0] == '2': deque.append(cmd[1])
    elif cmd[0] == '3':
        if deque: print(deque[0]); del deque[0]
        else: print(-1)
    elif cmd[0] == '4':
        if deque: print(deque[-1]); del deque[-1]
        else: print(-1)
    elif cmd[0] == '5': print(len(deque))
    elif cmd[0] == '6':
        if deque: print(0)
        else: print(1)
    elif cmd[0] == '7':
        if deque: print(deque[0])
        else: print(-1)
    else:
        if deque: print(deque[-1])
        else: print(-1)