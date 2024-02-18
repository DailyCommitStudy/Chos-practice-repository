n = int(input())

def fibonaci(n):
    if n > 2: return fibonaci(n-1) + fibonaci(n-2)
    elif n == 0: return 0
    else: return 1

print(fibonaci(n))