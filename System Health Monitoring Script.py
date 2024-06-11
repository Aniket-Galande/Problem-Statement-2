import psutil
import datetime
import time

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEM_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Define log file
LOG_FILE = "system_health.log"

def send_alert(message):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - ALERT: {message}\n")
    print(f"ALERT: {message}")

def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        send_alert(f"CPU usage is {cpu_percent}%, which exceeds {CPU_THRESHOLD}% threshold.")

def check_memory():
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    if mem_percent > MEM_THRESHOLD:
        send_alert(f"Memory usage is {mem_percent}%, which exceeds {MEM_THRESHOLD}% threshold.")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > DISK_THRESHOLD:
        send_alert(f"Disk usage is {disk_percent}%, which exceeds {DISK_THRESHOLD}% threshold.")

def check_processes():
    processes = psutil.process_iter()
    for process in processes:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            if process_info['cpu_percent'] > CPU_THRESHOLD or process_info['memory_percent'] > MEM_THRESHOLD:
                send_alert(f"Process '{process_info['name']}' (PID: {process_info['pid']}) is consuming excessive resources.")
        except psutil.NoSuchProcess:
            pass

if __name__ == "__main__":
    # Clear log file
    open(LOG_FILE, 'w').close()
    
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        # Check system health every 5 minutes
        time.sleep(300)
