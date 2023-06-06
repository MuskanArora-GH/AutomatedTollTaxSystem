from tkinter import *
import changetollpassword
import addvehicle
import viewentry
import viewtransaction
import viewvehicle
import issue_pass
import view_issuepass
import tollDemo

class Main:
    def __init__(self, tollID,tollName):
        self.tollID = tollID
        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root = Tk()

        self.root.state('zoomed')
        self.root.configure(background=self.backgroundcolour)
        self.root.title('Toll Dashboard')

        self.rootMenu = Menu(self.root)
        self.root.configure(menu=self.rootMenu)


        self.vehicleMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='New Vehicle', menu=self.vehicleMenu)
        self.vehicleMenu.add_command(label='Add Vehicle',command=lambda :addvehicle.Main())
        self.vehicleMenu.add_command(label='View vehicle',command=lambda :viewvehicle.Main())

        self.vehicleMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Profile', menu=self.vehicleMenu)
        self.vehicleMenu.add_command(label='Change Password', command=lambda :changetollpassword.Main(tollID))
        self.vehicleMenu.add_command(label='Logout',command=lambda :self.root.destroy())

        self.vehicleMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='New pass', menu=self.vehicleMenu)
        self.vehicleMenu.add_command(label='Issue pass', command=lambda: issue_pass.Main())
        self.vehicleMenu.add_command(label='View pass', command=lambda: view_issuepass.Main())


        self.rootMenu.add_command(label='Entry',command=lambda: viewentry.Main())
        self.rootMenu.add_command(label='Transaction',command=lambda: viewtransaction.Main())
        self.rootMenu.add_command(label='Detect',command=lambda: self.openDemoWindow())



        self.mainLabel = Label(self.root, text=f"Welcome {tollName}", font=('calibri', 28, 'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.root.mainloop()

    def openDemoWindow(self):
        self.root.withdraw()
        tollDemo.Main(self.tollID)

#obj = Main()