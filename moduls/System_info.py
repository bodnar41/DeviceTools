import platform, psutil
from datetime import datetime
import json
import paramiko

# Client name
uname = platform.uname()
clientname= uname.node.strip('-PC')

# Opening the file which contains the instrucs
received_data = []
with open(f"C:/Users/Device_tools/Devicetools/teszt.txt", 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        received_data.append(currentPlace)

choice = received_data[0]
user = received_data[1]
# print(choice)

if choice == "1.":
    uname = platform.uname()
    sysinfo = {"System info": [
        {"System": uname.system, "Node Name": uname.node, "Release": uname.release, "Version": uname.version,
         "Machine": uname.machine, "Processor": uname.processor}]}
    sysJSON = json.dumps(sysinfo, indent=4, sort_keys=True)


elif choice == "2.":
    sysinfo = {"CPU info": [
        {"Physical cores": psutil.cpu_count(logical=False), "Total cores": psutil.cpu_count(logical=True)}]}
    cpuJSON = json.dumps(sysinfo, indent=4, sort_keys=True)


elif choice == "3.":
    cpufreq = psutil.cpu_freq()
    sysinfo = {"Frequency info": [
        {"Max Frequency": str(cpufreq.max) + " Mhz", "Min Frequency": str(cpufreq.min) + " Mhz",
         "Current Frequency": str(cpufreq.current) + " Mhz"}]}
    freqJSON = json.dumps(sysinfo, indent=4, sort_keys=True)


elif choice == "4.":
    core = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=2)):
        core.append(percentage)

    data3 = psutil.cpu_percent()
    length = len(core)
    sysinfo = {"Core info": []}

    for i in range(length):
        sysinfo["Core info"].append({'Core' + str(i): str(core[i]) + "%"})
    sysinfo["Core info"].append({'Full usage': str(data3) + "%"})
    coreJSON = json.dumps(sysinfo, indent=4, sort_keys=True)


with open(f"C:/Users/Device_tools/Devicetools/system_info.json", "w") as file:
    json.dump(sysinfo, file, indent=4)

