from tkinter import *
from PIL import Image, ImageTk

import adminlogin
import tollplazalogin


# import faceDemo


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        img = Image.open('m2.jpg')
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        canvas.pack(fill='both', expand=True)

        canvas.create_image(0, 0, image=bg, anchor='nw')

        canvas.create_text(800, 50, text="Automated Toll Payment System", font=('Constantia', 70), fill='#C4F1BF')


        self.rootMenu = Menu(self.root)
        self.root.configure(menu=self.rootMenu)

        self.rootMenu.add_command(label='Admin', command=lambda :adminlogin.Main())
        self.rootMenu.add_command(label='Toll Plaza', command=lambda :tollplazalogin.Main())
        self.rootMenu.add_command(label='Exit', command=lambda :self.root.destroy())



        self.root.mainloop()


obj = Main()
