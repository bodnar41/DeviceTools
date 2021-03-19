from tkinter import *
import socket
import sys
import paramiko, time
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

class Transfer():
    def __init__(self, root):
        self.root = root
        self.root.title('File transfer')
        self.root.geometry("815x520")

        title = Label(root, text="File transfer", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=770, height=400)


        lbl_ip = Label(Manage_Frame, text="Enter IP Address:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_ip.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        ip_input = Entry(Manage_Frame, font=("times new roman", 15, "bold"), width = 30, bd=5, relief = GROOVE)
        ip_input.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_user = Label(Manage_Frame, text="Enter Username:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_user.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        user_input = Entry(Manage_Frame, font=("times new roman", 15, "bold"), width = 30, bd=5, relief=GROOVE)
        user_input.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_pwd = Label(Manage_Frame, text="Enter Password:", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_pwd.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        pwd_input = Entry(Manage_Frame, show="*", font=("times new roman", 15, "bold"), width = 30, bd=5, relief=GROOVE)
        pwd_input.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_path = Label(Manage_Frame, text="Choose a file:", bg="grey", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_path.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        lbl_path_message = Label(Manage_Frame, text=None, bg="grey", fg="white",
                         font=("times new roman", 8, "bold"))
        lbl_path_message.grid(row=7, column=1, pady=5, padx=20, sticky="w")

        lbl_output = Label(Manage_Frame, text="Enter output name with extension:", bg="grey", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_output.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        output_input = Entry(Manage_Frame, font=("times new roman", 15, "bold"), width = 30, bd=5, relief=GROOVE)
        output_input.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        lbl_outplace = Label(Manage_Frame, text="Will be transferred to User's home", bg="grey", fg="white",
                           font=("times new roman", 10, "bold"))
        lbl_outplace.grid(row=9, column=1, pady=10, padx=20, sticky="w")


        def choosen():
            choosen.chosen_file = filedialog.askopenfilename(initialdir="C:/Users/Device_tools/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.txt*"),
                                                         ("all files",
                                                          "*.*")))
            lbl_path_message.configure(text="Chosen file: " + choosen.chosen_file)

        def scp_conn(ip, user, pwd, filename):
                if ip_input.index("end") != 0 and user_input.index("end") != 0 and pwd_input.index("end") != 0:
                    if output_input.index("end") != 0:
                        try:
                            print("Creating SSH Client..")
                            ssh_client = paramiko.SSHClient()
                            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            ssh_client.connect(hostname=ip, username=user, password=pwd)
                            sftp_client = ssh_client.open_sftp()
                            print("File transferring")

                            sftp_client.put(filename, f"C:/Users/{user}/{output_input.get()}")
                            messagebox.showinfo("Error", f"File successfully transferred as {output_input.get()}")
                            sftp_client.close()
                            ssh_client.close()
                        except paramiko.ssh_exception.AuthenticationException:
                            messagebox.showerror("Error", f"Username:{user_input.get()} or password invalid!\nGive correct data!")
                        except FileNotFoundError:
                            messagebox.showerror("Error", f"{choosen().get()} invalid!\nGive correct path!")
                        except socket.gaierror:
                            messagebox.showerror("Error", f"{ip_input.get()} invalid! Give correct address!")
                        except:
                            messagebox.showerror("Error", f"Unexpected error!")
                    else:
                        messagebox.showwarning("Warning", "Output name is required!")
                else:
                    messagebox.showwarning("Warning", "IP Address, Username and Password are required!")


        def check():
            try:
                scp_conn(ip_input.get(), user_input.get(), pwd_input.get(),
                                                 choosen.chosen_file)
            except AttributeError:
                messagebox.showwarning("Warning", "Choose a file first!")

        # Button frame
        button_explore = Button(Manage_Frame,
                                text="Browse",
                                command= lambda: choosen())
        button_explore.grid(row=6, column=1, padx=100, pady=10, sticky="w")

        testbtn = Button(Manage_Frame, text="Transfer",
                         bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                         command=lambda: check())

        testbtn.grid(row=10, column=1, padx=20, pady=10, sticky="w")


root = Tk()
ob = Transfer(root)
root.mainloop()