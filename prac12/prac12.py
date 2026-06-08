import time

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

memo_fib = {}
def fib_memo(n):
    if n in memo_fib: return memo_fib[n]
    if n <= 1: return n
    memo_fib[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo_fib[n]

def main():
    n = 30
    
    t0 = time.perf_counter()
    res1 = fib(n)
    t1 = time.perf_counter()
    dur1 = t1 - t0
    
    t2 = time.perf_counter()
    res2 = fib_memo(n)
    t3 = time.perf_counter()
    dur2 = t3 - t2
    
    speedup = ((dur1 - dur2) / dur1) * 100 if dur1 > 0 else 0
    print(f"Fib({n}) = {res2}")
    print(f"Пришвидшення: {speedup:.2f}%")

if __name__ == "__main__":
    main()