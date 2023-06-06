from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import connection

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Toll Plaza")
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Add Toll Plaxa", font=('arial', 20, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="Enter ID", font=self.font)
        self.txt0 = Entry(self.f, width=25, font=self.font)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)

        self.lb1 = Label(self.f, text="Enter Name", font=self.font)
        self.txt1 = Entry(self.f, width=25, font=self.font)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text="Enter Email", font=self.font)
        self.txt2 = Entry(self.f, width=25, font=self.font)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text="Enter Mobile", font=self.font)
        self.txt3 = Entry(self.f, width=25, font=self.font)
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.txt3.grid(row=3, column=1, padx=10, pady=10)



        self.lb4 = Label(self.f, text="Enter Password", font=self.font)
        self.txt4 = Entry(self.f, width=25, font=self.font, show='*')
        self.lb4.grid(row=4, column=0, padx=10, pady=10)
        self.txt4.grid(row=4, column=1, padx=10, pady=10)


        self.btn = Button(self.root, text="Submit", font=self.font, command=self.insertToll)
        self.btn.pack(pady=10)


        self.root.mainloop()

    def insertToll(self):
        conn = connection.Connect()
        cr = conn.cursor()
        id = self.txt0.get()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()

        if len(id)==0 or len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(password) == 0 :
            msg.showwarning("Warning", "Please Enter All Data..", parent=self.root)
        else:
            q = f"insert into toll values (null,{id}, '{name}', '{email}','{mobile}', '{password}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success", "Toll Added Successfully..", parent=self.root)
            self.txt0.delete(0,'end')
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')



obj = Main()