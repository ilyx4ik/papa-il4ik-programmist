import sys

def count_letters(s):
    stats = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            stats[char_lower] = stats.get(char_lower, 0) + 1
    return stats

def run_tests():
    assert count_letters("Hello!") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print("Тести пройдено")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    s = sys.stdin.read()
    stats = count_letters(s)
    for k, v in sorted(stats.items()):
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()