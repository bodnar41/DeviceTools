import _tkinter
from tkinter import END, messagebox

import pymysql

def add_devices(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="devicemgmt")
    cur = con.cursor()
    try:
        cur.execute("insert into devices values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                                  self.name_var.get(),
                                                                                  self.category_var.get(),
                                                                                  self.quantity_var.get(),
                                                                                  self.manufacturer_var.get(),
                                                                                  self.type_var.get(),
                                                                                  self.serial_var.get(),
                                                                                  self.guarantee_var.get()
                                                                                  ))

    except _tkinter.TclError:
        messagebox.showerror('Error', f"Roll No. and Quantity must be a number!")
    except pymysql.err.IntegrityError:
        messagebox.showerror('Error', f"Roll No. {self.Roll_No_var.get()} already exists!")
    con.commit()
    fetch_data(self)
    clear(self)
    con.close()

def fetch_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="devicemgmt")
    cur = con.cursor()
    cur.execute("select * from devices")
    rows = cur.fetchall()
    if len(rows) != 0:
        self.Device_table.delete(*self.Device_table.get_children())
        for row in rows:
            self.Device_table.insert('', END, values=row)
        con.commit()
    con.close()

def clear(self):
    self.Roll_No_var.set("")
    self.name_var.set("")
    self.category_var.set("")
    self.quantity_var.set("")
    self.manufacturer_var.set("")
    self.type_var.set("")
    self.serial_var.set("")
    self.guarantee_var.set("")

def update_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="devicemgmt")
    cur = con.cursor()
    try:
        cur.execute("update devices set name=%s,category=%s,quantity=%s,manufacturer=%s,type=%s,serial=%s,guarantee=%s where roll_no=%s",(self.name_var.get(),
                                                                            self.category_var.get(),
                                                                            self.quantity_var.get(),
                                                                            self.manufacturer_var.get(),
                                                                            self.type_var.get(),
                                                                            self.serial_var.get(),
                                                                            self.guarantee_var.get(),
                                                                            self.Roll_No_var.get()
                                                                            ))
    except _tkinter.TclError:
        messagebox.showerror('Error', f"Roll No. and Quantity must be a number!")
    except pymysql.err.IntegrityError:
        messagebox.showerror('Error', f"Roll No. {self.Roll_No_var.get()} already exists!")

    con.commit()
    fetch_data(self)
    clear(self)
    con.close()

def delete_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="devicemgmt")
    cur = con.cursor()
    try:
        cur.execute("delete from devices where roll_no=%s",self.Roll_No_var.get())
    except _tkinter.TclError:
        messagebox.showerror('Error', f"Select item to delete!")
    con.commit()
    fetch_data(self)
    clear(self)
    con.close()

def search_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="devicemgmt")
    cur = con.cursor()
    try:
        cur.execute("select * from devices where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Device_table.delete(*self.Device_table.get_children())
            for row in rows:
                self.Device_table.insert('', END, values=row)
        else:
            messagebox.showwarning('Warning', f"No data found as *{self.search_txt.get()}*")
    except:
        messagebox.showwarning('Warning', "Select a filter option!")

    con.commit()
    con.close()


