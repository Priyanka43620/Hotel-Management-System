from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
       self.root=root
       self.root.title("Hotel Management System")
       self.root.geometry("1295x550+230+220")

       #=========variable======================
       self.var_ref=StringVar()
       x=random.randint(1000,9999)
       self.var_ref.set(str(x))

       self.var_cust_name=StringVar()
       self.var_Father=StringVar()
      
       self.var_gender=StringVar()
       self.var_post=StringVar()
       self.var_mobile=StringVar()
       self.var_email=StringVar()
       self.var_nationality=StringVar()
       self.var_address=StringVar()
       self.var_id_proof=StringVar()
       self.var_id_number=StringVar()

       #================ title ===================
       
       lbl_title= Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
       lbl_title.place(x=0,y=0,width=1295,height=50)

       #=============== logo ======================

       img2 =Image.open(r"C:\photos\Royal-Hotel-logo.webp")
       img2 =img2.resize((100,40),Image.Resampling.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
       lblimg.place(x=5,y=2,width=100,height=40)

       #==============labelFrame===================
        
       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
       labelframeleft.place(x=5,y=50,width=425,height=490)

       #=============labels and entries=============
       # custRef
       lbl_cust_ref= Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
       lbl_cust_ref.grid(row=0,column=0,sticky=W)

       entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
       entry_ref.grid(row=0,column=1)

       #cust name
       cname= Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
       cname.grid(row=1,column=0,sticky=W)

       txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
       txtcname.grid(row=1,column=1)

       #father name
       lblmname= Label(labelframeleft,text="Father Name",font=("arial",12,"bold"),padx=2,pady=6)
       lblmname.grid(row=2,column=0,sticky=W)

       txtmname=ttk.Entry(labelframeleft,textvariable=self.var_Father,font=("arial",13,"bold"),width=29)
       txtmname.grid(row=2,column=1)

       #gender combobox
       label_gender= Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
       label_gender.grid(row=3,column=0,sticky=W)
       combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
       combo_gender["value"]=("Male","Female","Other")
       combo_gender.current(0)
       combo_gender.grid(row=3,column=1)

       # post code
       lblPostCode= Label(labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
       lblPostCode.grid(row=4,column=0,sticky=W)

       txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
       txtPostCode.grid(row=4,column=1)

       #mobile number
       lblMobile= Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
       lblMobile.grid(row=5,column=0,sticky=W)

       txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
       txtMobile.grid(row=5,column=1)

       # email
       lblEmail= Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
       lblEmail.grid(row=6,column=0,sticky=W)

       txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
       txtEmail.grid(row=6,column=1)

       # nationality
       lblNationality= Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
       lblNationality.grid(row=7,column=0,sticky=W)

       combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
       combo_Nationality["value"]=("Indian","American","Britist")
       combo_Nationality.current(0)
       combo_Nationality.grid(row=7,column=1)

       # id proof type combobox

       lblIdProof= Label(labelframeleft,text="Id Proof",font=("arial",12,"bold"),padx=2,pady=6)
       lblIdProof.grid(row=8,column=0,sticky=W)
       combo_Id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
       combo_Id["value"]=("Aadhar","Driving licence","Passport")
       combo_Id.current(0)
       combo_Id.grid(row=8,column=1)

       # id number
       lblIdNumber= Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
       lblIdNumber.grid(row=9,column=0,sticky=W)

       txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
       txtIdNumber.grid(row=9,column=1)

       # address
       lblAddress= Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
       lblAddress.grid(row=10,column=0,sticky=W)

       txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
       txtAddress.grid(row=10,column=1)

       #======= buttons================

       btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
       btn_frame.place(x=0,y=400,width=412,height=40)

       btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnAdd.grid(row=0,column=0,padx=1)

       
       btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnUpdate.grid(row=0,column=1,padx=1)

       
       btnDelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnDelete.grid(row=0,column=2,padx=1)

       
       btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnReset.grid(row=0,column=3,padx=1)

       #============= table frame====================================
       
       Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
       Table_Frame.place(x=435,y=50,width=860,height=490)

       lblSearchBy= Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
       lblSearchBy.grid(row=0,column=0,sticky=W)

       self.search_var=StringVar()

       combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
       combo_Search["value"]=("Search Option","Mobile","Ref")
       combo_Search.current(0)
       combo_Search.grid(row=0,column=1)

       self.txt_search=StringVar()

       txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
       txtSearch.grid(row=0,column=2,padx=2)

       btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnSearch.grid(row=0,column=3,padx=1)

       
       btnshowAll=Button(Table_Frame,text="Show all",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
       btnshowAll.grid(row=0,column=4,padx=1)

       #======== Show data Table ===============================

       details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
       details_table.place(x=0,y=50,width=860,height=350)

       scroll_x= ttk.Scrollbar(details_table,orient=HORIZONTAL)
       scroll_y= ttk.Scrollbar(details_table,orient=VERTICAL)

       self.Cust_details_Table=ttk.Treeview(details_table,column=("ref","name","Father name","gender","post","mobile",
                                                                  "email","nationality","idproof","id number","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.Cust_details_Table.xview)
       scroll_y.config(command=self.Cust_details_Table.yview)

       self.Cust_details_Table.heading("ref",text="Refer No")
       self.Cust_details_Table.heading("name",text="Name")
       self.Cust_details_Table.heading("Father name",text="Father Name")
       self.Cust_details_Table.heading("gender",text="Gender")
       self.Cust_details_Table.heading("post",text="Post code")
       self.Cust_details_Table.heading("mobile",text="Mobile")
       self.Cust_details_Table.heading("email",text="Email")
       self.Cust_details_Table.heading("nationality",text="nationality")
       self.Cust_details_Table.heading("idproof",text="Id Proof")
       self.Cust_details_Table.heading("id number",text="Id Number")
       self.Cust_details_Table.heading("address",text="Address")

       self.Cust_details_Table['show']="headings"

       self.Cust_details_Table.column("ref",width=90)
       self.Cust_details_Table.column("name",width=90)
       self.Cust_details_Table.column("Father name",width=90)
       self.Cust_details_Table.column("gender",width=90)
       self.Cust_details_Table.column("post",width=90)
       self.Cust_details_Table.column("mobile",width=90)
       self.Cust_details_Table.column("email",width=90)
       self.Cust_details_Table.column("nationality",width=90)
       self.Cust_details_Table.column("idproof",width=90)
       self.Cust_details_Table.column("id number",width=90)
       self.Cust_details_Table.column("address",width=90)
       


       self.Cust_details_Table.pack(fill=BOTH,expand=1)
       self.Cust_details_Table.bind("<ButtonRelease-1>",self.__getattribute__)
       self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_Father.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Priya@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_ref.get(),
                                        self.var_cust_name.get(),
                                        self.var_Father.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nationality.get(),
                                        
                                        self.var_id_proof.get(),
                                        self.var_id_number.get(),
                                        self.var_address.get()

                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priya@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close
                                           
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            
                conn=mysql.connector.connect(host="localhost",user="root",password="Priya@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("update customer set name=%s, Father name=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,id number=%s,address=%s where ref=%s",(
                                                                                                                                                          
                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                        self.var_Father.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_post.get(),
                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_nationality.get(),
                                        
                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                        self.var_address.get(),  
                                                                                                                                                        self.var_ref.get() ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Customer has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("hotel management system","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Priya@123",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:                return
            
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_Father.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
       # self.var_nationality.set(""),
       # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
       
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Priya@123",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute(" select* from customer where " + str(self.search_var.get())+ "LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("", END, values=i)

        conn.close()
            
                    














if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()