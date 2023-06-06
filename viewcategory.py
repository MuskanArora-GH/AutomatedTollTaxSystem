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
        self.root.title('View Category')
        self.root.configure(background=self.backgroundcolour)
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Category', font=('arial', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.categoryTable = ttk.Treeview(self.root, columns=( 'name', 'description'))
        self.categoryTable.pack(pady=10, padx=10, expand=True, fill='both')

        self.categoryTable.heading('name', text='Name')
        self.categoryTable.heading('description', text='Description')


        self.categoryTable['show'] = 'headings'
        self.categoryTable.bind("<Double-1>", self.openUpdateWindow)

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

        name = self.categoryTable.selection()[0]
        item = self.categoryTable.item(name)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('600x600')
        self.root1.configure(background=self.backgroundcolour)
        self.root1.title('Update Category')
        self.mainLabel = Label(self.root1, text="Update Category", font=('arial', 20, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root1,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)

        self.font = ('calibri', 14)


        self.lb1 = Label(self.f, text="Enter Name", font=self.font,bg=self.lb0color)
        self.txt1 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.f, text="Enter Description", font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.txt2.grid(row=2, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])




        self.btn = Button(self.root1, text="Submit", font=self.font, command=self.updateCategory,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)


        self.root1.mainloop()


    def updateCategory(self):
        name = self.txt1.get()
        description = self.txt2.get()


        q = f"update category set description='{description}' where name='{name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Category has been Updated",parent=self.root)
        self.root1.destroy()
        self.getValues()


    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = 'select name,description from category'
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.categoryTable.get_children():
            self.categoryTable.delete(k)
        count = 0
        for i in data:
            self.categoryTable.insert('', index=count, values=i)
            count += 1

    def deleteAdmin(self):
        name = self.categoryTable.selection()[0]
        item = self.categoryTable.item(name)
        data = item['values']
        name = data[0]
        q = f'delete from category where name="{name}"'
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', 'Category has been Removed',parent=self.root)
        self.getValues()

if __name__ == '__main__':
    obj = Main()