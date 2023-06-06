from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import Connect


class Main:
    def __init__(self):

        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()
        self.root.title('View Issued Pass')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Issued Pass', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text='Search', font=('arial', 14),bg=self.lb0color)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.f, width=40, font=('arial', 14),relief=SOLID)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.btn = Button(self.f, text='Search', font=('arial', 12), command=self.searchVehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.grid(row=0, column=2, padx=10, pady=10)
        self.btn1 = Button(self.f, text='Refresh', font=('arial', 12), command=self.refreshTable,bg=self.btncolor,activebackground=self.activebutton)
        self.btn1.grid(row=0, column=3, padx=10, pady=10)

        self.passTable = ttk.Treeview(self.root, columns=('number', 'owner', 'mobile', 'email','issued_date', 'expiry_date', 'category'))
        self.passTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.passTable.heading('number', text='Number')
        self.passTable.heading('owner', text='Owner Name')
        self.passTable.heading('mobile', text='Mobile')
        self.passTable.heading('email', text='Email')
        self.passTable.heading('issued_date', text='Issue Date')
        self.passTable.heading('expiry_date', text='Expiry Date')
        self.passTable.heading('category', text='Category')

        self.passTable['show'] = 'headings'
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12), rowheight=30)
        self.getValues()

        self.root.mainloop()

    def refreshTable(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchVehicle(self):
        text = self.txt1.get()
        q = f'''SELECT vehicle.vehicle_number,vehicle.owner_name,vehicle.mobile, vehicle.email, issue_monthlypass.issue_date, issue_monthlypass.expiry_date, vehicle.category
FROM vehicle
INNER JOIN issue_monthlypass
ON vehicle.id = issue_monthlypass.vehicle_id where vehicle.owner_name like '%{text}%';'''
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.passTable.get_children():
            self.passTable.delete(k)
        count = 0
        for i in data:
            self.passTable.insert('', index=count, values=i)
            count += 1


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = '''SELECT vehicle.vehicle_number,vehicle.owner_name,vehicle.mobile, vehicle.email, issue_monthlypass.issue_date, issue_monthlypass.expiry_date, vehicle.category
                FROM vehicle
                INNER JOIN issue_monthlypass
                ON vehicle.id = issue_monthlypass.vehicle_id;'''
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.passTable.get_children():
            self.passTable.delete(k)
        count = 0
        for i in data:
            self.passTable.insert('', index=count, values=i)
            count += 1


#obj = Main()
