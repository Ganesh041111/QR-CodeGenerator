from tkinter import*
from tkinter import font
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500")
        frame=Frame(self.root,bg="powder blue")
        frame.pack(side=LEFT)
        self.root.title("QR Generator")
        self.root.resizable(False,False)

        title=Label(self.root,text=" QR GENERATOR ",font=("Albertus 25 bold"),width=43,bg="turquoise2")
        title.place(x=15,y=10)
        self.root=root
        self.root.title("QR GENERATOR")
        self.root.geometry("900x500")
        self.frame_1=Frame(root,width=900,height=500,bg="powder blue")
        self.frame_1.pack(side=LEFT)
        self.root.resizable(False,False)
        title=Label(self.root,text=" QR GENERATOR ",font=("Albertus 25 bold"),width=43,bg="turquoise2")
        title.place(x=15,y=10)


        #============Employee Details Window======================

        #============Variables==============

        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()


        emp_frame=Frame(self.root,bd=2,relief=RIDGE)
        emp_frame.place(x=15,y=78,width=540,height=400)
        title=Label(emp_frame,text=" Employee Details ",font=("Albertus 20 bold"),width=30,bg="turquoise2")
        title.place(x=11,y=10)

        title=Label(emp_frame,text=" Employee ID ",font=("Albertus 10 bold"),width=15,bg="turquoise2")
        title.place(x=85,y=60)
        title=Label(emp_frame,text=" Name ",font=("Albertus 10 bold"),width=15,bg="turquoise2")
        title.place(x=85,y=120)
        title=Label(emp_frame,text=" Department ",font=("Albertus 10 bold"),width=15,bg="turquoise2")
        title.place(x=85,y=180)
        title=Label(emp_frame,text=" Designation ",font=("Albertus 10 bold"),width=15,bg="turquoise2")
        title.place(x=85,y=240)

        Employee_ID=Entry(emp_frame, font=("times new roman",11,"bold"),textvariable=self.var_emp_code,bg="powder blue").place(x=275,y=60)
        Name=Entry(emp_frame, font=("times new roman",11,"bold"),textvariable=self.var_name,bg="powder blue").place(x=275,y=120)
        Department=Entry(emp_frame, font=("times new roman",11,"bold"),textvariable=self.var_department,bg="powder blue").place(x=275,y=180)
        Designation=Entry(emp_frame, font=("times new roman",11,"bold"),textvariable=self.var_designation,bg="powder blue").place(x=275,y=240)

        btn_generate=Button(emp_frame,text=" Generate ",command=self.generate,font=("Albertus 10 bold"),width=15,bg="turquoise2").place(x=85,y=320)
        btn_clear=Button(emp_frame,text=" Clear ",command=self.clear,font=("Albertus 10 bold"),width=15,bg="turquoise2").place(x=275,y=320)
       
        self.msg="                                         "
        self.lbl_msg=Label(emp_frame,text=self.msg ,font=("times new roman",11,"bold"),bg="powder blue")
        self.lbl_msg.place(x=160,y=360)

        #====================== QR code ==========================
        qr_frame=Frame(self.root,bd=2,relief=RIDGE)
        qr_frame.place(x=585,y=78,width=300,height=400)
        title=Label(qr_frame,text=" QR Code ",font=("Albertus 20 bold"),width=15,bg="turquoise2")
        title.place(x=16,y=10)

        self.qr_code=Label(qr_frame,text=" No QR Code\n Available",font=("Albertus 20 "),width=15,bg="white")
        self.qr_code.place(x=52,y=100,width=200,height=200)


    def generate(self):
        if self.var_designation.get()=="" or self.var_name.get()=="" or self.var_department.get()=="" or self.var_emp_code.get()=="":
            self.msg="All Fields Are Required!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\n Employee Name: {self.var_name.get()}\n Department: {self.var_department.get()}\n Employee ID: {self.var_designation.get()}\n ")
            qr_code=qrcode.make(qr_data)


            #=======Qr code image=======
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)



            #=======update msg==========
            self.msg="QR Generated Successfully!!"
            self.lbl_msg.config(text=self.msg,fg="black")
           

    def clear(self):
        self.var_emp_code.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        self.msg="                                         "
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")



root=Tk()
obj = Qr_Generator(root)
root.mainloop()