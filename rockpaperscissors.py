#imports:
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.messagebox import showinfo
import random



root=tkinter.Tk()
root.title("ROCK-PAPER-SCISSORS")
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
w=550
h=200
x=int(ws/2-w/2)
y=int(hs/2-h/2)
root.configure(background="lightgreen")
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

list=['rock','scissors','paper']

global s,c    
s=0
c=0

def result():
        global s,c
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
        root.title("ROCK-PAPER-SCISSORS")
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
        lblr= Label(root,text="GAME OVER! \n Your score is:" +str(s)+"\nComputer's score is:"+str(c), font=("helvetica",25,"bold"), bg='BLACK', fg='LIGHTGREEN')
        
        lblr.pack()
        exitBtn=Button(root,text='Exit',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=quit_func,relief=FLAT)
        exitBtn.place(x=70, y=150)
        mainBtn=Button(root,text='Main Menu',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=mainbtn_func,relief=FLAT)
        mainBtn.place(x=300, y=150)

def rock():
        global lbltext,s,c
        comp=random.choice(list)
        btnagain.config(state='normal')
        btnresult.config(state='normal')
        #print(comp)
        if comp=='rock':
                lbltext=Label(mainwin,text="Computer chose rock\nYou chose rock\nIt's a tie",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
        elif comp=='scissors':
                lbltext=Label(mainwin,text="Computer chose scissors\nYou chose rock\nYou win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                s+=1
        elif comp=='paper':
                lbltext=Label(mainwin,text="Computer chose paper\nYou chose rock\nComputer win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                c+=1
def scissors():
        global lbltext,s,c
        comp=random.choice(list)
        btnagain.config(state='normal')
        btnresult.config(state='normal')
        #print(comp)
        if comp=='scissors':
                lbltext=Label(mainwin,text="Computer chose scissors\nYou chose scissors\nIt's a tie",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
        elif comp=='rock':
                lbltext=Label(mainwin,text="Computer chose rock\nYou chose scissors\nComputer win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                c+=1
        elif comp=='paper':
                lbltext=Label(mainwin,text="Computer chose paper\nYou chose scissors\nYou win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                s+=1
                

def paper():
        global lbltext,s,c
        comp=random.choice(list)
        btnagain.config(state='normal')
        btnresult.config(state='normal')
        #print(comp)
        if comp=='rock':
                lbltext=Label(mainwin,text="Computer chose rock\nYou chose paper\nYou win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                s+=1
        elif comp=='scissors':
                lbltext=Label(mainwin,text="Computer chose scissors\nYou chose paper\nComputer win",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                c+=1
        elif comp=='paper':
                lbltext=Label(mainwin,text="Computer chose paper\nYou chose paper\nIt's a tie",font=("bookman old style",10,"bold"),bg="snow",fg="black",width=30,height=5,justify=LEFT)
                lbltext.place(x=220,y=50)
                


def again():
        lbltext.destroy()
        lblchoice.destroy()
        btnr.destroy()
        btnp.destroy()
        btns.destroy()
        btnagain.destroy()
        game()
        


        
    
def game():
        global lblchoice,btnr,btnp,btns,btnagain,btnresult
        lblchoice=Label(mainwin,text="Choose a symbol",font=("bookman old style",20,"bold"),bg="midnightblue",fg="snow")
        lblchoice.pack()
        btnr=Button(mainwin,text="ROCK",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,width=8,command=rock)
        btnr.place(x=10,y=50)
        btnp=Button(mainwin,text="PAPER",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,width=8,command=paper)
        btnp.place(x=10,y=100)
        btns=Button(mainwin,text="SCISSORS",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,width=8,command=scissors)
        btns.place(x=10,y=150)
        btnagain=Button(mainwin,text="AGAIN",font=("georgia",12,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=again,state='disabled')
        btnagain.place(x=400,y=150)
        btnresult=Button(mainwin,text="RESULT",font=("georgia",12,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=result,state='disabled')
        btnresult.place(x=200,y=150)
        
    
def startispressed():
    global mainwin
    root.destroy()
    mainwin=tkinter.Tk()
    mainwin.title("RPS")
    ws1=mainwin.winfo_screenwidth()
    hs1=mainwin.winfo_screenheight()
    w1=500
    h1=500
    x1=int(ws/2-w/2)
    y1=int(hs/2-h/2)
    mainwin.configure(background="midnightblue")
    data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
    mainwin.geometry(data)
    mainwin.resizable(0,0)
    game()

def intro():
    
    lbl.destroy()
    lbl1.destroy()
    pl.destroy()
    btn.destroy()
    lbl2=Label(root,text="Read your instructions and click on start",font=("bookman old style",19,"bold"),bg="lightgreen",fg="black",justify=LEFT)
    lbl2.pack()
    lbl3=Label(root,text="You have to choose a specific symbol and the computer \nwill select a random symbol and the game proceeds ",font=("bookman old style",14,"bold"),bg="BLACK",fg="red",justify=LEFT)
    lbl3.pack()
    btn2=Button(root,text="START",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=startispressed)
    btn2.place(x=230,y=150)

    
lbl=Label(root,text="WELCOME To the game of ROCK-PAPER-SCISSCORS!!!",font=("bookman old style",14,"bold"),bg="snow",fg="black")
lbl.pack()
lbl1=Label(root,text="Please enter your name",font=("bookman old style",14,"bold"),bg="snow",fg="black")
lbl1.pack()
pl=Entry(root,text="player1 ",font=("comic sans ms",10,"bold"),bd=3,bg="ghostwhite",fg="midnightblue",relief=FLAT)
pl.place(x=180,y=100)
pl.insert(0,"  ")
p=pl.get()
btn=Button(root,text="LET'S GO",font=("georgia",11,"bold"),bg="BLACK",fg="azure",relief=FLAT,command=intro)
btn.place(x=380,y=150)


root.mainloop()
