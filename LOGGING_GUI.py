import os
import socket
import time
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import paramiko
from SSH_CONN import ssh_conn
from SCP_CONN import scp_conn


class Logging:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitoring")
        self.root.geometry("600x550")


        title = Label(root, text="Monitoring", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=550, height=430)


        lbl_ip = Label(Manage_Frame, text="Enter IP Address:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_ip.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        ip_input = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief = GROOVE)
        ip_input.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_user = Label(Manage_Frame, text="Enter Username:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_user.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        user_input = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        user_input.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_pwd = Label(Manage_Frame, text="Enter Password:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_pwd.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        pwd_input = Entry(Manage_Frame, show="*", font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        pwd_input.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_path = Label(Manage_Frame, text="Enter the path for monitoring", bg="grey", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_path.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        lbl_path_eg = Label(Manage_Frame, text="\n\n\neg.: C:/Users/Teszt/Documents/", bg="grey", fg="purple",
                         font=("times new roman", 12))
        lbl_path_eg.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        path_input = Entry(Manage_Frame, font=("times new roman", 15), bd=5, relief=GROOVE)

        path_input.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_monitoring_time = Label(Manage_Frame, text="Enter time in sec:", bg="grey", fg="white",
                            font=("times new roman", 15, "bold"))
        lbl_monitoring_time.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        monitoring_time_input = Entry(Manage_Frame, font=("times new roman", 15), bd=5, relief=GROOVE)

        monitoring_time_input.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_time = Label(Manage_Frame, bg="grey", fg="purple",
                            font=( 12))
        lbl_time.grid(row=7, column=0, pady=10, padx=20, sticky="w")


        def test_conn(ip, user, pwd, cmd):
            try:
                global running_check
                running_check = True
                print("Creating SSH Client..")
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print("Connection..")
                ssh_client.connect(hostname=ip, username=user, password=pwd)
                print("Command execution..")
                stdin, stdout, stderr = ssh_client.exec_command(cmd)
                time.sleep(5)
                print("Command executed..")
                stdout = stdout.readlines()
                print(stdout)
                ssh_client.close()

            except paramiko.ssh_exception.AuthenticationException :
                messagebox.showerror('Error', f"Username:{user_input.get()} or password invalid!\nGive correct data!")
                running_check = False

            except socket.gaierror:
                messagebox.showerror('Error', f"{ip_input.get()} invalid! Give correct address!")
                running_check = False

            except:
                e = sys.exc_info()
                messagebox.showerror('Error', f"Unexpected error: {e}")
                running_check = False


        def get_info():
            if ip_input.index("end") != 0 and user_input.index("end") != 0 and pwd_input.index("end") != 0:
                if path_input.index("end") != 0:
                    if monitoring_time_input.index("end") != 0:
                        transfer_data = []
                        try:
                            transfer_data.append(path_input.get())
                            transfer_data.append((int(monitoring_time_input.get())))
                            test_conn(ip_input.get(), user_input.get(), pwd_input.get(), "echo")
                            with open("C:/Users/Device_tools/Devicetools/moduls/logging.txt", "w") as filehandle:
                                for listitem in transfer_data:
                                    filehandle.write(f"{listitem}\n")
                            if running_check == True:
                                scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "put", "Logging_host.py")
                                scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "put", "logging.txt")
                                ssh_conn(ip_input.get(), user_input.get(), pwd_input.get(),
                                         f"python C:/Users/Device_tools/Devicetools/Logging_host.py")
                                messagebox.showinfo('Info', f"Successfully started monitoring: {path_input.get()}!")
                                get_time()
                                global monitor_check
                                monitor_check = True
                        except ValueError:
                            messagebox.showerror('Error', f"Time must be number!")
                    else:
                        messagebox.showwarning('Warning', "Enter time!")
                else:
                    messagebox.showwarning('Warning', "Enter the path!")
            else:
                messagebox.showwarning('Warning', "IP Address, Username and Password are required!")


        def open_info():
            try:
                if monitor_check == True:
                    scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "get", "log_info.log")
                    os.system('python FILE_OPENER.py')
                else:
                    pass
            except:
                messagebox.showwarning('Warning', "Run the module first!")


        #Time until get the log file
        # added_time= int(monitoring_time_input.get())

        import datetime

        def get_time():
            tm = datetime.datetime.now().time()
            added_time = int(monitoring_time_input.get())
            secs = added_time

            fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
            fulldate = fulldate + datetime.timedelta(seconds=secs)
            lbl_time.config(text=f"Monitoring until: {fulldate.time()}", bg="black")
            return fulldate.time()


        # Button frame
        getbtn = Button(Manage_Frame, text="Progress",
                           bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                           command= lambda: get_info())
        getbtn.grid(row=7, column=1, padx=20, pady=10, sticky="w")


        addedbtn = Button(Manage_Frame, text="Open",
                          bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                          command=lambda: open_info())
        addedbtn.grid(row=7, column=1, padx=120, pady=10, sticky="w")


root = Tk()
ob = Logging(root)
root.mainloop()