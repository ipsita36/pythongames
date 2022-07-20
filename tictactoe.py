import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.messagebox import showinfo

root=tkinter.Tk()
root.title("TIC-TAC-TOE")
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
w=400
h=200
x=int(ws/2-w/2)
y=int(hs/2-h/2)
root.configure(background="MAROON")
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)


clicked=True
c=0

def game():
    def result(sx,so):
            def quit_func():
                while(1):
                    root.destroy()
                    break
            def mainbtn_func():
                quit_func()
                import tutorialtk
                
            root=tkinter.Tk()
            root.title("SCORE")
            root.resizable(0,0)
            ws1=root.winfo_screenwidth()
            hs1=root.winfo_screenheight()
            w1=400
            h1=200
            x1=int(ws1/2-w1/2)
            y1=int(hs1/2-h1/2)
            root.configure(background="black")
            data1=str(w1)+"x"+str(h1)+"+"+str(x1)+"+"+str(y1)
            root.geometry(data1)
            mainwin.destroy()

            lblr= Label(root,text="GAME OVER! \n X's score:" +str(sx)+"\nO's score:"+str(so), font=("helvetica",25,"bold"), fg='cornsilk', bg='black')
            lblr.pack()
            exitBtn=Button(root,text='Exit',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=quit_func,relief=FLAT)
            exitBtn.place(x=30, y=150)
            mainBtn=Button(root,text='Main Menu',font=("helvetica",15,"bold"), width=10, bg='red', fg='azure', command=mainbtn_func,relief=FLAT)
            mainBtn.place(x=230, y=150)
        
    def win(b):
        sx=0
        so=0
        
        
        if btna["text"]==btnb["text"]==btnc["text"]=="X":
            btna.config(bg="thistle",fg="crimson")
            btnb.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
        
            sx+=1
            result(sx,so)
        elif btnd["text"]==btne["text"]==btnf["text"]=="X":
            btnd.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btnf.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            sx+=1
            result(sx,so)
        elif btng["text"]==btnh["text"]==btni["text"]=="X":
            btng.config(bg="thistle",fg="crimson")
            btnh.config(bg="thistle",fg="crimson")
            btni.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            result(sx,so)

        elif btna["text"]==btnd["text"]==btng["text"]=="X":
            btna.config(bg="thistle",fg="crimson")
            btnd.config(bg="thistle",fg="crimson")
            btng.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            sx+=1
            result(sx,so)
        elif btnb["text"]==btne["text"]==btnh["text"]=="X":
            btne.config(bg="thistle",fg="crimson")
            btnb.config(bg="thistle",fg="crimson")
            btnh.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won ")
            
            sx+=1
            result(sx,so)
        elif btnc["text"]==btnf["text"]==btni["text"]=="X":
            btni.config(bg="thistle",fg="crimson")
            btnf.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            sx+=1
            result(sx,so)

        elif btna["text"]==btne["text"]==btni["text"]=="X":
            btni.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btna.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            sx+=1
            result(sx,so)
        elif btnc["text"]==btne["text"]==btng["text"]=="X":
            btng.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nX won")
            
            sx+=1
            result(sx,so)

        elif btna["text"]==btnb["text"]==btnc["text"]=="O":
            btna.config(bg="thistle",fg="crimson")
            btnb.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)
        elif btnd["text"]==btne["text"]==btnf["text"]=="O":
            btnd.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btnf.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)
        elif btng["text"]==btnh["text"]==btni["text"]=="O":
            btng.config(bg="thistle",fg="crimson")
            btnh.config(bg="thistle",fg="crimson")
            btni.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)

        elif btna["text"]==btnd["text"]==btng["text"]=="O":
            btna.config(bg="thistle",fg="crimson")
            btnd.config(bg="thistle",fg="crimson")
            btng.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)
        elif btnb["text"]==btne["text"]==btnh["text"]=="O":
            btne.config(bg="thistle",fg="crimson")
            btnb.config(bg="thistle",fg="crimson")
            btnh.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
           
            so+=1
            result(sx,so)
        elif btnc["text"]==btnf["text"]==btni["text"]=="O":
            btni.config(bg="thistle",fg="crimson")
            btnf.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)

        elif btna["text"]==btne["text"]==btni["text"]=="O":
            btni.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btna.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)
        elif btnc["text"]==btne["text"]==btng["text"]=="O":
            btng.config(bg="thistle",fg="crimson")
            btne.config(bg="thistle",fg="crimson")
            btnc.config(bg="thistle",fg="crimson")
            messagebox.showinfo("WON","YAAYYY!!!!\nO won")
            
            so+=1
            result(sx,so)

        elif c==9:
            
            btna.config(bg="lightcoral",fg="mintcream")
            btnb.config(bg="lightcoral",fg="mintcream")
            btnc.config(bg="lightcoral",fg="mintcream")
            btnd.config(bg="lightcoral",fg="mintcream")
            btne.config(bg="lightcoral",fg="mintcream")
            btnf.config(bg="lightcoral",fg="mintcream")
            btng.config(bg="lightcoral",fg="mintcream")
            btnh.config(bg="lightcoral",fg="mintcream")
            btni.config(bg="lightcoral",fg="mintcream")
            messagebox.showinfo("DRAW","OOOHHH!!!!!\nIts a DRAW")
            result(sx,so)

        

        
            
        
    
    def b_clicked(b):
        global clicked,c
        global lbla,lblb
        if b["text"]=="  " and clicked==True:
            b["text"]="X"
            clicked=False
            c+=1
            lbla=Label(text="It is O's turn",font=("HELVETICA",15,"bold"),bg="lightyellow",fg="darkslateblue")
            lbla.grid(row=3,column=1)
            win(b)
        elif b["text"]=="  " and clicked==False:
            b["text"]="O"
            clicked=True
            c+=1
            lblb=Label(text="It is X's turn",font=("HELVETICA",15,"bold"),bg="lightyellow",fg="darkslateblue")
            lblb.grid(row=3,column=1)
            win(b)
        else:
            messagebox.showerror("error","OOPSSS!!!This box is already filled\nPlease select another box..")
        

    btna=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btna))
    btnb=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btnb))
    btnc=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btnc))
    
    btnd=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btnd))
    btne=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btne))
    btnf=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btnf))

    btng=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btng))
    btnh=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btnh))
    btni=Button(text="  ",font=("HELVETICA",25,"bold"),height=3,width=8,bg="peachpuff",fg="darkred",relief=SUNKEN,command=lambda: b_clicked(btni))
    

    btna.grid(row=0,column=0)
    btnb.grid(row=0,column=1)
    btnc.grid(row=0,column=2)
    
    btnd.grid(row=1,column=0)
    btne.grid(row=1,column=1)
    btnf.grid(row=1,column=2)

    btng.grid(row=2,column=0)
    btnh.grid(row=2,column=1)
    btni.grid(row=2,column=2)
        
