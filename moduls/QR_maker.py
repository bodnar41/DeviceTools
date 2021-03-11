import qrcode
import platform
import psutil
#import pynvml as nvml

#OS and client name
uname = platform.uname()
clientname= uname.node.strip("-PC")

# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")

# let's print CPU information
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")
# number of cores
# print("Total cores:", psutil.cpu_count(logical=True))

# CPU frequencies
cpufreq = psutil.cpu_freq()
# print(f"Max Frequency: {cpufreq.max:.2f}Mhz")

#RAM info
# print("Memory info")
total = round(psutil.virtual_memory().total * (9.91*10**-10))
# print(f"{total} GB")

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# print("Partitions and Usage:")
# get all disk partitions

partitions = psutil.disk_partitions()
disks = {}

for partition in partitions:
    # print(f"Device: {partition.device} ===")
    # print(f"File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that isn't ready
        continue
    # print(f"Total Size: {get_size(partition_usage.total)}")
    disks[partition.device] = get_size(partition_usage.total)

# nvml.nvmlInit()
#
# #print(f"Number of devices: {nvml.nvmlDeviceGetCount()}")
# handle = nvml.nvmlDeviceGetHandleByIndex(0)
# info = nvml.nvmlDeviceGetMemoryInfo(handle)
# total_mem = info.total
# total_mem = total_mem / (1024*1024)
# #print(f"Total size: {total_mem} MB")
#
# deviceCount = nvml.nvmlDeviceGetCount()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(f"System: {uname.system}\nRelease: {uname.release}\nClient Name: {uname.node}\n"
            f"CPU: {uname.machine}\nCPU Type: {uname.processor}\nTotal cores: {psutil.cpu_count(logical=True)}\n"
            f"Max Frequency: {cpufreq.max:.2f}Mhz\nMemory: {total} GB\n"
            )

for key in disks:
    qr.add_data(f"Device: {key}\nTotal size: {disks[key]}\n")

# qr.add_data(f"GPU devices: {nvml.nvmlDeviceGetCount()}\nTotal size: {total_mem} MB\n")
# for i in range(deviceCount):
#     info = str((nvml.nvmlDeviceGetName(handle)))
#     info = info.replace("b", "").replace("'", "").strip()
#     #print(f"Device{i}: {info}")
#     qr.add_data(f"Device{i}: {info}")

qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save(f"C:/Users/{clientname}/sysinfo.png")

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"C:/Users/Device_tools/Devicetools/sysinfo.png")