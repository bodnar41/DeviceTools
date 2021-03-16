from tkinter import *
from tkinter import ttk
import pymysql
from MGMT_DB import *

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import  DateEntry

class Device:
    def __init__(self, root):
        self.root = root
        self.root.title("Device Manager")
        self.root.geometry("1450x700+0+0")

        title = Label(self.root, text="Device Manager", bd=5, relief=GROOVE, font=("times new roman", 40, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        #All Variables
        self.Roll_No_var = IntVar()
        self.name_var = StringVar()
        self.category_var = StringVar()
        self.quantity_var = IntVar()
        self.manufacturer_var = StringVar()
        self.type_var = StringVar()
        self.serial_var = StringVar()
        self.guarantee_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


        # Manage frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=450, height=560)

        m_title = Label(Manage_Frame, text="Manage Devices", bg="grey", fg="white", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief = GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Device name", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_category = Label(Manage_Frame, text="Category", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_category.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_category = ttk.Combobox(Manage_Frame, textvariable=self.category_var, font=("times new roman", 15, "bold"), state="readonly")
        combo_category['values'] = ("Mobile", "Laptop", "IT Equipment", "Network device", "Other")
        combo_category.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        combo_category.set('--Select--')

        lbl_quantity = Label(Manage_Frame, text="Quantity", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_quantity.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_quantity = Entry(Manage_Frame, textvariable=self.quantity_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_quantity.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_manuf = Label(Manage_Frame, text="Manufacturer", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_manuf.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_manuf = Entry(Manage_Frame, textvariable=self.manufacturer_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_manuf.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_type = Label(Manage_Frame, text="Type", bg="grey", fg="white",font=("times new roman", 15, "bold"))
        lbl_type.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_type = Entry(Manage_Frame, textvariable=self.type_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_type.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_serial_id = Label(Manage_Frame, text="Serial ID", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_serial_id.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_serial_id = Entry(Manage_Frame, textvariable=self.serial_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_serial_id.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_guarantee = Label(Manage_Frame, text="Guarantee", bg="grey", fg="white",font=("times new roman", 15, "bold"))
        lbl_guarantee.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        cal = DateEntry(Manage_Frame, textvariable=self.guarantee_var, width=15, background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # Button frame
        btn_Frame = Frame(Manage_Frame, bd=0, relief=RIDGE, bg="grey")
        btn_Frame.place(x=15, y=500, width=420)

        addbtn = Button(btn_Frame, text="Add", width=10, command=lambda: add_devices(self)).grid(row=8, column=1, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=lambda: update_data(self)).grid(row=8, column=2, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10, command=lambda: delete_data(self)).grid(row=8, column=3, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=lambda: clear(self)).grid(row=8, column=4, padx=10, pady=10)

        # Detail frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="grey")
        Detail_Frame.place(x=500, y=100, width=850, height=560)

        lbl_search = Label(Detail_Frame, text="Search By", bg="grey", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=15, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Category", "Manufacturer", "Serial")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")
        combo_search.set('--Select--')

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, width=15, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,
                           command=lambda: search_data(self)).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", width=10, command=lambda: fetch_data(self)).grid(row=0, column=4, padx=10, pady=10)


        # Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="grey")
        Table_Frame.place(x=10, y=70, width=760, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Device_table = ttk.Treeview(Table_Frame, columns=("roll", "device name", "category", "quantity", "manufacturer", "type", "serial id", "guarantee"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Device_table.xview)
        scroll_y.config(command=self.Device_table.yview)
        self.Device_table.heading("roll", text="Roll No.")
        self.Device_table.heading("device name", text="Device Name")
        self.Device_table.heading("category", text="Category")
        self.Device_table.heading("quantity", text="Quantity")
        self.Device_table.heading("manufacturer", text="Manufacturer")
        self.Device_table.heading("type", text="Type")
        self.Device_table.heading("serial id", text="Serial ID")
        self.Device_table.heading("guarantee", text="Guarantee")
        self.Device_table['show'] = 'headings'
        self.Device_table.column("roll", width=50)
        self.Device_table.column("quantity", width=70)
        self.Device_table.pack(fill=BOTH, expand=1)

        self.Device_table.bind("<ButtonRelease-1>", self.get_cursor)

        fetch_data(self)

    def get_cursor(self, ev):
        cursor_row = self.Device_table.focus()
        contents = self.Device_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.category_var.set(row[2])
        self.quantity_var.set(row[3])
        self.manufacturer_var.set(row[4])
        self.type_var.set(row[5])
        self.serial_var.set(row[6])
        self.guarantee_var.set(row[7])


root = tk.Tk()
ob = Device(root)
root.mainloop()