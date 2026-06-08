def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_cmyk(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    k = 1.0 - max(r, g, b)
    if k == 1.0:
        return 0.0, 0.0, 0.0, 1.0
    c = (1.0 - r - k) / (1.0 - k)
    m = (1.0 - g - k) / (1.0 - k)
    y = (1.0 - b - k) / (1.0 - k)
    return c, m, y, k

def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    l = (mx + mn) / 2.0
    if df == 0:
        h = s = 0.0
    else:
        s = df / (2.0 - mx - mn) if l > 0.5 else df / (mx + mn)
        if mx == r:
            h = (g - b) / df + (6.0 if g < b else 0.0)
        elif mx == g:
            h = (b - r) / df + 2.0
        else:
            h = (r - g) / df + 4.0
        h /= 6.0
    return h * 360.0, s * 100.0, l * 100.0

def main():
    hex_color = input().strip()
    r, g, b = hex_to_rgb(hex_color)
    c, m, y, k = rgb_to_cmyk(r, g, b)
    h, s, l = rgb_to_hsl(r, g, b)
    print(f"CMYK: C={c:.2f} M={m:.2f} Y={y:.2f} K={k:.2f}")
    print(f"HSL: H={h:.1f} S={s:.1f}% L={l:.1f}%")

if __name__ == "__main__":
    main()