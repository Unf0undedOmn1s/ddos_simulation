# monitoring.py
import psutil
import time

def log_system_usage():
    with open('system_usage.log', 'a') as f:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent
            f.write(f"CPU: {cpu_usage}%, Memory: {mem_usage}%\n")
            time.sleep(5)

if __name__ == '__main__':
    log_system_usage()
