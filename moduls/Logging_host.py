import platform
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Client name
uname = platform.uname()
clientname = uname.node.strip('-PC')

#O pening the file which contains the instrucs
received_data = []
with open("C:/Users/Device_tools/Devicetools/info.txt", 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        received_data.append(currentPlace)

given_path = received_data[0]
given_time = int(received_data[1])


# Set the format for logging info
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename= "C:/Users/Device_tools/Devicetools/log_info.log")


# Initializer logging event handler
event_handler = LoggingEventHandler()

# Initialize Observer
observer = Observer()
observer.schedule(event_handler, given_path, recursive=True)

# Start the Observer
observer.start()

# Time until the logger listen
time.sleep(given_time)

# Stop the Observer
observer.stop()

# Add to logfile
observer.join()
