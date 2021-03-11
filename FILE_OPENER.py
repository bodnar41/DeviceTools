# a very simple Tkinter editor to show file read/write dialog

from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile


class Editor(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.text = Text()
        self.text.pack()

        menu = Menu(master)
        root.config(menu=menu)
        # file menu
        filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Actions", menu=filemenu)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.do_exit)



    def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "E:/PyCharm/Projects/"
        # the filetype mask (default is all files)
        mask = \
            [("Text and JSON files", "*.txt *.json"),
             ("Python files", "*.py *.pyw"),
             ("HTML files", "*.htm"),
             ("Log files", "*.log"),
             ("All files", "*.*")]
        try:
            fin = askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
            text = fin.read()

            if text != None:
                self.text.delete(0.0, END)
                self.text.insert(END, text)
        except AttributeError:
            pass
        except UnicodeDecodeError:
            from PIL import Image
            Image.open(fin.name).show()



    def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0, END))
        fout.write(text2save)
        fout.close()

    def do_exit(self):
        root.destroy()




root = Tk()
root.title("Info editor")
root.geometry("700x400")
app = Editor(root)
root.mainloop()