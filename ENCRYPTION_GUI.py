from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfile

class Device:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption")
        self.root.geometry("500x380")

        title = Label(root, text="Encryption", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=450, height=250)

        lbl_ip = Label(Manage_Frame, text="Open file", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_ip.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        lbl_infotype = Label(Manage_Frame, text="Select action", bg="grey", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_infotype.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        combo_type  = ttk.Combobox(Manage_Frame, font=("times new roman", 15, "bold"), width=18, state="readonly")
        combo_type['values'] = ("1. Encrypt", "2. Decrypt")
        combo_type.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_key = Label(Manage_Frame, text="Enter Key:", bg="grey", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_key.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        key_input = Entry(Manage_Frame, show="*", font=("times new roman", 15, "bold"), width=10, bd=5, relief=GROOVE)
        key_input.grid(row=3, column=1, pady=10, padx=20, sticky="w")


        def file_open():
            """open a file to read"""
            # optional initial directory (default is current directory)
            initial_dir = "E:/PyCharm/Projects/"

            # the filetype mask (default is all files)
            mask = \
                [("Text and JSON files", "*.txt *.json"),
                 ("Python files", "*.py *.pyw"),
                 ("HTML files", "*.htm"),
                 ("All files", "*.*")]
            try:
                file_open.fin = ""
                file_open.fin = askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
                print(file_open.fin.name)
                global check
                check = True

            except AttributeError:
                pass
            except UnicodeDecodeError:
                from PIL import Image
                Image.open(file_open.name).show()
            except FileNotFoundError:
                pass

        # defining function of encryption
        def encrypt(filename=None, key=None):
            if filename is None:
                filename = file_open.fin.name
            if key is None:
                key = key_input.get()
            try:
                file = open(filename, "rb")
                data = file.read()
                file.close()
                reversed = filename[::-1]
                counter = 0
                for element in range(0, len(reversed)):
                    if reversed[element] != "/":
                        counter += 1
                    else:
                        break

                cutted_filename = reversed[0:counter]
                clear_name = cutted_filename[::-1]
                current_path = filename[0:-counter]

                data = bytearray(data)
                for index, value in enumerate(data):
                    data[index] = value ^ int(key)

                file = open(current_path + "Encrypted-" + clear_name, "wb")
                file.write(data)
                file.close()
                messagebox.showinfo("Success", "Successfully Encrypted!")

            except FileNotFoundError:
                messagebox.showerror("Error", "Give me valid path!")
            except ValueError:
                messagebox.showerror("Error", "Give me NUMBER as a key!")
            except:
                messagebox.showerror("Error", "Unexpected error!")

        # defining function of decryption
        def decrypt(filename=None, key=None):
            if filename is None:
                filename = file_open.fin.name
            if key is None:
                key = key_input.get()
            try:
                file = open(filename, "rb")
                data = file.read()
                file.close()

                reversed = filename[::-1]
                counter = 0
                for element in range(0, len(reversed)):
                    if reversed[element] != "/":
                        counter += 1
                    else:
                        break

                cutted_filename = reversed[0:counter]
                clear_name = cutted_filename[::-1]
                old_name = clear_name.split("-")
                current_path = filename[0:-counter]
                #print(current_path)

                data = bytearray(data)
                for index, value in enumerate(data):
                    data[index] = value ^ int(key)

                file = open(current_path + old_name[1], "wb")
                #print(file)
                file.write(data)
                file.close()
                messagebox.showinfo("Success", "Successfully Decrypted!")

            except FileNotFoundError:
                messagebox.showerror("Error", "Give me valid path!")
            except ValueError:
                messagebox.showerror("Error", "Give me NUMBER as a key!")
            except:
                messagebox.showerror("Error", "Unexpected error!")

        def calling_funcs():
            if 'check' in globals():
                choice = combo_type.get().split(" ")
                if choice[0] == "1.":
                        encrypt()
                elif choice[0] == "2.":
                    decrypt()
                else:
                    messagebox.showwarning("Warning", "No action given!")
            else:
                messagebox.showwarning("Warning", "Open a file first")

        # Button frame
        getbtn = Button(Manage_Frame, text="Open",
                        bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                        command=lambda: file_open())
        getbtn.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        getbtn = Button(Manage_Frame, text="Progress",
                           bg="lightblue", fg="black", font=("times new roman", 12, "bold"),
                           command= lambda: calling_funcs())
        getbtn.grid(row=5, column=1, padx=20, pady=10, sticky="w")


root = Tk()
ob = Device(root)

root.mainloop()