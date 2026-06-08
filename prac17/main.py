from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats

def main():
    print("=== Демонстрація Календаря ===")
    cal = UkrainianCalendar()
    print("Свята:", cal.get_holiday_list())
    date = "24-08-2024"
    print(f"Чи є {date} робочим днем? - {cal.is_working_day(date)}")

    print("\n=== Демонстрація Аналізу Тексту ===")
    user_text = input("Введіть текст для аналізу: ")
    stats = TextStats(user_text)
    print(f"Кількість слів: {stats.count_words()}")
    print(f"Найчастіша літера: {stats.most_common_letter()}")

    print("\n=== Демонстрація Калькулятора ===")
    calc = Calculator()
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        op = input("Оберіть операцію (+, -, *, /): ")
        
        if op == '+': print("Результат:", calc.add(a, b))
        elif op == '-': print("Результат:", calc.subtract(a, b))
        elif op == '*': print("Результат:", calc.multiply(a, b))
        elif op == '/': print("Результат:", calc.divide(a, b))
        else: print("Невідома операція.")
    except ValueError as e:
        print("Помилка вводу або обчислення:", e)

if __name__ == "__main__":
    main()