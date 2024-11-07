import time
import multiprocessing

def read_info(name):
    all_data = []
    try:
        with open(name, "r", encoding='utf-8') as file:
            for line in file:
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    return all_data


if __name__ == '__main__':
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start_time = time.time()
    for file in files:
        func = read_info(file)
    stop_time = time.time()
    timer = stop_time - start_time
    print(timer, "(линейный)")

    start_time = time.time()
    with multiprocessing.Pool(processes= 4) as pool:
        pool.map(read_info, files)
    stop_time = time.time()
    timer = stop_time - start_time
    print(timer, "(многопроцессный)")