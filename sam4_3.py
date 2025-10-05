import datetime
import time

def print_current_time():
    for i in range(5):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print(f"Текущее время: {formatted_time}")

        if i < 4:
            time.sleep(1)

if __name__ == '__main__':
    print_current_time()