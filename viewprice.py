import re
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
        self.root.title('View Price')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Price', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.priceTable = ttk.Treeview(self.root, columns=('id', 'category', 'price', 'description', ))
        self.priceTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.priceTable.heading('id', text='ID')
        self.priceTable.heading('category', text='Category')
        self.priceTable.heading('price', text='Price')
        self.priceTable.heading('description', text='Description')


        self.priceTable['show'] = 'headings'
        self.priceTable.bind("<Double-1>", self.openUpdateWindow)

        self.btn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.deleteCategory,bg=self.btncolor,activebackground=self.activebutton)
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

        rowid = self.priceTable.selection()[0]
        item = self.priceTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Tollprice')
        self.mainLabel = Label(self.root1, text="Update Price", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)

        self.lb0 = Label(self.f, text="Category ID", font=self.font,bg=self.lb0color)
        self.txt0 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.txt0.insert(0, data[0])
        self.txt0.configure(state='readonly')

        self.lb1 = Label(self.f, text="Enter Category", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.f, text="Enter Price", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2].replace('.0',''))

        self.lb3 = Label(self.f, text="Enter Description", font=self.font,bg=self.lb0color)
        self.txt3 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.txt3.grid(row=3, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])




        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateTollPrice,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()


    def updateTollPrice(self):
        id = self.txt0.get()
        category= self.txt1.get()
        price = self.txt2.get()
        description = self.txt3.get()

        if bool(re.match('^[0-9]+$', price)):
            q = f"update tollprice set category='{category}', price='{price}',description='{description}' where id='{id}'"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("Success", "Tollprice has been Updated", parent=self.root)
            self.root1.destroy()
            self.getValues()
        else:
            msg.showwarning('Warning', "Please Enter valid amount.", parent=self.root1)


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select id,category,price,description from tollprice'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.priceTable.get_children():
            self.priceTable.delete(k)
        count = 0
        for i in data:
            self.priceTable.insert('', index=count, values=i)
            count += 1

    def deleteCategory(self):
        rowid = self.priceTable.selection()[0]
        item = self.priceTable.item(rowid)
        data = item['values']
        categoryID = data[0]
        q = f'delete from tollprice where id="{categoryID}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Category has been Removed', parent=self.root)
        self.getValues()

if __name__ == '__main__':
    obj = Main()