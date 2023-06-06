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

        self.root =Toplevel()
        self.root.title('View Vehicle')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Vehicle', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text='Search', font=('arial', 14),bg=self.lb0color)
        self.lb11.grid(row=0, column=0, padx=10, pady=10)
        self.txt11 = Entry(self.f, width=40, font=('arial', 14),relief=SOLID)
        self.txt11.grid(row=0, column=1, padx=10, pady=10)
        self.btn = Button(self.f, text='Search', font=('arial', 12), command=self.searchVehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.grid(row=0, column=2, padx=10, pady=10)
        self.btn11 = Button(self.f, text='Refresh', font=('arial', 12), command=self.refreshTable,bg=self.btncolor,activebackground=self.activebutton)
        self.btn11.grid(row=0, column=3, padx=10, pady=10)

        self.vehicleTable = ttk.Treeview(self.root, columns=('id','vehicle_number', 'owner_name', 'mobile', 'email','year','model','company','category'))
        self.vehicleTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.vehicleTable.heading('id', text='ID')
        self.vehicleTable.heading('vehicle_number', text='Vehicle Number')
        self.vehicleTable.heading('owner_name', text='Owner Name')
        self.vehicleTable.heading('mobile', text='Mobile')
        self.vehicleTable.heading('email', text='Email')
        self.vehicleTable.heading('year', text='Year')
        self.vehicleTable.heading('model', text='Model')
        self.vehicleTable.heading('company', text='Company')
        self.vehicleTable.heading('category', text='Category')


        self.vehicleTable.column('id',width=70,anchor=CENTER)
        self.vehicleTable.column('year', width=100, anchor=CENTER)
        self.vehicleTable.column('mobile', width=150, anchor=CENTER)
        self.vehicleTable.column('model', width=130, anchor=CENTER)
        self.vehicleTable.column('email', width=250, anchor=CENTER)
        self.vehicleTable.column('company', width=120, anchor=CENTER)
        self.vehicleTable.column('vehicle_number', anchor=CENTER)
        self.vehicleTable.column('owner_name',anchor=CENTER)
        self.vehicleTable.column('category', anchor=CENTER)

        self.vehicleTable['show'] = 'headings'
        self.vehicleTable.bind("<Double-1>", self.openUpdateWindow)

        self.btn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.deletevehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=20)

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12), rowheight=30)
        self.getValues()
        self.root.mainloop()

    def refreshTable(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def searchVehicle(self):
        text = self.txt11.get()
        q = f'''select id,vehicle_number,owner_name,mobile,email,year,model,company,category from vehicle where owner_name like "%{text}%" or vehicle_number like "%{text}%"'''
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.vehicleTable.get_children():
            self.vehicleTable.delete(k)
        count = 0
        for i in data:
            self.vehicleTable.insert('', index=count, values=i)
            count += 1






    def openUpdateWindow(self, event):

        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        rowid = self.vehicleTable.selection()[0]
        item = self.vehicleTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Vehicle')
        self.mainLabel = Label(self.root1, text="Update Vehicle", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="Vehicle ID", font=self.font,bg=self.lb0color)
        self.txt0 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.txt0.insert(0, data[0])
        self.txt0.configure(state='readonly')

        self.lb1 = Label(self.f, text="Vehicle Number", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.f, text="Owner Name", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.f, text="Enter Mobile", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.txt3.grid(row=3, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.f, text="Enter Email",font=self.font,bg=self.lb0color)
        self.txt4 = Entry(self.f, width=23, font=self.font,relief=SOLID)
        self.lb4.grid(row=4, column=0, padx=10, pady=10)
        self.txt4.grid(row=4, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[4])

        self.lb5 = Label(self.f, text="Enter Year", font=self.font,bg=self.lb0color)
        self.txt5 =Entry(self.f, width=23, font=self.font,relief=SOLID)
        self.lb5.grid(row=5, column=0, padx=10, pady=10)
        self.txt5.grid(row=5, column=1, padx=10, pady=10)
        self.txt5.insert(0,data[5])

        self.lb6 = Label(self.f, text="Enter Model", font=self.font,bg=self.lb0color)
        self.txt6 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb6.grid(row=6, column=0, padx=10, pady=10)
        self.txt6.grid(row=6, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[6])

        self.lb7 = Label(self.f, text="Enter Company", font=self.font,bg=self.lb0color)
        self.txt7 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb7.grid(row=7, column=0, padx=10, pady=10)
        self.txt7.grid(row=7, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[7])

        self.lb8 = Label(self.f, text="Enter Category", font=self.font,bg=self.lb0color)
        self.txt8 = ttk.Combobox(self.f, width=25, font=self.font, values=self.getCategory(), state='readonly')
        self.lb8.grid(row=8, column=0, padx=10, pady=10)
        self.txt8.grid(row=8, column=1, padx=10, pady=10)
        self.txt8.set(data[8])


        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateVehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()

    def getCategory(self):
            conn = Connect()
            cr = conn.cursor()
            q = 'select name from category'
            cr.execute(q)
            data = cr.fetchall()
            print(data)
            lst = []
            for i in data:
                lst.append(i[0])
            return lst


    def updateVehicle(self):
        vehicle_number = self.txt1.get()
        owner_name = self.txt2.get()
        mobile = self.txt3.get()
        email = self.txt4.get()
        year= self.txt5.get()
        model = self.txt6.get()
        company = self.txt7.get()
        category = self.txt8.get()
        id=self.txt0.get()

        q = f"update vehicle set vehicle_number='{vehicle_number}', owner_name='{owner_name}',mobile='{mobile}',email='{email}',year='{year}',model='{model}',company='{company}',category='{category}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Vehicle has been Updated",parent=self.root)
        self.root1.destroy()
        self.getValues()


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select id,vehicle_number,owner_name,mobile,email,year,model,company,category from vehicle'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.vehicleTable.get_children():
            self.vehicleTable.delete(k)
        count = 0
        for i in data:
            self.vehicleTable.insert('', index=count, values=i)
            count += 1

    def deletevehicle(self):
        rowid = self.vehicleTable.selection()[0]
        item = self.vehicleTable.item(rowid)
        data = item['values']
        vehicleID = data[0]
        q = f'delete from vehicle where id="{vehicleID}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Vehicle has been Removed',parent=self.root)
        self.getValues()



if __name__ == '__main__':
    obj = Main()