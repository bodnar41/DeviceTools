import os
import platform
from tkinter import *
from tkinter import ttk, messagebox
from time import strftime
import datetime as dt
import getpass
import psutil


class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Sysadmin Tools")
        self.root.geometry("740x510")

        #Host's infos
        uname = platform.uname()
        clientname = uname.node.strip("-PC")
        username = getpass.getuser()
        cpufreq = psutil.cpu_freq()

        partitions = psutil.disk_partitions()
        disks = {}

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
                    return f"{bytes:.2f} {unit}{suffix}"
                bytes /= factor

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

        # RAM info
        # print("Memory info")
        total = round(psutil.virtual_memory().total * (9.91 * 10 ** -10))

        title = Label(root, text=f"Welcome {username}!", bd=5, relief=GROOVE, font=("times new roman", 20, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=460, height=350)


        combo_type = ttk.Combobox(Manage_Frame, font=("times new roman", 10), width=40, state="readonly")
        combo_type.set('Choose an option!')
        combo_type['values'] = ("1. Test SSH connection", "2. Test File Transferring with SCP", "3. Get System Information from a remote Host",
                                "4. Encrypt/Decrypt a file", "5. Monitor a remote host", "6. Device Management System")
        combo_type.grid(row=1, column=0, pady=10, padx=20, sticky="w")


        Data_Frame = Frame(root, bd=0, relief=RIDGE, bg="white")
        Data_Frame.place(x=575, y=450, width=145, height=25)

        Detail_Frame = Frame(root, bd=4, relief=RIDGE, bg="lightgrey")
        Detail_Frame.place(x=350, y=100, width=370, height=350)

        Detail_datas_Frame = Frame(root, bd=4, relief=RIDGE, bg="lightgrey")
        Detail_datas_Frame.place(x=350, y=130, width=370, height=320)

        Description_Frame = Frame(root, bd=0, relief=RIDGE, bg="grey")
        Description_Frame.place(x=25, y=200, width=310, height=200)

        Description_Frame.text = Text(Description_Frame, bd=0, relief=RIDGE, bg="grey", font=("times new roman", 10))
        Description_Frame.text.pack(side=BOTTOM, fill=X)

        default_text = "Use the app to make your work faster and more efficient.\n" \
                       "You can choose from 7 different functions using the " \
                       "drop-down menu. After selected one, click *?* and you will\n" \
                       " see a brief introduction about the feature."

        ssh_text = "Use this feature to test the SSH connection is working\n" \
                   "properly. Add Host IP Adrress, Username and Password\n" \
                   "and the function test it. If the test is successfull\n" \
                   "You will get a feedback."

        scp_text = "Use this function to test the File Transferring is working\n" \
                   "properly.Add Host IP Adrress, Username and Password,\n" \
                   "select Action (Put or Get), then select a File and the\n" \
                   "function Put/Get it. If the progress is successfull You will get a feedback."

        sysinfo_text = "Use this feature to get information from a remote Host.\n" \
                       "Add Host IP Adrress, Username and Password select\n" \
                       "what kind of info You want.With Get Info button You\n" \
                       "received the selected info in .json file. With Get QR\n" \
                       "received a QR code from infos. If the progress is\n" \
                       "successfull You will be able to open the received file(s)."

        encryption_text = "Use this function to encrypt/decrypt a file on your local\n" \
                          "system.Open a file select Action (Encrypt or Decrypt),\n" \
                          "then enter a Key as number! If the progress is successfull\n" \
                          "Your file will be encrypt/decrypt."

        monitor_text = "Use this function to monitor a folder or an entire disk on\n" \
                       "remote host. Enter the path and enter the time in sec. The monitoring will take place until the given time.\n" \
                        "If the progress is successfull, You will get a log file with\n" \
                       "the informations."

        mgmt_text = "Use this function to store devices. With this device\n" \
                    "management, You can get an overview about the\n" \
                    "guarantee status of devices. You will get an email alert\n" \
                    "when the expiration day of guarantee less than 60 days.\n" \
                    "You can add, edit and delete devices and search by\n" \
                    "different filters." \


        def show_desc():
            choice = combo_type.get().split(".")
            if choice[0] == "1":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, ssh_text)
            elif choice[0] == "2":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, scp_text)
            elif choice[0] == "3":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, sysinfo_text)
            elif choice[0] == "4":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, encryption_text)
            elif choice[0] == "5":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, monitor_text)
            elif choice[0] == "6":
                if Description_Frame.text != None:
                    Description_Frame.text.delete(0.0, END)
                    Description_Frame.text.insert(END, mgmt_text)

            else:
                Description_Frame.text.delete(0.0, END)
                Description_Frame.text.insert(END, default_text)

        show_desc()

        title = Label(Detail_Frame, text=f"Your host's info:", bd=5, relief=GROOVE, font=("arial", 10, "bold"),
                      bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        lbl_client_name = Label(Detail_datas_Frame, text=f"Client Name: {uname.node}", bg="lightgrey", fg="black",
                         font=("times new roman", 10, "bold"))
        lbl_client_name.grid(row=1, column=0, pady=2, padx=0, sticky="w")

        lbl_system = Label(Detail_datas_Frame, text=f"System: {uname.system}", bg="lightgrey", fg="black",
                             font=("times new roman", 10, "bold"))
        lbl_system.grid(row=2, column=0, pady=2, padx=0, sticky="w")

        lbl_release = Label(Detail_datas_Frame, text=f"Release: {uname.release}", bg="lightgrey", fg="black",
                             font=("times new roman", 10, "bold"))
        lbl_release.grid(row=3, column=0, pady=2, padx=0, sticky="w")

        lbl_cpu = Label(Detail_datas_Frame, text=f"CPU: {uname.machine}", bg="lightgrey", fg="black",
                             font=("times new roman", 10, "bold"))
        lbl_cpu.grid(row=4, column=0, pady=2, padx=0, sticky="w")

        lbl_cpu_type = Label(Detail_datas_Frame, text=f"CPU Type:{uname.processor}", bg="lightgrey", fg="black",
                        font=("times new roman", 10, "bold"))
        lbl_cpu_type.grid(row=5, column=0, pady=2, padx=0, sticky="w")

        lbl_cores = Label(Detail_datas_Frame, text=f"Total Cores: {psutil.cpu_count(logical=True)}", bg="lightgrey", fg="black",
                        font=("times new roman", 10, "bold"))
        lbl_cores.grid(row=6, column=0, pady=2, padx=0, sticky="w")

        lbl_freq = Label(Detail_datas_Frame, text=f"Max Frequency: {cpufreq.max:.2f} Mhz", bg="lightgrey",
                          fg="black",
                          font=("times new roman", 10, "bold"))
        lbl_freq.grid(row=7, column=0, pady=2, padx=0, sticky="w")

        lbl_mem = Label(Detail_datas_Frame, text=f"Memory: {total} GB", bg="lightgrey",
                         fg="black",
                         font=("times new roman", 10, "bold"))
        lbl_mem.grid(row=8, column=0, pady=2, padx=0, sticky="w")


        def device_info():
            row_id = 9
            for key in disks:
                lbl_disk = Label(Detail_datas_Frame, text=f"Device: {key}"
                                                          f"\tTotal size: {disks[key]}", bg="lightgrey",
                             fg="black",
                             font=("times new roman", 10, "bold"))
                lbl_disk.grid(row=row_id, column=0, pady=2, padx=0, sticky="w")
                row_id +=1
        device_info()


        lbl_clock = Label(Data_Frame, font=('helvetica', 8, 'bold'),
                          background='purple',
                          foreground='white', )

        lbl_clock.grid(row=0, column=2, padx=0, pady=2)


        lbl_date = Label(Data_Frame, text=f"{dt.datetime.now():%a, %b %d. %Y}",
                         fg="white", bg="black", font=("helvetica", 8))
        lbl_date.grid(row=0, column=1, padx=0, pady=2)

        def progressing():
            choice = combo_type.get().split(".")
            if choice[0] == "1":
                os.system('python SSH_CONN_GUI.py')
            elif choice[0] == "2":
                os.system('python SCP_CONN_GUI.py')
            elif choice[0] == "3":
                os.system('python SYSINFO_GUI.py')
            elif choice[0] == "4":
                os.system('python ENCRYPTION_GUI.py')
            elif choice[0] == "5":
                os.system('python LOGGING_GUI.py')
            elif choice[0] == "6":
                os.system('python DEVICE_MGMT.py')
            else:
                pass


        def time():
            string = strftime('%H:%M:%S')
            lbl_clock.config(text=string)
            lbl_clock.after(1000, time)

        # Button frame
        infobtn = Button(Manage_Frame, text="?",
                            bg="lightblue", fg="black", font=("times new roman", 7),
                            command=lambda: show_desc())
        infobtn.grid(row=1, column=0, padx=300, pady=0, sticky="w")

        progressbtn = Button(Manage_Frame, text="Progress",
                         bg="lightblue", fg="black", font=("times new roman", 10),
                         command=lambda: progressing())
        progressbtn.grid(row=2, column=0, padx=150, pady=5, sticky="w")

        time()


root = Tk()
ob = Home(root)

root.mainloop()