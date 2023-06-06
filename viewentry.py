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

        self.root=Toplevel()
        self.root.title('View Entry')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Entry', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text='Search', font=('arial', 14),bg=self.lb0color)
        self.lb11.grid(row=0, column=0, padx=10, pady=10)
        self.txt11 = Entry(self.f, width=40, font=('arial', 14),relief=SOLID)
        self.txt11.grid(row=0, column=1, padx=10, pady=10)
        self.btn = Button(self.f, text='Search', font=('arial', 12), command=self.searchVehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.grid(row=0, column=2, padx=10, pady=10)


        self.entryTable = ttk.Treeview(self.root, columns=('id', 'vehicle_id', 'date', 'time', 'type'))
        self.entryTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.entryTable.heading('id', text='ID')
        self.entryTable.heading('vehicle_id', text='Vehicle Number')
        self.entryTable.heading('date', text='Date')
        self.entryTable.heading('time', text='Time')
        self.entryTable.heading('type', text='Type')

        self.entryTable['show'] = 'headings'
        # self.entryTable.bind("<Double-1>", self.openUpdateWindow)
        #
        # self.btn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.deleteEntry,bg=self.btncolor,activebackground=self.activebutton)
        # self.btn.pack(pady=20)

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12), rowheight=30)
        self.getValues()


        self.root.mainloop()


    def searchVehicle(self):
            text = self.txt11.get()
            q = f'''select entry.id,vehicle.vehicle_number,entry.date,entry.time,entry.type from entry inner join vehicle on entry.vehicle_id = vehicle.id where vehicle.vehicle_number like "%{text}%"'''
            self.cr.execute(q)
            data = self.cr.fetchall()
            # print(data)
            for k in self.entryTable.get_children():
                self.entryTable.delete(k)
            count = 0
            for i in data:
                self.entryTable.insert('', index=count, values=i)
                count += 1




    def openUpdateWindow(self, event):
        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        rowid = self.entryTable.selection()[0]
        item = self.entryTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Entry')
        self.mainLabel = Label(self.root1, text="Update Entry", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="ID", font=self.font,bg=self.lb0color)
        self.txt0 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.txt0.insert(0, data[0])
        self.txt0.configure(state='readonly')

        self.lb1 = Label(self.f, text="Enter Vehicle ID", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.f, text="Enter Date", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.f, text="Enter Time", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.txt3.grid(row=3, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.f, text="Select Type", font=self.font,bg=self.lb0color)
        self.txt4 = ttk.Combobox(self.f, width=23, font=self.font)
        self.lb4.grid(row=4, column=0, padx=10, pady=10)
        self.txt4.grid(row=4, column=1, padx=10, pady=10)
        self.txt4.set(data[4])


        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateEntry,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()


    def updateEntry(self):
        id = self.txt0.get()
        vehicle_id = self.txt1.get()
        date = self.txt2.get()
        time = self.txt3.get()
        type = self.txt4.get()

        q = f"update entry set vehicle_id='{vehicle_id}', date='{date}',time='{time}', type='{type}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Entry has been Updated", parent=self.root)
        self.root1.destroy()
        self.getValues()


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select entry.id,vehicle.vehicle_number,entry.date,entry.time,entry.type from entry inner join vehicle on entry.vehicle_id = vehicle.id'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.entryTable.get_children():
            self.entryTable.delete(k)
        count = 0
        for i in data:
            self.entryTable.insert('', index=count, values=i)
            count += 1

    def deleteEntry(self):
        rowid = self.entryTable.selection()[0]
        item = self.entryTable.item(rowid)
        data = item['values']
        entryID = data[0]
        q = f'delete from entry where id="{entryID}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Entry has been Removed', parent=self.root)
        self.getValues()


#obj = Main()