import re
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import connection

class Main:
    def __init__(self):

        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()
        self.root.title("Add Price")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Add Price", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="Select Category", font=self.font,bg=self.lb0color)
        self.txt0 = ttk.Combobox(self.f, width=23, font=self.font, values=self.getCategory(), state='readonly')
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)



        self.lb1 = Label(self.f, text="Enter Price", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text="Enter Description", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)




        self.btn = Button(self.root, text="Submit", font=self.font, command=self.insertData,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root.mainloop()

    def getCategory(self):
        conn = connection.Connect()
        cr = conn.cursor()
        q = 'select name from category'
        cr.execute(q)
        data = cr.fetchall()
        print(data)
        lst = []
        for i in data:
            lst.append(i[0])
        return lst



    def insertData(self):
        conn = connection.Connect()
        cr = conn.cursor()
        price = self.txt1.get()
        description = self.txt2.get()
        category=self.txt0.get()


        if len(price) == 0 or len(description) == 0:
            msg.showwarning("Warning", "Please Enter All Data..", parent=self.root)
        else:
            if bool(re.match('^[0-9]+$', price)):
                q = f"insert into tollprice values (null, '{category}', '{price}','{description}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo("Success", "vehicle Added Successfully..", parent=self.root)
                self.txt0.set('')
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
            else:
                msg.showwarning('Warning',"Please Enter valid amount.", parent=self.root)

if __name__ == '__main__':
    obj = Main()