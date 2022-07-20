#imports:
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.messagebox import showinfo
import random



root=tkinter.Tk()
root.title("JUMBLED WORDS")
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
w=400
h=200
x=int(ws/2-w/2)
y=int(hs/2-h/2)
root.configure(background="paleturquoise")
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

global c,entryans,lblque,lblq,btnnext,s,l,que,ans,e,ca,p
questions={ 'TIWEH' : 'white',
      'DASI' : 'said',
      'LCSOHO' : 'school',
      'RUEPPL' : 'purple',
      'DBRI' : 'bird',
      'ATHER' : 'earth',
      'RSAM' : 'mars',
      'PEUNNTE' : 'neptune',
      'VEHAY' : 'heavy',
      'TERTEB' : 'better',
      'HISFNI':'finish',
      'OMOYD':'moody',
      'DOFUN':'found',
      'ARTST':'start',
      'RLOUOC':'colour'}


que = []
ans = []
s=0
l=len(questions)
for key, value in questions.items():
        que.append(key)
        ans.append(value)

def result():
        global p
        def quit_func():
                while(1):
                    root.destroy()
                    break
        def mainbtn_func():
                root.destroy()
                import tutorialtk
        #p=pl.get()
    
        mainwin.destroy()
        root=tkinter.Tk()
        root.title("JUMBLED WORDS")
        root.resizable(0,0)
        ws1=root.winfo_screenwidth()
        hs1=root.winfo_screenheight()
        w1=400
        h1=200
        x1=int(ws1/2-w1/2)
        y1=int(hs1/2-h1/2)
        root.configure(background="BLACK")
        data1=str(w1)+"x"+str(h1)+"+"+str(x1)+"+"+str(y1)
        root.geometry(data)
        lblr= Label(root,text="GAME OVER! \n Your score is:" +str(s+1), font=("helvetica",25,"bold"), bg='BLACK', fg='LIGHTGREEN')
        
        lblr.pack()
        exitBtn=Button(root,text='Exit',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=quit_func,relief=FLAT)
        exitBtn.place(x=30, y=150)
        mainBtn=Button(root,text='Main Menu',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=mainbtn_func,relief=FLAT)
        mainBtn.place(x=230, y=150)
    
    
    
global lblhint   

def nextq():
        global c,entryans,lblque,lblq,btnnext,s,l,que,ans,e,ca,lblhint
        lblhint.config(text="                      ")
        if entryans.get().lower()==ca.lower():
                s=s+1
                lblq.destroy()
                entryans.delete(0,END)
                game()
                #print(s)
        elif entryans.get().lower()!=ca.lower():
                #print("else")
                messagebox.showerror("WRONG CHOICE","Hey!!!That's not correct...try again")
                s=s-1



        
    
def game():
    global c,entryans,lblque,lblq,btnnext,s,l,que,ans,e,ca,index,h,lblhint
    def hint():
        
        global c,entryans,lblque,lblq,btnnext,s,l,que,ans,e,ca,index,h,lblhint
        h=ca[0:index+1]
        
        lblhint.config(text="letter is "+str(h))
        #print(h)
        index+=1
        #return lblhint
    if l>0:
        c=random.choice(que)
        cqno=que.index(c)
        ca=ans[cqno]
        index=0
        lblque=Label(mainwin,text="WOHOOO!!!Let's BLEUNSCRAM ",font=("comic sans ms",19,"bold"),bg="peachpuff",fg="black")
        lblque.place(x=0,y=0)
        lblq=Label(mainwin,text=c,font=("bookman old style",15,"bold"),bg='cornsilk',fg="black")
        lblq.place(x=70,y=70)
        entryans=Entry(mainwin,text="      ",font=("comic sans ms",10,"bold"),bd=3,bg="snow",fg="black",relief=FLAT)
        entryans.place(x=190,y=70)
        e=entryans.get()
        lblhint=Label(mainwin,text="                ",font=("comic sans ms",12,"bold"),bg="brown",fg="snow")
        lblhint.place(x=130,y=110)
        btnnext=Button(mainwin,text="NEXT",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=nextq)
        btnnext.place(x=150,y=150)
        btnhint=Button(mainwin,text="HINT",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=hint)
        btnhint.place(x=250,y=150)
        
        #lblhint.destroy()
        que.remove(c)
        ans.remove(ca)
        l=l-1

    if l==0:
        result()
    
def startispressed():
    global mainwin
    root.destroy()
    mainwin=tkinter.Tk()
    mainwin.title("JUMBLED WORDS")
    ws1=mainwin.winfo_screenwidth()
    hs1=mainwin.winfo_screenheight()
    w1=600
    h1=400
    x1=int(ws/2-w/2)
    y1=int(hs/2-h/2)
    mainwin.configure(background="brown")
    data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
    mainwin.geometry(data)
    mainwin.resizable(0,0)
    game()

def intro():
    
    lbl.destroy()
    lbl1.destroy()
    pl.destroy()
    btn.destroy()
    lbl2=Label(root,text=" Please read your instructions \n  and click on start ",font=("bookman old style",19,"bold"),bg="paleturquoise",fg="black",justify=LEFT)
    lbl2.pack()
    lbl3=Label(root,text=" BE CAREFUL!!You have to enter the correct\n answer and if you don't then score gets\n DEDUCTED ",font=("bookman old style",13,"bold"),bg="BLACK",fg="red",justify=LEFT)
    lbl3.pack()
    btn2=Button(root,text="START",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=startispressed)
    btn2.place(x=150,y=150)

    
lbl=Label(root,text="Welcome to the game of JUMBLED WORDS!!!",font=("bookman old style",13,"bold"),bg="snow",fg="black")
lbl.pack()
lbl1=Label(root,text="Please enter your name",font=("bookman old style",14,"bold"),bg="snow",fg="black")
lbl1.pack()
pl=Entry(root,text="player1 ",font=("comic sans ms",10,"bold"),bd=3,bg="ghostwhite",fg="seagreen",relief=FLAT)
pl.place(x=110,y=100)
pl.insert(0,"  ")
p=pl.get()
btn=Button(root,text="LET'S GO",font=("georgia",11,"bold"),bg="BLACK",fg="azure",relief=FLAT,command=intro)
btn.place(x=150,y=150)


root.mainloop()
