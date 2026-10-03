import time
import threading


def print_message(message, delay):
    time.sleep(delay)
    print(message)

#Без потоков
def run_norm(delay):
    print_message("Первый mess", delay)
    print_message("Второй mess", delay)
    print_message("Третий mess", delay)

#Отдельные потоки
def run_threads(delay):
    threads = [
        threading.Thread(target=print_message, args=("Первый mess", delay)),
        threading.Thread(target=print_message, args=("Второй mess", delay)),
        threading.Thread(target=print_message, args=("Третий mess", delay))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start = time.perf_counter()
    run_norm(2)
    end = time.perf_counter()
    print(f"Время последовательного выполнения: {end - start} сек\n")

    start = time.perf_counter()
    run_threads(2)
    end = time.perf_counter()

    print(f"Время выполнения с потоками: {end - start} сек.")