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
        self.root.title('View Toll Plaza')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Toll Plaza', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.tollTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'password'))
        self.tollTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.tollTable.heading('id', text='ID')
        self.tollTable.heading('name', text='Name')
        self.tollTable.heading('mobile', text='Mobile')
        self.tollTable.heading('email', text='Email')
        self.tollTable.heading('password', text='Password')

        self.tollTable['show'] = 'headings'
        self.tollTable.bind("<Double-1>", self.openUpdateWindow)

        self.btn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.deleteToll,bg=self.btncolor,activebackground=self.activebutton)
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

        rowid = self.tollTable.selection()[0]
        item = self.tollTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Toll')
        self.mainLabel = Label(self.root1, text="Update Toll", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text=" Toll ID", font=self.font,bg=self.lb0color)
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

        self.lb4 = Label(self.f, text="Enter Password", font=self.font,bg=self.lb0color)
        self.txt4 = Entry(self.f, width=25, font=self.font,relief=SOLID, show='*')
        self.lb4.grid(row=4, column=0, padx=10, pady=10)
        self.txt4.grid(row=4, column=1, padx=10, pady=10)
        self.txt4.insert(0,data[4])


        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateToll,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()


    def updateToll(self):
        id = self.txt0.get()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password= self.txt4.get()

        q = f"update toll set name='{name}', email='{email}',mobile='{mobile}', password='{password}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Toll has been Updated",parent=self.root)
        self.root1.destroy()
        self.getValues()


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select id,name,email,mobile,password from toll'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.tollTable.get_children():
            self.tollTable.delete(k)
        count = 0
        for i in data:
            self.tollTable.insert('', index=count, values=i)
            count += 1

    def deleteToll(self):
        rowid = self.tollTable.selection()[0]
        item = self.tollTable.item(rowid)
        data = item['values']
        tollID = data[0]
        q = f'delete from toll where id="{tollID}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Toll has been Removed',parent=self.root)
        self.getValues()


#obj = Main()