from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import connection

class Main:
    def __init__(self):
        self.backgroundcolour='#92A9BD'
        self.maincolor='#B9EDDD'
        self.btncolor='#B9EDDD'
        self.lb0color='#87CBB9'
        self.activebutton='#87CBB9'
        self.framecolor='#87CBB9'

        self.root = Tk()
        self.root.title("Add Admin")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Add Admin", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Enter Name", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text="Enter Email", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text="Enter Mobile", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.f, text="Select Role", font=self.font,bg=self.lb0color)
        self.txt4 = ttk.Combobox(self.f, width=23, font=self.font, values=['Super Admin', 'Admin'],state='readonly')
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.f, text="Enter Password", font=self.font,bg=self.lb0color)
        self.txt5 = Entry(self.f, width=25, font=self.font, show='*',relief=SOLID)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)


        self.btn = Button(self.root, text="Submit", font=self.font, command=self.insertAdmin,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root.mainloop()

    def insertAdmin(self):
        conn = connection.Connect()
        cr = conn.cursor()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        role = self.txt4.get()
        password = self.txt5.get()

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(password) == 0 or len(role) == 0:
            msg.showwarning("Warning", "Please Enter All Data..", parent=self.root)
        else:
          if connection.verify(email)=='Invalid' or connection.check(mobile)=='Invalid':
              msg.showwarning("","Invalid Email or Mobile Number",parent=self.root)

          else:
            q = f"insert into admin values (null, '{name}', '{email}','{mobile}', '{password}','{role}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success", "Admin Added Successfully..", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt5.delete(0, 'end')
            self.txt4.set('')


#obj = Main()