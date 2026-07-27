import psutil
import platform
import datetime

# ==========================================
# CPU FUNCTIONS
# ==========================================

def cpu_usage():
    print(f"CPU Usage : {psutil.cpu_percent(interval=1)} %")

def cpu_cores():
    print(f"Physical Cores : {psutil.cpu_count(logical=False)}")
    print(f"Total Cores : {psutil.cpu_count(logical=True)}")

def cpu_frequency():
    freq = psutil.cpu_freq()

    print(f"Current : {freq.current:.2f} MHz")
    print(f"Minimum : {freq.min:.2f} MHz")
    print(f"Maximum : {freq.max:.2f} MHz")

# ==========================================
# RAM FUNCTIONS
# ==========================================

def ram_usage():

    ram = psutil.virtual_memory()

    print(f"Total RAM : {round(ram.total/1024**3,2)} GB")
    print(f"Available : {round(ram.available/1024**3,2)} GB")
    print(f"Used : {round(ram.used/1024**3,2)} GB")
    print(f"RAM Usage : {ram.percent} %")

def swap_memory():

    swap = psutil.swap_memory()

    print(f"Total Swap : {round(swap.total/1024**3,2)} GB")
    print(f"Used Swap : {round(swap.used/1024**3,2)} GB")
    print(f"Swap Usage : {swap.percent} %")

# ==========================================
# DISK FUNCTIONS
# ==========================================

def disk_usage():

    disk = psutil.disk_usage("/")

    print(f"Total Disk : {round(disk.total/1024**3,2)} GB")
    print(f"Used Disk : {round(disk.used/1024**3,2)} GB")
    print(f"Free Disk : {round(disk.free/1024**3,2)} GB")
    print(f"Disk Usage : {disk.percent} %")

def disk_partitions():

    partitions = psutil.disk_partitions()

    for partition in partitions:

        print("----------------------------------")
        print("Device :", partition.device)
        print("Mount :", partition.mountpoint)
        print("File System :", partition.fstype)

# ==========================================
# BATTERY FUNCTIONS
# ==========================================

def battery_percentage():

    battery = psutil.sensors_battery()

    if battery:

        print(f"Battery : {battery.percent}%")

    else:

        print("Battery Not Available")

def battery_status():

    battery = psutil.sensors_battery()

    if battery:

        if battery.power_plugged:

            print("Charging")

        else:

            print("Not Charging")

    else:

        print("Battery Not Available")

# ==========================================
# SYSTEM INFORMATION
# ==========================================

def boot_time():

    boot = datetime.datetime.fromtimestamp(psutil.boot_time())

    print("Boot Time :", boot.strftime("%d-%m-%Y %I:%M:%S %p"))

def uptime():

    boot = datetime.datetime.fromtimestamp(psutil.boot_time())

    now = datetime.datetime.now()

    print("System Uptime :", now-boot)

def system_information():

    print("System :", platform.system())
    print("Node :", platform.node())
    print("Release :", platform.release())
    print("Version :", platform.version())
    print("Machine :", platform.machine())
    print("Processor :", platform.processor())

# ==========================================
# LIVE CPU MONITOR
# ==========================================

def live_cpu():

    while True:

        print(f"CPU : {psutil.cpu_percent()} %")