import sys

def rle_encode(s):
    if not s: return ""
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        res.append(f"{count}{s[i]}")
        i += 1
    return "".join(res)

def rle_decode(s):
    res = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        res.append(s[i] * int(count_str))
        i += 1
    return "".join(res)

def run_tests():
    assert rle_encode("AAAAABBBCC") == "5A3B2C"
    assert rle_decode("5A3B2C") == "AAAAABBBCC"
    print("Тести пройдено")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
        return
    orig = input().strip()
    comp = rle_encode(orig)
    decomp = rle_decode(comp)
    pct = ((len(orig) - len(comp)) / len(orig)) * 100 if len(orig) > 0 else 0
    print(comp)
    print(f"{pct:.2f}%")
    print(decomp)

if __name__ == "__main__":
    main()