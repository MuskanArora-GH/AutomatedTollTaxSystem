from tkinter import *
import tkinter.messagebox as msg
import connection
import dashboard


class Main:
    def __init__(self):

        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()
        self.root.title("Login Form")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('600x500')

        self.mainLabel = Label(self.root, text="Login Form", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Enter Email", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)


        self.lb2 = Label(self.f, text="Enter Password", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID ,show="*")
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.btn = Button(self.root, text="Submit", font=self.font, command=self.checkLogin,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root.mainloop()

    def checkLogin(self):
        email = self.txt1.get()
        password = self.txt2.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        data = cr.fetchall()
        if len(data) == 0:
            msg.showwarning('Warning',"Invalid Email/Password", parent=self.root)
        else:
            # print(data[0])
            id = data[0][0]
            name = data[0][1]
            msg.showinfo('Success', "Login Successful", parent=self.root)
            self.root.destroy()
            dashboard.Main(adminID=id, adminName=name, adminRole=data[0][-1])

# obj = Main()