from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
import pymysql
from PIL import ImageTk,Image
import pickle
from datetime import datetime
import random


pas=""
name=""
address=""
totalroom=100
remainingroom=0

db=pymysql.connect("localhost","root","","")

 
try:
   

    db.cursor().execute("create database hotelm")
   
    db=pymysql.connect("localhost","root","","hotelm")
   
    
    db.cursor().execute("create table login(ID int(10) Unique,User varchar(20),Password varchar(20),pin varchar(5));")
  
    
    db.cursor().execute("""insert into login(ID,User,Password,pin) values('%s','%s','%s','%s')"""%("1","admin","1234","0000"))
    db.cursor().execute("""create table roominfo(sno int(10) Unique AUTO_INCREMENT,roomleft varchar(20),roominuse varchar(20));""")
    db.cursor().execute("""insert into roominfo(sno,roomleft,roominuse)values('%s','%s','%s')"""%("1",totalroom,remainingroom))
    db.cursor().execute("""create table roomdetail(sno int(10) Unique AUTO_INCREMENT,roomgiven varchar(255),ID varchar(20));""")
    db.cursor().execute("create table Info(ID int(100) Unique AUTO_INCREMENT,Name varchar(200),PhoneNO varchar(255),Email varchar(200),Gender varchar(200),Roomtype varchar(200),Address varchar(200),AdharcardNo varchar(200),checkindate varchar(100),checkoutdate varchar(100),room varchar(100));")
    print("asd")
    db.commit()
    db.close()
    
except:
    print()
    
    


db=pymysql.connect("localhost","root","","hotelm")
c=db.cursor()
c.execute("select User,Password,pin from login where id=1")
results = c.fetchall()

print(results)

def start():
     def now():
         qea.destroy()
         login()
     qea=Tk()
     width, height=qea.winfo_screenwidth(), qea.winfo_screenheight()
     qea.geometry('%dx%d+0+0' %(width,height))
        
     qea.title("welcome")

     imoo=ImageTk.PhotoImage(Image.open("img.png"),master=qea)
     qqee=Label(qea,image=imoo)
    
     qqee.place(x=0, y=0)

     le=Label(qqee,text="WELCOME TO 5 STAR",font=("clibri",40),bg="blue")
     le.place(x=500,y=2)

     ob=Button(qqee,text="Continue",height=5,width=20,command=now)
     ob.place(x=700,y=400)
     qea.mainloop()

    
def des (root):
    root.destroy()    
def login():
    def close_window (root): 
        root.destroy()
    
    
    ##login page
    def welhotel():
        if(e.get()==results[0][0] and e1.get()==results[0][1]):
            tk.destroy()
            menu()
        elif(e.get()=="" or e1.get()==""):
            messagebox.showinfo("error","Empty Field")
                
        else:
            messagebox.showinfo("error","wrong password")

    def fgt():
        def rest():
            
            def chg():
                
                if(e1.get()!= ""):
                    pas=e1.get()
                    c.execute("""update login set Password='%s' where ID=1;"""%(pas))
                    db.commit()
                    pas=""
                    c.execute("select User,Password,pin from login where id=1")
                    results=[]
                    results= c.fetchall()
                    messagebox.showinfo("req","please restart the program to update the password")
                    db.close()
                
                else:
                     messagebox.showinfo("error","Empty Field")
                tk2.destroy()
                    
            tk2=Tk()
            tk2.geometry("200x200")
            if(e2.get()==results[0][2]):
                tk3.destroy()
                l=Label(tk2,text="Enter New Password",bg="RED")
                l.place(x=10,y=30)
                e1=Entry(tk2,show="*",width=10,font=30)
                e1.place(x=40,y=50)
                b=Button(tk2,text="Submit",height=2,width=10,command=chg)
                b.place(x=100,y=100)
               
            else:
                messagebox.showinfo("error","wrong pin")
                
            
        tk3=Tk()
        tk3.geometry("250x250")
        l=Label(tk3,text="Security Checking  \n Enter your pin ",bg="RED")
        l.place(x=10,y=10)
        e2=Entry(tk3,width=10,font=60,show="*")
        e2.place(x=50,y=60)
        b=Button(tk3,text="Submit",height=2,width=10,command=rest)
        b.place(x=100,y=100)
    ##login end
    tk=Tk()
    width, height=tk.winfo_screenwidth(), tk.winfo_screenheight()
    tk.geometry('%dx%d+0+0' %(width,height))
    imga=ImageTk.PhotoImage(Image.open("kk.png"))
    q=Label(tk,image=imga)
    q.place(x=0,y=0)
    tk.title("Login Page")
    lo=Label(q,text="Login Page",font=("clibri",40),fg="grey")
    lo.place(x=700,y=30)
    l=Label(q,text="Username",bg="blue",font=("clibri",15))
    l.place(x=180,y=300)
    l1=Label(q,text="Password",bg="blue",font=("clibri",15))
    l1.place(x=180,y=450)
    
    e=Entry(q,width=15,font=50)
    e.place(x=300,y=300)
    e1=Entry(q,show="*",width=15,font=50)
    e1.place(x=300,y=450)
    b=Button(q,text="Submit",height=2,width=10,command=welhotel)
    b.place(x=500,y=500)
    b2=Button(q,text="Forget",height=2,width=10,command=fgt)
    b2.place(x=600,y=500)
    tk.mainloop()

