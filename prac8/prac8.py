def rle_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)


def rle_decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""
    
    decoded = []
    count_str = ""
    
    for char in encoded_text:
        if char.isdigit():
            count_str += char  
        else:
            count = int(count_str) if count_str else 1
            decoded.append(char * count)
            count_str = ""
            
    return "".join(decoded)


def calculate_compression_percentage(original: str, compressed: str) -> float:
    if not original:
        return 0.0
    len_orig = len(original)
    len_comp = len(compressed)
    
    percentage = ((len_orig - len_comp) / len_orig) * 100
    return percentage


if __name__ == "__main__":
    print("--- Демонстрація роботи програми ---")
    input_string = input("Введіть рядок для стиснення: ")
    
    compressed_string = rle_encode(input_string)
    print(f"\nСтиснений рядок: {compressed_string}")
    
    comp_percent = calculate_compression_percentage(input_string, compressed_string)
    print(f"Довжина зменшилася на: {comp_percent:.2f}%")

    decompressed_string = rle_decode(compressed_string)
    print(f"Розтиснений рядок:  {decompressed_string}")
    
    assert input_string == decompressed_string, "Помилка! Дані втрачено!"
    print("Результат: Успішно відновлено 1-в-1.")