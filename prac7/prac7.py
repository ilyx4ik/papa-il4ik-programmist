def draw_graph():
    try:
        start = float(input("Введіть початок проміжку (від): "))
        end = float(input("Введіть кінець проміжку (до): "))
        step = float(input("Введіть крок ітерування: "))
    except ValueError:
        print("Помилка: введіть коректні числа.")
        return

    if step <= 0 or start >= end:
        print("Помилка: неправильно задано проміжок або крок.")
        return

    def f(x):
        return int(round(x**2 - 4))

    points = []
    current_x = start
    
    while current_x <= end:
        x_coord = int(round(current_x))
        y_coord = f(current_x)
        points.append((x_coord, y_coord))
        current_x += step

    if not points:
        print("Немає точок для побудови.")
        return

    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    min_y, max_y = min_y - 1, max_y + 1

    for y in range(max_y, min_y - 1, -1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                line += "*"  
            elif x == 0 and y == 0:
                line += "+"  
            elif x == 0:
                line += "|"  
            elif y == 0:
                line += "-"  
            else:
                line += " "  
        print(line)

if __name__ == "__main__":
    draw_graph()