def menu():
    def cc():
        tk7.destroy()
        hotel()
    def bb():
        tk7.destroy()
        cod()

    def dd():
        def correct(inp):
            if inp=="":
                return True
            else:
                try:
                    inp=int(inp)
                except:
                    return False
                else:
                    return True
        def eo():
            if(ex.get()!=""):
                try:
                    
                    c.execute("""select * from info where id = '%s'"""%(ex.get()))
                    f=c.fetchall()
                    c.execute("""select roomgiven from roomdetail where id = '%s'"""%(f[0][0]))
                    ff=c.fetchall()
                    if (len(f)==0 or len(ff)==0):
                        messagebox.showinfo("error","Id does not exist")
                    else:
                        
                        scrolW = 30 
                        scrolH = 3

                        st="ID :"+str(f[0][0])+"\nNAME : "+str(f[0][1])+"\nPHONE NO. :"+str(f[0][2])+"\nEMAIL :"+str(f[0][3])+"\nGENDER :"+str(f[0][4])+"\nROOMTYPE :"+str(f[0][5])+"\nADDRESS : "+str(f[0][6])+"\nADHARNO. : "+str(f[0][7])+"\nCHECK IN DATE : "+str(f[0][8])+"\nCHECK OUT DATE :"+str(f[0][9])+"\nNUMBER OF ROOMS :"+str(f[0][10])+"\n ROOM NO. " +str(ff[0][0])
                        

                        
                        text=Text(qe)

                        w=Text(qqe)
                        text.insert(INSERT,st)
                        text.place(x=50,y=150)
                except:
                        messagebox.showinfo("error","Id does not exist")

              
                
            else:
                messagebox.showinfo("error","Empty Field")
                qe.destroy()
        qe=Tk()
        qe.geometry("700x500")    
        
        qe.title("Detail")
        
        
        
        imo=ImageTk.PhotoImage(Image.open("kk.png"),master=qe)
        qqe=Label(qe,image=imo)
        qqe.place(x=0,y=0)

        
        
        
        l1=Label(qqe,text="DETAIL",bg="green",font=("clibri",30))
        l1.place(x=65,y=5)

        l2=Label(qqe,text="Enter your ID",font=40)
        l2.place(x=5,y=90)

        ex=Entry(qqe,width=10)
        cho=ex.register(correct)
        ex.config(validate="key",validatecommand =(cho,'%P'))
        ex.place(x=120,y=90,height=30,width=100)


        be=Button(qqe,text="ok",command=eo)
        be.place(x=230,y=90,height=30,width=40)

        

      


        

        

        qe.mainloop()




        
    tk7=Tk()
   
   


    width, height=tk7.winfo_screenwidth(), tk7.winfo_screenheight()
    tk7.geometry('%dx%d+0+0' %(width,height))
    
    im=ImageTk.PhotoImage(Image.open("menu1.jpg"),master=tk7)
    w=Label(tk7,image=im)
    w.place(x=0,y=0)

    le=Label(w,text="WELCOME TO 5 STAR",font=("clibri",40),bg="red",fg="white")
    le.place(x=500,y=2)

    imoo=ImageTk.PhotoImage(Image.open("cin.png"),master=w)
    w1=Label(w,image=imoo)
    w1.place(x=250,y=200)

    
    imooo=ImageTk.PhotoImage(Image.open("cout.jfif"),master=w)
    w2=Label(w,image=imooo)
    w2.place(x=650,y=200)

    
    imoooo=ImageTk.PhotoImage(Image.open("de.png"),master=w)
    w2=Label(w,image=imoooo)
    w2.place(x=1050,y=200)
    

    b=Button(w,text="Check In",bg="grey",fg="white",command=cc)
    b.config(height=5,width=20)
    b.place(x=300,y=500)


    
    b1=Button(w,text="Check out",bg="grey",fg="white",command=bb)
    b1.config(height=5,width=20)
    b1.place(x=700,y=500)

    b2=Button(w,text="Detail",bg="grey",fg="white",command=dd)
    b2.config(height=5,width=20)
    b2.place(x=1100,y=500)

    tk7.mainloop()
