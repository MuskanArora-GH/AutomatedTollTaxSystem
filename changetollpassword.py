from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import connection

class Main:
    def __init__(self, tollID):

        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()
        self.root.title("Change Toll Password")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Change Toll Password", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Your Toll ID", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, tollID)
        self.txt1.config(state='readonly')

        self.lb2 = Label(self.f, text="Enter Old Password", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID ,show='*')
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text="Enter New Password", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID, show='*')
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)



        self.btn = Button(self.root, text="Submit", font=self.font, command=self.updatePass,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root.mainloop()


    def updatePass(self):
        id = self.txt1.get()
        oldpass = self.txt2.get()
        newpass = self.txt3.get()
        conn = connection.Connect()
        cr = conn.cursor()
        q = f"SELECT * from toll where id='{id}' and password='{oldpass}'"
        cr.execute(q)
        data = cr.fetchall()
        if len(data) == 0:
            msg.showwarning('Warning', "Incorrect Old Password", parent=self.root)
        else:
            q1 = f"update toll set password='{newpass}' where id='{id}'"
            cr.execute(q1)
            conn.commit()
            msg.showinfo('Success', 'Password Changed Successfully', parent=self.root)
            self.root.destroy()

#obj = Main()