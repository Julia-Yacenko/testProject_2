import time
import threading
import psutil
import pandas as pd

def get_CPU(ar_time, ar_name, ar_val):
    while True:
        ar_time.append(f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")
        ar_val.append(psutil.cpu_percent())
        ar_name.append("CPU")
        time.sleep(60)

def get_RAM(ar_time, ar_name, ar_val):
    while True:
        ar_time.append(f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")
        ar_val.append(psutil.virtual_memory().percent)
        ar_name.append("RAM")
        time.sleep(60)

if __name__ == '__main__':
    ar_time = list()
    ar_name = list()
    ar_val = list()

    t_1 = threading.Thread(target=get_CPU, args=(ar_time, ar_name, ar_val), daemon=True)
    t_2 = threading.Thread(target=get_RAM, args=(ar_time, ar_name, ar_val), daemon=True)
    t_1.start()
    t_2.start()

    stop_time = time.time() + 130
    while time.time() < stop_time:
        a = 0

    t_1.join()
    t_2.join()

    table = pd.DataFrame({"Время": ar_time, "Название метрики": ar_name, "Значение": ar_val})
    table.to_csv("data.csv", sep = ";")
