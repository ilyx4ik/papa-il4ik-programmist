import sys

def factorial(n):
    if n < 0: raise ValueError("Від'ємне число")
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 0: raise ValueError("Від'ємне число")
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def recursive_sum(lst):
    if not lst: return 0
    return lst[0] + recursive_sum(lst[1:])

def is_palindrome(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_palindrome(s[1:-1])

def run_tests():
    assert factorial(5) == 120
    assert fibonacci(6) == 8
    assert recursive_sum([1, 2, 3, 4]) == 10
    assert is_palindrome("radar") == True
    print("Тести пройдено")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    try:
        n_fact = int(input().strip())
        print(factorial(n_fact))
        n_fib = int(input().strip())
        print(fibonacci(n_fib))
        lst = [float(x) for x in input().strip().split()]
        print(recursive_sum(lst))
        s = input().strip()
        print(is_palindrome(s))
    except Exception as e:
        print(f"Помилка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()