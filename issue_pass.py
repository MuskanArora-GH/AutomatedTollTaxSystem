import datetime
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
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
        self.root.title("Issue Pass")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Issue Pass", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Enter Number", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text="Vehicle Id", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text="Pass", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)



        self.lb4 = Label(self.f, text="Issue Date", font=self.font,bg=self.lb0color)
        self.txt4 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.f, text="Select Days", font=self.font,bg=self.lb0color)
        self.txt5 = ttk.Combobox(self.f, width=23, font=self.font, state='readonly', values=list(range(1, 31)))
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.bind('<<ComboboxSelected>>', self.setExpiry)

        self.lb6 = Label(self.f, text="Expiry Date", font=self.font,bg=self.lb0color)
        self.txt6 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)


        self.btn = Button(self.root, text="Submit", font=self.font, command=self.issuePass,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)

        self.searchBtn = Button(self.f, text="Search", font=self.font, command=self.searchNumber,bg=self.btncolor,activebackground=self.activebutton)
        self.searchBtn.grid(row=0, column=2)



        self.root.mainloop()

    def setExpiry(self, event):
        self.txt6.delete(0, 'end')
        self.txt6.insert(0, str(datetime.date.today() + datetime.timedelta(days=int(self.txt5.get()))))

    def searchNumber(self):
        number = self.txt1.get()
        if len(number) == 0:
            msg.showwarning('Warning', 'PLease Enter Number First', parent=self.root)
        else:
            conn = connection.Connect()
            cr = conn.cursor()
            q = f"select id, category from vehicle where vehicle_number = '{number}'"
            cr.execute(q)
            data = cr.fetchall()
            if len(data) == 0:
                msg.showwarning('Warning', 'Vehicle not Registered.', parent=self.root)
            else:
                self.txt2.delete(0, 'end')
                self.txt2.insert(0, data[0][0])
                category = data[0][1]
                q = f'select id from monthlypass where category ="{category}"'
                cr.execute(q)
                passData = cr.fetchall()
                if len(passData) == 0:
                    msg.showwarning('Warning', f"{category} is not Registered.", parent=self.root)
                else:
                    self.txt3.delete(0, 'end')
                    self.txt3.insert(0, passData[0][0])
                    self.txt4.insert(0, str(datetime.date.today()))

    def issuePass(self):
        conn = connection.Connect()
        cr = conn.cursor()
        number = self.txt1.get()
        vehicle_id = self.txt2.get()
        issue_pass= self.txt3.get()
        issue_date = self.txt4.get()
        expiry_date = self.txt6.get()

        if len(number) == 0 or len(vehicle_id) == 0 or len(issue_pass) == 0 or len(issue_date) == 0 or len(expiry_date) == 0:
            msg.showwarning("Warning", "Please Enter All Data..",parent=self.root)
        else:
            q = f"select * from issue_monthlypass where vehicle_id='{vehicle_id}' and expiry_date > '{issue_date}'"
            cr.execute(q)
            data = cr.fetchall()
            if len(data) == 0:
                q = f"insert into issue_monthlypass values (NULL,'{vehicle_id}','{issue_pass}', '{issue_date}','{expiry_date}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo("Success", "Pass Issued Successfully..",parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.set('')
                self.txt6.delete(0, 'end')
            else:
                msg.showwarning('Warning','Already have an active pass.', parent=self.root)



#obj = Main()