def startispressed():
    global mainwin
    root.destroy()
    mainwin=tkinter.Tk()
    mainwin.title("TIC-TAC-TOE")
    mainwin.resizable(0,0)
    game()

def intro():
    
    lbl.destroy()
    lbl1.destroy()
    pl1.destroy()
    pl2.destroy()
    lbl2=Label(root,text="Please read your instructions and\n click on start",font=("bookman old style",15,"bold"),bg="peachpuff",fg="black")
    lbl2.pack()
    lbl3=Label(root,text="You pick a button to place your symbol\n You have to place your symbol in an empty space",font=("bookman old style",11,"bold"),bg="darkred",fg="goldenrod2",justify=LEFT)
    lbl3.pack()
    btn2=Button(root,text="START",font=("georgia",15,"bold"),bg="aliceblue",fg="midnightblue",relief=FLAT,command=startispressed)
    btn2.place(x=150,y=150)
    
     
     
     
lbl=Label(root,text="Welcome to the game of Tic-Tac-Toe",font=("bookman old style",15,"bold"),bg="peachpuff",fg="black")
lbl.pack()
lbl1=Label(root,text="Please enter your names",font=("bookman old style",15,"bold"),bg="peachpuff",fg="black")
lbl1.pack()
pl1=Entry(root,text="player1 ",font=("comic sans ms",10,"bold"),bd=3,bg="ivory",fg="black",relief=FLAT)
pl1.place(x=10,y=100)
pl1.insert(0,"  ")
pl2=Entry(root,text="player2 ",font=("comic sans ms",10,"bold"),bd=3,bg="ivory",fg="black",relief=FLAT)
pl2.place(x=220,y=100)
pl2.insert(0,"  ")
btn=Button(root,text="LET'S GO",font=("georgia",11,"bold"),bg="aliceblue",fg="midnightblue",relief=FLAT,command=intro)
btn.place(x=150,y=150)

     
root.mainloop()
