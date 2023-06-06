from tkinter import*
import tkinter.messagebox as msg
import connection
import re

class Main :
    def __init__(self):
        self.backgroundcolour = '#92A9BD'
        self.maincolor = '#B9EDDD'
        self.btncolor = '#B9EDDD'
        self.lb0color = '#87CBB9'
        self.activebutton = '#87CBB9'
        self.framecolor = '#87CBB9'

        self.root=Tk()
        self.root.title("Details")
        self.root.configure(background=self.backgroundcolour)
        self.root.geometry('600x500')
        self.mainLabel=Label(self.root,text='Add Category',font=('arial',20,'bold'),bg=self.maincolor,borderwidth=4,relief=SUNKEN)
        self.mainLabel.pack(pady=20)
        self.f=Frame(self.root,bg=self.framecolor,height=30,highlightthickness=5)
        self.f.pack(pady=10)
        self.font=('calibri',14)

        self.lb1=Label(self.f,text='Enter Name',font=self.font,bg=self.lb0color)
        self.txt1=Entry(self.f,width=25,font=self.font,relief=SOLID)
        self.lb1.grid(row=0,column=0,padx=10,pady=10)
        self.txt1.grid(row=0,column=1,padx=10,pady=10)

        self.lb2 = Label(self.f, text='Enter Description', font=self.font,bg=self.lb0color)
        self.txt2 = Entry(self.f, width=25, font=self.font,relief=SOLID)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.btn=Button(self.root,text='Submit',font=self.font,command=self.insert,bg=self.btncolor,activebackground=self.activebutton)
        self.btn.pack(pady=10)
        self.root.mainloop()

    def insert(self):
        name=self.txt1.get()
        description=self.txt2.get()

        if len(name) == 0 or len(description) == 0:
            msg.showwarning('Warning', 'Please Enter Values.', parent=self.root)
        else:
            if bool(re.match('[a-zA-Z\s]+$', name)):
                conn=connection.Connect()
                cr=conn.cursor()
                try:
                    q=f"insert into category values('{name}','{description}')"
                    cr.execute(q)
                    conn.commit()
                    msg.showinfo('Success','Data Entered Successfully',parent=self.root)
                    self.txt1.delete(0,'end')
                    self.txt2.delete(0, 'end')
                except:
                    msg.showinfo('Warning', "Category Already Exists. ",parent=self.root)
            else:
                msg.showwarning("Warning", 'Name only contains Alphabets and Space.')

if __name__ == '__main__':
    obj=Main()