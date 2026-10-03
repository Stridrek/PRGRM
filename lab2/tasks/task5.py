import threading
import time

counter = 0

def increment():
    global counter
    for i in range(10000):
        temp = counter
        time.sleep(0.0000000000001)
        counter = temp + 1

threads = []

# 5 потоков
def run_threads():
    for x in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Ожидаемый результат:", 5 * 10_000)
    print("Настоящий результат:", counter)
    return counter

if __name__ == '__main__':
    run_threads()