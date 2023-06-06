from tkinter import *

import addmonthlypass
import addprice
import changeAdminPassword
import addadmin
import viewadmin
import addcategory
import viewcategory
import addtollplaza
import viewmonthlypass
import viewprice
import viewtollplaza


class Main:
    def __init__(self, adminID, adminName, adminRole):
        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(background=self.backgroundcolour)
        self.root.title('Admin Dashboard')

        self.rootMenu = Menu(self.root)
        self.root.configure(menu=self.rootMenu)

        if adminRole == 'Super Admin':
            self.adminMenu = Menu(self.rootMenu, tearoff=0)
            self.rootMenu.add_cascade(label='Admin', menu=self.adminMenu)
            self.adminMenu.add_command(label='Add Admin', command=lambda :addadmin.Main())
            self.adminMenu.add_command(label='View Admin', command=lambda :viewadmin.Main())

        self.categoryMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Category', menu=self.categoryMenu)
        self.categoryMenu.add_command(label='Add Category',command=lambda :addcategory.Main())
        self.categoryMenu.add_command(label='View Category',command=lambda :viewcategory.Main())

        self.tollPriceMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Manage Price', menu=self.tollPriceMenu)
        self.tollPriceMenu.add_command(label='Add Price',command=lambda :addprice.Main())
        self.tollPriceMenu.add_command(label='View Price',command=lambda :viewprice.Main())

        self.passMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Manage Pass', menu=self.passMenu)
        self.passMenu.add_command(label='Add Pass',command=lambda :addmonthlypass.Main())
        self.passMenu.add_command(label='View Pass',command=lambda :viewmonthlypass.Main())

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Profile', menu=self.profileMenu)
        self.profileMenu.add_command(label='Change Password', command=lambda :changeAdminPassword.Main(adminID))
        self.profileMenu.add_command(label='Logout',command=lambda :self.root.destroy())

        self.nameMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='New Toll', menu=self.nameMenu)
        self.nameMenu.add_command(label='Add Toll', command=lambda: addtollplaza.Main())
        self.nameMenu.add_command(label='View Toll', command=lambda: viewtollplaza.Main())

        self.mainLabel = Label(self.root, text=f"Welcome {adminName}", font=('calibri', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.root.mainloop()

# obj = Main()