from tkinter import *
import qrcode
from resizeimage import resizeimage
from PIL import Image,ImageTk
class Qr:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Employee QR generator|created by Priya Kandu")
        self.root.resizable(False,False)

        #header of the appplication
        title=Label(self.root,text="Employee QR Generator",font=("Consolas",30),bg='#DA6464',fg='#F7EFEF',anchor="w").place(x=0,y=0,relwidth=1)


        #variables
        self.id=StringVar()
        self.name=StringVar()
        self.department=StringVar()
        self.designation=StringVar()

        #details of the employee(frame 1)
        details_frame=Frame(self.root,bd=3,relief=RIDGE,bg='#DA6464')
        details_frame.place(x=40,y=70,width=500,height=400)
        details_title=Label(details_frame,text="Employee Details",font=("Verdana",20),bg='#F7EFEF',fg='#DA6464').place(x=0,y=0,relwidth=1)

        #labels for the employee
        id=Label(details_frame,text="Employee ID",font=("Verdana",15,'bold'),bg='#DA6464',fg='#F7EFEF',anchor="w").place(x=0,y=45,relwidth=1)
        name=Label(details_frame,text="Name",font=("Verdana",15,'bold'),bg='#DA6464',fg='#F7EFEF',anchor="w").place(x=0,y=90,relwidth=1)
        department=Label(details_frame,text="Department",font=("Verdana",15,'bold'),bg='#DA6464',fg='#F7EFEF',anchor="w").place(x=0,y=135,relwidth=1)
        designation=Label(details_frame,text="Designation",font=("Verdana",15,'bold'),bg='#DA6464',fg='#F7EFEF',anchor="w").place(x=0,y=180,relwidth=1)

        #entries for the employee
        txt_id=Entry(details_frame,textvariable=self.id,font=("Verdana",15,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=165,y=45)
        txt_name=Entry(details_frame,textvariable=self.name,font=("Verdana",15,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=165,y=90)
        txt_department=Entry(details_frame,textvariable=self.department,font=("Verdana",15,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=165,y=135)
        txt_designation=Entry(details_frame,textvariable=self.designation,font=("Verdana",15,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=165,y=180)

        #buttons
        generate_btn=Button(details_frame,command=self.generate,text="Generate Id",font=("Verdana",14,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=30,y=280,height=50,width=180)
        clear_btn=Button(details_frame,command=self.clear,text="Clear",font=("Verdana",14,'bold'),bg='#F7EFEF',fg='#DA6464').place(x=230,y=280,height=50,width=180)

        #labels for message
        self.msg=""
        self.lbl_msg=Label(details_frame,text=self.msg,font=("Verdana",14),bg='#DA6464')
        self.lbl_msg.place(x=0,y=345,relwidth=1)

        #id of the employee(frame 2)
        qr_frame=Frame(self.root,bd=3,relief=RIDGE,bg='#DA6464')
        qr_frame.place(x=550,y=70,width=320,height=400)
        qr_title=Label(qr_frame,text="Generate ID",font=("Verdana",20),bg='#F7EFEF',fg='#DA6464').place(x=0,y=0,relwidth=1)

        #body of second frame
        self.img_lbl=Label(qr_frame,text="ID Not Found!!..",font=("Verdana",15),bg='#F7EFEF',fg='#DA6464',bd=1,relief=RIDGE)
        self.img_lbl.place(x=50,y=100,width=200,height=200)

    def clear(self):
        self.id.set('')
        self.name.set('')
        self.department.set('')
        self.designation.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg,bg='#DA6464')
        self.img_lbl.config(image='')


    def generate(self):
        if self.id.get()=="" or self.name.get()=="" or self.department.get()=="" or self.designation.get()=="" :
            self.msg="All fields are required!!!"
            self.lbl_msg.config(text=self.msg,fg="red",bg='#F7EFEF')
        else:
            qr_data=(f"Empployee Id:\t{self.id.get()} \n Empployee Name:\t{self.name.get()} \n Empployee Department:\t{self.department.get()} \n Employee Designation:\t{self.designation.get()} \n")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save(str(self.id.get())+".png")

            self.im=ImageTk.PhotoImage(file=str(self.id.get())+".png")
            self.img_lbl.config(image=self.im)

            self.msg="Id generated sucessfully!!"
            self.lbl_msg.config(text=self.msg,fg='#048B0D',bg='#F7EFEF')
    


root=Tk()
obj=Qr(root)
root.mainloop()
