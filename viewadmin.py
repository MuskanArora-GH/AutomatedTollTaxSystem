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

        self.root = Toplevel()
        self.root.title('View Admin')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Admin', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.adminTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'role'))
        self.adminTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.adminTable.heading('id', text='ID')
        self.adminTable.heading('name', text='Name')
        self.adminTable.heading('mobile', text='Mobile')
        self.adminTable.heading('email', text='Email')
        self.adminTable.heading('role', text='Admin Role')

        self.adminTable['show'] = 'headings'
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.btn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.deleteAdmin,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=20)

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12), rowheight=30)
        self.getValues()


        self.root.mainloop()






    def openUpdateWindow(self, event):
        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        rowid = self.adminTable.selection()[0]
        item = self.adminTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Admin')
        self.mainLabel = Label(self.root1, text="Update Admin", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="Admin ID", font=self.font,bg=self.lb0color)
        self.txt0 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.txt0.insert(0, data[0])
        self.txt0.configure(state='readonly')

        self.lb1 = Label(self.f, text="Enter Name", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.f, text="Enter Email", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.f, text="Enter Mobile", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.txt3.grid(row=3, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.f, text="Select Role", font=self.font,bg=self.lb0color)
        self.txt4 = ttk.Combobox(self.f, width=23, font=self.font, values=['Super Admin', 'Admin'],state='readonly')
        self.lb4.grid(row=4, column=0, padx=10, pady=10)
        self.txt4.grid(row=4, column=1, padx=10, pady=10)
        self.txt4.set(data[4])


        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateAdmin,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()


    def updateAdmin(self):
        id = self.txt0.get()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        role = self.txt4.get()

        q = f"update admin set name='{name}', email='{email}',mobile='{mobile}', role='{role}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Admin has been Updated",parent=self.root1)
        self.root1.destroy()
        self.getValues()


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select id,name,email,mobile,role from admin'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.adminTable.get_children():
            self.adminTable.delete(k)
        count = 0
        for i in data:
            self.adminTable.insert('', index=count, values=i)
            count += 1

    def deleteAdmin(self):
        rowid = self.adminTable.selection()[0]
        item = self.adminTable.item(rowid)
        data = item['values']
        adminID = data[0]
        q = f'delete from admin where id="{adminID}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Admin has been Removed',parent=self.root1)
        self.getValues()


#obj = Main()