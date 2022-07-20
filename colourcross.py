#imports:
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.messagebox import showinfo
import random



root=tkinter.Tk()
root.title("COLOUR-CROSS")
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
w=400
h=200
x=int(ws/2-w/2)
y=int(hs/2-h/2)
root.configure(background="mintcream")
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

global s,e
colours=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
colours1=['Blue','Green','Black','Brown','Red','Yellow','Purple','Orange']

#fc=colours1[1]
s=0
l=len(colours)

    
def result(s):
    def quit_func():
        while(1):
            root.destroy()
            break
    def mainbtn_func():
        root.destroy()
        import tutorialtk
    
    mainwin.destroy()
    root=tkinter.Tk()
    root.title("COLOUR-CROSS")
    root.resizable(0,0)
    ws1=root.winfo_screenwidth()
    hs1=root.winfo_screenheight()
    w1=400
    h1=200
    x1=int(ws1/2-w1/2)
    y1=int(hs1/2-h1/2)
    root.configure(background="darkkhaki")
    data1=str(w1)+"x"+str(h1)+"+"+str(x1)+"+"+str(y1)
    root.geometry(data)
    lblr= Label(root,text="GAME OVER! \n your score is:" +str(s), font=("helvetica",25,"bold"), bg='lightgreen', fg='black')
    lblr.pack()
    exitBtn=Button(root,text='Exit',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=quit_func,relief=FLAT)
    exitBtn.place(x=30, y=150)
    mainBtn=Button(root,text='Main Menu',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=mainbtn_func,relief=FLAT)
    mainBtn.place(x=230, y=150)
    
    
    
def game():
    global current,entryans,lblque,lblq,btnnext,s,l,c,mainwin
    
    
    #lblq.destroy()
    def la2():
        global current,entryans,lblque,lblq,btnnext,s,l,c
        if entryans.get().lower()==current.lower():
            s=s+1
            lblq.destroy()
            entryans.delete(0,END)
            la()
            
        else:
            lblq.destroy()
            entryans.delete(0,END)
            la()
            s=s-1
    def la():
        global current,entryans,lblque,lblq,btnnext,s,l,c
        if l>0:
            c=random.choice(colours)
            current=random.choice(colours1)
            lblque=Label(mainwin,text="REMEMBER...Choose the text colour......",font=("comic sans ms",15,"bold"),bg="peachpuff",fg="black")
            lblque.place(x=0,y=0)
            lblq=Label(mainwin,text=c,font=("bookman old style",15,"bold"),bg='cornsilk',fg=current)
            lblq.place(x=70,y=70)
            entryans=Entry(mainwin,text="      ",font=("comic sans ms",10,"bold"),bd=3,bg="snow",fg="black",relief=FLAT)
            entryans.place(x=190,y=70)
            btnnext=Button(mainwin,text="NEXT",font=("georgia",15,"bold"),bg="cornsilk",fg="black",relief=FLAT,command=la2)
            btnnext.place(x=150,y=150)
            l=l-1
        elif l==0:
             
             result(s)
        
        
        
    if l>0:
        la()
    
        
def startispressed():
    global mainwin
    root.destroy()
    mainwin=tkinter.Tk()
    mainwin.title("COLOUR-CROSS")
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

    lbl2=Label(root,text="Please read your instructions and\n click on start",font=("bookman old style",15,"bold"),bg="azure",fg="black")
    lbl2.pack()
    lbl3=Label(root,text=" BE CAREFUL!! You have to select the name of the  \n colour and not the colour in which it is written ",font=("bookman old style",11,"bold"),bg="indigo",fg="cornsilk",justify=LEFT)
    lbl3.pack()
    btn2=Button(root,text="START",font=("georgia",15,"bold"),bg="black",fg="cornsilk",relief=FLAT,command=startispressed)
    btn2.place(x=150,y=150)

    
lbl=Label(root,text="Welcome to the game of Colour-cross",font=("bookman old style",15,"bold"),bg="snow",fg="black")
lbl.pack()
lbl1=Label(root,text="Please enter your name",font=("bookman old style",15,"bold"),bg="snow",fg="black")
lbl1.pack()
pl=Entry(root,text="player1 ",font=("comic sans ms",10,"bold"),bd=3,bg="mediumaquamarine",fg="ivory",relief=FLAT)
pl.place(x=110,y=100)
pl.insert(0,"  ")

btn=Button(root,text="LET'S GO",font=("georgia",11,"bold"),bg="black",fg="azure",relief=FLAT,command=intro)
btn.place(x=150,y=150)


root.mainloop()