def hotel():
    k=""
    def roomgen():
            rno=[]
            for i in range(0,101):
                rno.append(i)
            xo=random.choice(rno)
            return xo
     #enter integer only function
    def correct(inp):
        if inp=="":
            return True
        else:
            try:
                inp=int(inp)
            except:
                return False
            else:
                return True
    
    
    def store():
        pas=int(e14.get())
        print(pas)
        xo=[]
        amp=roomcheck(pas)
        if(amp != 9999):
            xo.append(amp)
        else:
            messagebox.showinfo("error","room not available")
            
        if(e.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or numberChosen.get()=="" or e7.get()=="" or e8.get()=="" or e9.get()=="" or e10.get()=="" or nnk.get()=="" or e14.get()==""  ):
            messagebox.showinfo("error","Empty Field")
        else:
            if(var.get()==0):
                k="AC"
            elif(var.get()==1):
                k="NonAC"
            date=n.get()+"-"+nn.get()+"-"+nnk.get()
            address=e7.get()+e8.get()+e9.get()
            name=e.get()+e2.get()
            pp=e3.get()
            
            db.cursor().execute("""insert into Info(Name,PhoneNO,Email,Gender,Roomtype,Address,AdharcardNo,checkindate,room) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name,e3.get(),e4.get(),numberChosen.get(),k,address,e10.get(),date,e14.get()))
            db.commit()
           
                
            k=""
            address=""
            name=""
            date=""
            c=db.cursor()
            c.execute("""select ID from Info where PhoneNO='%s'"""%(pp))
            ch=c.fetchall()
            db.cursor().execute("""insert into roomdetail (roomgiven,ID) values('%s','%s')"""%(xo,ch[0][0]) )
            db.commit()
            

            
            
            c="YOUR ROOM NO. IS  "+str(xo)+ "  AND ID IS "+str(ch[0][0])+" REMEMBER YOUR ID"
            messagebox.showinfo("Done",c)
            pp=""
            c=""
            ch=""
            tk4.destroy()
            menu()                    
                       
    def roomcheck( che):
        
        c.execute("select roomleft,roominuse from roominfo where sno='1'")
        detail=c.fetchall()
        print(detail)
        av=int(detail[0][0])
        con=int(detail[0][1])
        if(av>che):
            av=av-int(che)
            con=con+int(che)
            db.cursor().execute("""update roominfo set roominuse='%s',roomleft='%s' where sno='1'  """%(con,av) )
            db.commit()
            xo=[]
            ae=0
            for i in range (0,int(che)):
                ae=roomgen()
                xo.append(ae)
        
            if(c.execute("select roomgiven from roomdetail where roomgiven='%s'"%(xo))):
                print("room exist")
            
            
            
            else:
                print("room does not exist")
            return xo
            
        else:
            messagebox.showinfo("Notice","Only " +str(av)  +"Room Available")
            return 9999
        
        
            
        
           
    def ex():
        tk4.destroy()
    def awm():
        tk4.destroy()
        menu()
    tk4=Tk()
    tk4.title("WELCOME TO HOTEL")
    width, height=tk4.winfo_screenwidth(), tk4.winfo_screenheight()
    tk4.geometry('%dx%d+0+0' %(width,height))
    imgg=ImageTk.PhotoImage(Image.open("img4.png"))
    ww=Label(tk4,image=imgg)
    ww.place(x=0,y=0)
    le=Label(ww,text="WELCOME TO 5 STAR",font=("clibri",40),bg="blue")
    le.place(x=500,y=2)

    l1=Label(ww,text="First Name",font="40")
    l1.place(x=10,y=100)
    
    e=Entry(ww,width=15,font=20)
    e.place(x=150,y=100)
    
    l2=Label(ww,text="Last Name",font="40")
    l2.place(x=10,y=140)
    
    e2=Entry(ww,width=15,font=20)
    e2.place(x=150,y=140)

    l3=Label(ww,text="Phone No.",font="40")
    l3.place(x=10,y=180)
    
    
    e3=Entry(ww,width=15,font=20)
    ch1=e3.register(correct)
    e3.config(validate="key",validatecommand =(ch1,'%P'))
    e3.place(x=150,y=180)

    l4=Label(ww,text="Email",font="40")
    l4.place(x=10,y=230)
    
    e4=Entry(ww,width=20,font=20)
    e4.place(x=150,y=230)

    l5=Label(ww,text="Gender",font="40")
    l5.place(x=10,y=285)
    
    number="str"
    numberChosen= ttk.Combobox(ww,state="readonly", width=12, textvariable=number)  
    #Adding Values  
    numberChosen['values']=("Male","Female","Others")  
    numberChosen.place(x=150,y=285)  
    numberChosen.current()

    l6=Label(ww,text="RoomType",font="40")
    l6.place(x=10,y=360)

    var=IntVar()
    r = Radiobutton(ww,text="AC",value=0,variable=var)
    r.place(x=150,y=360)
    r.deselect()
    r1 = Radiobutton(ww,text="NonAC",value=1,variable=var)
    r1.deselect()
    r1.place(x=200,y=360)

    l7=Label(ww,text="Address.",font="40")
    l7.place(x=700,y=100)
    
    e7=Entry(ww,width=20,font=40)
    e7.place(x=850,y=100)

    l7=Label(ww,text="House /Flat No. /Area") 
    l7.place(x=1100,y=100)

    l8=Label(ww,text="City",font="40")
    l8.place(x=700,y=140)
    
    e8=Entry(ww,width=20,font=40)
    e8.place(x=850,y=140)

    
    l9=Label(ww,text="State and country",font="40")
    l9.place(x=700,y=200)
    
    e9=Entry(ww,width=20,font=40)
    e9.place(x=900,y=200)

    l10=Label(ww,text="Aadhar Card No",font="40")
    l10.place(x=700,y=240)


     
    e10=Entry(ww,width=20,font=40)
    ch4=e10.register(correct)
    e10.config(validate="key",validatecommand=(ch4,"%P"))
    e10.place(x=900,y=240)

    l11=Label(ww,text="Check in Date",font="40")
    l11.place(x=700,y=290)
    
    n1=""
    n= ttk.Combobox(ww,state="readonly", width=2, textvariable=n1)  
    #Adding Values  
    n['values']=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")  
    n.place(x=850,y=290)  
    n.current()
    #e11.place(x=850,y=290)

    xx=""
    nn= ttk.Combobox(ww,state="readonly", width=2, textvariable=xx)
    #Adding Values  
    nn['values']=("01","02","03","04","05","06","07","08","09","10","11","12")  
    nn.place(x=890,y=290)  
    nn.current()
    #e12.place(x=900,y=290)
   

    #e13=Entry(ww,width=4,font="40")
    e13=""
    nnk=ttk.Combobox(ww,state="readonly", width=4, textvariable=e13)
    nnk['values']=("2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030")
    #e17=Entry(ww,width=4,font=40,borderwidth="3")
    nnk.place(x=930,y=290)
    nnk.current()
    

    l12=Label(ww,text="(D/M/Y)",font="40")
    
    l12.place(x=990,y=290)


    l13=Label(ww,text="No. of room required",font="40")
    l13.place(x=700,y=340)
    
    e14=Entry(ww,width=20,font="40")
    ch3=e14.register(correct)
    e14.config(validate="key",validatecommand =(ch1,'%P'))
    
    e14.place(x=900,y=340)
    

    b=Button(ww,text="Submit",font=30,bg="grey" ,command=store)
    b.place(x=500,y=500)

    b2=Button(ww,text="Back",bg="violet",command=awm)
    b2.place(x=600,y=500)
    b2.config(height=2,width=10)

    tk4.mainloop()
    



def cod():
    def leave():
        if (nn2.get()!="" and nn1.get()!="" and nn3.get()!="" and e14.get()!=""):

            
            date=nn2.get()+"-"+nn1.get()+"-"+nn3.get()
            
            db.cursor().execute("""update Info set checkoutdate='%s' where ID='%s'  """%(date,e14.get()) )
            db.commit()
            messagebox.showinfo("Updated","your slip is generated please check your folder")
            cal()
            menu()
        else:
            messagebox.showinfo("Empty","check your entrie field")
            
    def aaa():
        tk5.destroy()
        menu()

    def cal():
        inf=""
        da=""
        ac=2000
        nonac=1000
        da=int(e14.get())
        c.execute("""select checkindate,checkoutdate,Roomtype,room from Info where ID='%s'"""%(da))
        da=""
        pri = c.fetchall()
        print(pri)
        r=int(pri[0][3])
        a=str(pri[0][0])
        b=str(pri[0][1])
        fi=pri[0][2]
        bob2 = datetime.strptime(a, '%d-%m-%Y').date()
        bob = datetime.strptime(b, '%d-%m-%Y').date()
        aaa=bob-bob2
        payfinaldays=int(aaa.days)
    
        
            
    
        if(fi=="AC"):
            price=ac*payfinaldays*r
               
        else:
            price=nonac*payfinaldays*r
        
           
            
            
        ii=e14.get()
        c.execute("select ID,Name,checkindate,room,checkoutdate from Info where ID='%s'"%(ii))
        fin=c.fetchall()
        inf=("WELCOME TO 5 STAR \n ID :"+str(fin[0][0])+"\n Name : "+str(fin[0][1])+"\n Check in date : "+str(fin[0][2]) +"\n Check out Date :"+str(fin[0][4])+"\n No. of Rooms :"+str(fin[0][3])+"\n PRICE : "+str(price)+"\n THANKS FOR VISITING\n PLEASE VISIT AGAIN \n HAVE A NICE DAY")
        
        print(inf)
        
        f=open("id"+str(fin[0][0])+".txt","w")
        f.write(inf)
        inf=""
        tk5.destroy()
        
    
    

    tk5=Tk()
    width, height=tk5.winfo_screenwidth(), tk5.winfo_screenheight()
    tk5.geometry('%dx%d+0+0' %(width,height))
    imgs=ImageTk.PhotoImage(Image.open("img4.png"))
    ww=Label(tk5,image=imgs)
    ww.place(x=0,y=0)

    le=Label(ww,text="WELCOME TO 5 STAR",font=("clibri",40),bg="blue")
    le.place(x=500,y=2)

    l13=Label(ww,text="Enter your Id",font="40")
    l13.place(x=550,y=300)
        
    e14=Entry(ww,width=10,font=40,borderwidth="6")
    e14.place(x=700,y=300)

    l14=Label(ww,text="Check out Date",font="40")
    l14.place(x=550,y=380)

    nnn=""
    nn2= ttk.Combobox(ww,state="readonly", width=2, textvariable=nnn)  
    #Adding Values  
    nn2['values']=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")  
    nn2.place(x=700,y=380)  
    nn2.current()
    #e11.place(x=850,y=290)

    xxx=""
    nn1= ttk.Combobox(ww,state="readonly", width=2, textvariable=xxx)
    #Adding Values  
    nn1['values']=("01","02","03","04","05","06","07","08","09","10","11","12")  
    nn1.place(x=750,y=380)  
    nn1.current()
    
   
    e17=""
    nn3=ttk.Combobox(ww,state="readonly", width=4, textvariable=e17)
    nn3['values']=("2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030")
    #e17=Entry(ww,width=4,font=40,borderwidth="3")
    nn3.place(x=800,y=380)
    nn3.current()

    l12=Label(ww,text="(D/M/Y)",font="40")
    l12.place(x=850,y=380)

    b1=Button(ww,text="Submit",bg="violet",command=leave)
    b1.place(x=700,y=500)
    b1.config(height=2,width=10)

    b2=Button(ww,text="back",bg="violet",command=aaa)
    b2.place(x=790,y=500)
    b2.config(height=2,width=10)


    tk5.mainloop()
start()


