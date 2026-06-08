import threading
import time
import random


def countdown():
    print("\n[Потік 1] Початок відліку:")
    for i in range(10, 0, -1):
        print(f"Відлік: {i}")
        time.sleep(1)
    print("[Потік 1] Відлік завершено!")


def download_file(file_id):
    sleep_time = random.randint(3, 5)
    print(f"[Потік 2] Файл {file_id} почав завантаження (займе {sleep_time} сек)...")
    time.sleep(sleep_time)
    print(f"[Потік 2] Файл {file_id} успішно завантажено!")



results = []

def calculate_partial_sum(chunk, thread_id):
    partial_sum = sum(chunk)
    results.append(partial_sum)
    print(f"[Потік 3] Частина {thread_id} обчислена. Локальна сума: {partial_sum}")


if __name__ == "__main__":
  
    t1 = threading.Thread(target=countdown)
    t1.start()
    t1.join()  


    print("\n--- Старт завантаження файлів ---")
    download_threads = []
    for i in range(1, 4):
        t = threading.Thread(target=download_file, args=(i,))
        download_threads.append(t)
        t.start()

    for t in download_threads:
        t.join()  

   
    print("\n--- Старт обчислення суми ---")
    random_numbers = [random.randint(1, 100) for _ in range(1000)]
    
    
    chunk_size = 250
    chunks = [random_numbers[i:i + chunk_size] for i in range(0, 1000, chunk_size)]
    
    sum_threads = []
    for i, chunk in enumerate(chunks):
        t = threading.Thread(target=calculate_partial_sum, args=(chunk, i+1))
        sum_threads.append(t)
        t.start()

    for t in sum_threads:
        t.join()  

    total_sum = sum(results)
    actual_sum = sum(random_numbers)
    print(f"Загальна сума з потоків: {total_sum}")
    print(f"Перевірка (звичайна сума): {actual_sum}")