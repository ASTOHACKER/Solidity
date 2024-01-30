from multiprocessing import Process
import os
import time

def num():
    for i in range(100):
        result = i * i 
        time.sleep(0.1)

if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        p = Process(target=num)
        processes.append(p)
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("END")