import os
import socket
import time
from tkinter import *
from tkinter import ttk, messagebox
import paramiko
from SSH_CONN import ssh_conn
from SCP_CONN import scp_conn

class Device:
    def __init__(self, root):
        self.root = root
        self.root.title("System Info")
        self.root.geometry("600x520")


        title = Label(root, text="System Info", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=550, height=380)

        answer = Label(Manage_Frame, text=None, bg="grey", fg="white", font=("times new roman", 12))
        answer.grid(row=7, column=1, padx=10)


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

        lbl_infotype = Label(Manage_Frame, text="Select tpye of info:", bg="grey", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_infotype.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_type  = ttk.Combobox(Manage_Frame, font=("times new roman", 15, "bold"), width = 18, state="readonly")
        combo_type['values'] = ("1. System info", "2. CPU info", "3. Frequency info", "4. Core info")
        combo_type.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        cmd_input = "echo"

        def test_conn(ip=None, user=None, pwd=None, cmd=None):
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
                time.sleep(2)
                print("Command executed..")
                stdout = stdout.readlines()
                print(stdout)
                ssh_client.close()

            except paramiko.ssh_exception.AuthenticationException as e:
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
            if ip_input.index("end") != 0 and user_input.index("end") !=0 and pwd_input.index("end") != 0:
                if combo_type.index("end") != 0:
                    splitted_type = combo_type.get().split(" ")
                    transfer_data = [splitted_type[0], user_input.get()]
                    test_conn(ip_input.get(), user_input.get(), pwd_input.get(), "echo")
                    with open("C:/Users/teszt/Device tools/moduls/info.txt", "w") as filehandle:
                        for listitem in transfer_data:
                            filehandle.write(f"{listitem}\n")
                    if running_check == True:

                            scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "put", "System_info.py")
                            scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "put", "info.txt")
                            ssh_conn(ip_input.get(), user_input.get(), pwd_input.get(), f"python C:/Users/Device_tools/Devicetools/System_info.py")

                            messagebox.showinfo('Info', f"Successfully got info from {user_input.get()}")
                            addedbtn = Button(Manage_Frame, text="Open",
                                              bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                                              command=lambda: open_info())
                            addedbtn.grid(row=5, column=1, padx=100, pady=10, sticky="w")
                    else:
                        messagebox.showerror('Error', "Authentication error!")
                else:
                    messagebox.showwarning('Warning', "Select the type of info!")
            else:
                messagebox.showwarning('Warning', "IP Address, Username and Password are required!")

        def open_info():
            scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "get", "system_info.json")
            os.system('python FILE_OPENER.py')

        def open_qr():
            scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "get", "sysinfo.png")
            try:
                from PIL import Image
                Image.open("C:/Users/teszt/Device tools/data/sysinfo.png").show()
            except FileNotFoundError:
                messagebox.showerror('Error', "The sysinfo.png not found!")
            except:
                messagebox.showerror('Error', "Unexpected error!")
        def get_qr():
            if ip_input.get() and user_input.get() and pwd_input.get() != None:
                test_conn(ip_input.get(), user_input.get(), pwd_input.get(), "echo")
                if running_check == True:
                    scp_conn(ip_input.get(), user_input.get(), pwd_input.get(), "put", "QR_maker.py")
                    ssh_conn(ip_input.get(), user_input.get(), pwd_input.get(),
                             f"python C:/Users/Device_tools/Devicetools/QR_maker.py")
                    # answer.config(text=f"Successfully got QR code from {user_input.get()}!")
                    messagebox.showinfo('Info', f"Successfully got QR code from {user_input.get()}!")
                    addedbtn = Button(Manage_Frame, text="Open",
                                      bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                                      command=lambda: open_qr())
                    addedbtn.grid(row=6, column=1, padx=100, pady=10, sticky="w")
                else:
                    pass

            else:
                messagebox.showerror('Error', f"NO data!\nEnter the auth data!")


        # Button frame
        getbtn = Button(Manage_Frame, text="Get Info",
                           bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                           command= lambda: get_info())
        getbtn.grid(row=5, column=1, padx=20, pady=10, sticky="w")


        qrbtn = Button(Manage_Frame, text="Get QR",
                           bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                           command= lambda: get_qr())
        qrbtn.grid(row=6, column=1, padx=20, pady=10, sticky="w")


root = Tk()
ob = Device(root)

root.mainloop()