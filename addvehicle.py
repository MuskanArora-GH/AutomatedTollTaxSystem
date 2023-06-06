from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
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
        self.root.title("Add Vehicle")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('800x600')

        self.mainLabel = Label(self.root, text="Add Vehicle", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Enter Vehicle Number", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.f, text="Enter Owner Name", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.f, text="Enter Mobile", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.f, text="Enter Email", font=self.font,bg=self.lb0color)
        self.txt4 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.f, text="Enter Year", font=self.font,bg=self.lb0color)
        self.txt5 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = Label(self.f, text="Enter Model Name", font=self.font,bg=self.lb0color)
        self.txt6 = Entry(self.f, width=25, font=self.font,relief=SOLID )
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.lb7 = Label(self.f, text="Enter Company Name", font=self.font,bg=self.lb0color)
        self.txt7 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)

        self.lb8 = Label(self.f, text="Enter Category", font=self.font,bg=self.lb0color)
        self.txt8 = ttk.Combobox(self.f, width=25, font=self.font,values=self.getCategory(),state='readonly' )
        self.lb8.grid(row=7, column=0, padx=10, pady=10)
        self.txt8.grid(row=7, column=1, padx=10, pady=10)


        self.btn = Button(self.root, text="Submit", font=self.font, command=self.insertVehicle,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root.mainloop()

    def getCategory(self):
            conn = connection.Connect()
            cr = conn.cursor()
            q = 'select name from category'
            cr.execute(q)
            data = cr.fetchall()
            print(data)
            lst = []
            for i in data:
                lst.append(i[0])
            return lst

    def insertVehicle(self):
        conn = connection.Connect()
        cr = conn.cursor()
        vehicle_number = self.txt1.get()
        owner_name= self.txt2.get()
        mobile = self.txt3.get()
        email= self.txt4.get()
        year= self.txt5.get()
        model = self.txt6.get()
        company = self.txt7.get()
        category = self.txt8.get()

        if  len(vehicle_number) == 0 or len(owner_name) == 0 or len(mobile) == 0 or len(email) == 0 or len(year) == 0 or len(model) == 0 or len(company) == 0 or len(category)==0:
            msg.showwarning("Warning", "Please Enter All Data..",parent=self.root)
        else:
            if connection.verify(email)=='Invalid' or connection.check(mobile)=='Invalid':
                msg.showwarning("","Invalid Email or Mobile Number",parent=self.root)
            else:
                q = f"insert into vehicle values (null, '{vehicle_number}', '{owner_name}','{mobile}', '{email}','{year}','{model}','{company}','{category}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo("Success", "Vehicle Added Successfully..",parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt6.delete(0, 'end')
                self.txt7.delete(0, 'end')
                self.txt8.set('')


#obj = Main()