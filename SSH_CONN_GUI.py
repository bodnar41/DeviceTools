from tkinter import *
import socket
import sys
from tkinter import filedialog, messagebox

import paramiko, time
from tkinter import ttk

class SSH():
    def __init__(self, root):
        self.root = root
        self.root.title('SSH Teszt')
        self.root.geometry("600x400")
        def ssh_conn(ip = None, user = None, pwd = None, cmd = None):
            if ip_input.index("end") != 0 and user_input.index("end") != 0 and pwd_input.index("end") != 0:

                try:
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
                    # answer.config(text="")
                    # answer.config(text="SSH connection is OK!")
                    messagebox.showinfo("Info", "SSH connection is OK!")
                except paramiko.ssh_exception.AuthenticationException as e:
                    # print("Username: " + user + "\t or password invalid.")
                    # ssh_conn(ip_input.get(), None, None, cmd_input.get())
                    # answer.config(text=f"Username:{user_input.get()} or password invalid!\nGive correct datas!")
                    messagebox.showerror("Error", f"Username:{user_input.get()} or password invalid!\nEnter correct data!")


                except socket.gaierror:
                    # print(ip + " invalid.")
                    # ssh_conn(None, user_input.get(), pwd_input.get(), cmd_input.get())
                    # answer.config(text=f"{ip_input.get()} invalid! Give correct address!")
                    messagebox.showerror("Error", f"{ip_input.get()} invalid! Enter a correct address!")

                except:
                    e = sys.exc_info()
                    # answer.config(text=f"Unexpected error: {e}")
                    messagebox.showerror("Error", "Unexpected error: {e}")
            else:
                messagebox.showwarning("Warning","IP Address, Username and Password are required!")


        title = Label(self.root, text="SSH Teszt", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        SSH_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey")
        SSH_Frame.place(x=20, y=75, width=550, height=300)


        lbl_ip = Label(SSH_Frame, text="Enter IP Address:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_ip.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        ip_input = Entry(SSH_Frame, font=("times new roman", 15, "bold"), bd=5, relief = GROOVE)
        ip_input.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_user = Label(SSH_Frame, text="Enter Username:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_user.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        user_input = Entry(SSH_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        user_input.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_pwd = Label(SSH_Frame, text="Enter Password:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_pwd.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        pwd_input = Entry(SSH_Frame, show="*", font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        pwd_input.grid(row=3, column=1, pady=10, padx=20, sticky="w")


        cmd_input = "echo"

        # Button frame
        testbtn = Button(SSH_Frame, text="Test SSH",
                           bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                           command= lambda: ssh_conn(ip_input.get(), user_input.get(), pwd_input.get(), cmd_input))
        testbtn.grid(row=5, column=1, padx=10, pady=10, sticky="w")


        answer = Label(SSH_Frame, text=None, bg="grey", fg="white", font=("times new roman", 12))
        answer.grid(row=6, column=1, padx=10)



root = Tk()
ob = SSH(root)

root.mainloop()