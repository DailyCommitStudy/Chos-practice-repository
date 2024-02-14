n = int(input())
deck = [i for i in range(1, n+1)]

for _ in range(n):
    del deck[0]
    first = deck.pop(0)
    deck.append(first)

    if len(deck) == 1:
        print(deck[0])
        break
