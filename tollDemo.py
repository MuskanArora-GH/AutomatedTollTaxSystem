import datetime
import tkinter.tix
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import cv2
from connection import Connect
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename
import plateDemo2
import pytesseract as pyt
import numpy as np
import dashboard1



class Main:
    def __init__(self,tollid):
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')
        windowColor = '#242424'
        frameColor = '#2b2b2b'
        self.root = customtkinter.CTkToplevel()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        # print(sw, sh)
        self.root.geometry(f"{sw}x{sh}+0+0")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.sideFrame1 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3))
        self.sideFrame1.pack_propagate(0)
        self.sideFrame2 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3 * 2))
        self.sideFrame2.pack_propagate(0)
        self.sideFrame1.grid(row=0, column=0, padx=10, pady=20)
        self.sideFrame2.grid(row=0, column=1, padx=10, pady=20)

        self.mainLabel2 = customtkinter.CTkButton(self.sideFrame1, text='Automated Toll Payment System',
                                                  font=('arial', 26))
        self.mainLabel2.pack(pady=60)

        self.formFrame = customtkinter.CTkFrame(self.sideFrame1)
        self.formFrame.pack(pady=10, expand=True)
        self.mainLabel1 = customtkinter.CTkButton(self.formFrame, text='Pay Toll', font=('arial', 20), width=200)
        self.mainLabel1.pack(pady=20)

        # self.lb1 = Label(self.formFrame, text='Enter Vehicle Number', bg=frameColor, font=('arial', 12), fg='white')
        # self.lb1.grid(row=0, column=0)
        self.txt1 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Enter Vehicle Number', width=400)
        # self.txt1.grid(row=0, column=1, padx=10)
        self.txt1.pack(pady=10)
        self.btn1 = customtkinter.CTkButton(self.formFrame, text='Search', command=self.searchVehicle)
        self.btn1.pack(pady=10)
        self.txt2 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Vehicle ID', width=400)
        self.txt2.pack(pady=10)
        self.txt3 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt3.insert(0, datetime.date.today())
        self.txt3.pack(pady=10)
        self.txt4 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt4.insert(0, datetime.datetime.now().time())
        self.txt4.pack(pady=10)
        self.txt5 = customtkinter.CTkComboBox(self.formFrame, width=400, values=['Cash', 'Monthly Pass'],
                                              state='readonly')
        self.txt5.pack(pady=10)
        self.txt5.set('Cash')
        self.txt6 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt6.insert(0, '0')
        self.txt6.pack(pady=10, padx=10)

        self.txt7 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt7.insert(0, tollid)
        self.txt7.pack(pady=10, padx=10)
        self.txt7.configure(state='readonly')
        self.btn2 = customtkinter.CTkButton(self.formFrame, text='Submit', command=self.submitForm)
        self.btn2.pack(pady=10)

        self.displayFrame = customtkinter.CTkFrame(self.sideFrame2)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)

        self.label = Label(self.displayFrame)
        self.label.pack(anchor=NE)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)




        self.btnFrame = customtkinter.CTkFrame(self.sideFrame2, width=int(sw / 3 * 1.3) + 200)
        self.btnFrame.pack(pady=10, padx=10)
        self.btnFrame.pack_propagate(0)
        self.cameraButton = customtkinter.CTkButton(self.btnFrame, text='Open Camera', command=self.openCamera,font=('arial', 20), width=200)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=10)
        self.imageButton = customtkinter.CTkButton(self.btnFrame, text='Select Image', font=('arial', 20), width=200,
                                                   command=self.selectImage)
        self.imageButton.grid(row=0, column=1, pady=20, padx=10)
        self.themeButton = customtkinter.CTkButton(self.btnFrame, text='Dark Theme', font=('arial', 20), width=200,
                                                   command=self.changeTheme)
        self.themeButton.grid(row=0, column=2, pady=20, padx=10)
        # self.root.attributes('-topmost',True)

        self.root.mainloop()

    def fetchText(self, file):
        img = cv2.imread(file)
        img = cv2.resize(img, (700, 490))
        # pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pyt.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
        print(plateCascade)

        getCoordinates = plateCascade.detectMultiScale(image=img, scaleFactor=1.1, minNeighbors=4)
        self.text = ''
        for (x, y, w, h) in getCoordinates:
            a, b = (int(0.02 * img.shape[0]), int(0.025 * img.shape[1]))
            plate = img[y:y + h, x:x + w]
            kernal = np.ones((1, 1), np.uint8)
            plate = cv2.dilate(src=plate, kernel=kernal, iterations=1)
            plate = cv2.erode(src=plate, kernel=kernal, iterations=1)

            plateGray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
            (thresh, plate) = cv2.threshold(plateGray, 127, 255, cv2.THRESH_BINARY)

            self.text = pyt.image_to_string(plate)
            self.text = ''.join(e for e in self.text if e.isalnum())
            print(self.text)
            # cv2.imwrite(filename='newPlate.png',img=plate)
            cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
            cv2.putText(img, self.text, (x, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 3)

        # cv2.imshow('Image',plate)
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        self.txt1.delete(0, 'end')
        self.txt1.insert(0, self.text)

    def selectImage(self):
        file = askopenfilename()
        self.fetchText(file)

    def submitForm(self):
        id = self.txt2.get()
        date = self.txt3.get()
        time = self.txt4.get()
        type = self.txt5.get()
        amount = self.txt6.get()

        conn = Connect()
        cr = conn.cursor()
        q = f"insert into entry values (null, '{id}', '{date}','{time}', '{type}','{self.txt7.get()}')"
        cr.execute(q)
        conn.commit()
        if type == 'Cash':
            q = f"insert into transaction values (null, '{id}','{date}','{time}', '{amount}','{self.txt7.get()}')"
            print(q)
            cr.execute(q)
            conn.commit()
        msg.showinfo('Success', "Entry has been Marked.", parent=self.root)
        self.txt1.delete(0,'end')
        self.txt2.delete(0,'end')
        self.txt3.delete(0,'end')
        self.txt4.delete(0,'end')
        self.txt6.delete(0,'end')
        self.txt5.set('')
        self.txt3.insert(0, datetime.date.today())
        self.txt4.insert(0, datetime.datetime.now().time())



    def searchVehicle(self):
        number = self.txt1.get()
        if len(number) == 0:
            msg.showwarning('Warning', 'PLease Enter Number First', parent=self.root)
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"select id, category from vehicle where vehicle_number = '{number}'"
            cr.execute(q)
            data = cr.fetchall()
            if len(data) == 0:
                msg.showwarning('Warning', 'Vehicle not Registered.', parent=self.root)
            else:
                self.txt2.delete(0, 'end')
                self.txt2.insert(0, data[0][0])
                q = f"select id from issue_monthlypass where vehicle_id = '{data[0][0]}' and expiry_date > {datetime.date.today()}"
                cr.execute(q)
                data1 = cr.fetchall()
                if len(data1) == 0:
                    msg.showwarning('Warning', 'No Valid Pass Found', parent=self.root)
                    q = f"select price from tollprice where category='{data[0][1]}'"
                    cr.execute(q)
                    price = cr.fetchone()
                    self.txt5.set('Cash')
                    self.txt6.delete(0, 'end')
                    self.txt6.insert(0, price[0])
                else:
                    self.txt5.set('Monthly Pass')
                    self.txt6.delete(0, 'end')
                    self.txt6.insert(0, '0')

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.show_frames()
        self.cameraButton.configure(command=self.closeCamera, text='Close Camera')
        self.btn3 = customtkinter.CTkButton(self.btnFrame, text="Capture", command=self.fetchTextFromFrame)
        self.btn3.grid(row=0,column=3)

    def fetchTextFromFrame(self):
        self.txt1.delete(0, 'end')
        img = self.frame
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (700, 500))
        # pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pyt.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
        print(plateCascade)

        getCoordinates = plateCascade.detectMultiScale(image=img, scaleFactor=1.1, minNeighbors=4)
        self.text = ''
        for (x, y, w, h) in getCoordinates:
            a, b = (int(0.02 * img.shape[0]), int(0.025 * img.shape[1]))
            plate = img[y:y + h, x:x + w]
            kernal = np.ones((1, 1), np.uint8)
            plate = cv2.dilate(src=plate, kernel=kernal, iterations=1)
            plate = cv2.erode(src=plate, kernel=kernal, iterations=1)

            plateGray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
            (thresh, plate) = cv2.threshold(plateGray, 127, 255, cv2.THRESH_BINARY)

            self.text = pyt.image_to_string(plate)
            self.text = ''.join(e for e in self.text if e.isalnum())
            print(self.text)
            # cv2.imwrite(filename='newPlate.png',img=plate)
            cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
            cv2.putText(img, self.text, (x, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 3)

        # cv2.imshow('Image',plate)
        cv2.imshow('Image', img)
        cv2.waitKey(0)

        self.txt1.insert(0, self.text)

    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.camLabel.configure(image='')
        self.cameraButton.configure(command=self.openCamera, text='Open Camera')
        self.btn3.destroy()


    def show_frames(self):
        # Get the latest frame and convert into Image
        self.frame = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        self.frame = cv2.flip(self.frame, 1)
        img = Image.fromarray(self.frame)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        self.camLabel.imgtk = imgtk
        self.camLabel.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        self.camLabel.after(20, self.show_frames)

    def changeTheme(self):
        if self.themeButton.cget('text') == 'Dark Theme':
            customtkinter.set_appearance_mode('dark')
            self.themeButton.configure(text='Light Theme')
        else:
            customtkinter.set_appearance_mode('light')
            self.themeButton.configure(text='Dark Theme')


#obj = Main()