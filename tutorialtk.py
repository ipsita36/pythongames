#import:
import tkinter
from tkinter import*

from ttkthemes import ThemedTk,THEMES

root=tkinter.Tk()
root.title("GAMES")
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
w=600
h=600
x=int(ws/2-w/2)
y=int(hs/2-h/2)
root.configure(background="lavender")
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

#quit:
def quitfunc():
    while(1):
        root.destroy()
        break
#tictactoe:
def tic():
    root.destroy()
    import tictactoe


#jumbled words:
def jumbled():
    root.destroy()
    import jumbledwords


#colour-cross:
def colourcross():
    root.destroy()
    import colourcross

#rockpaperscissors:
def rps():
    root.destroy()
    import rockpaperscissors
    

    

about="-------Wanna go back to your childhood days?wanna relive the days of playing games?we have the perfect solution for you---------------------"

lbl1=Label(text="NOSTALGIA",font=("HARRINGTON",80,"bold"),bg="lavenderblush",fg="BLACK")
lbl1.place(x=0,y=0)
lbl2=Label(text=about,font=("HARRINGTON",15),bg="palegreen",fg="BLACK",wraplength=635,justify=LEFT)
lbl2.place(x=0,y=130)
btn1=Button(root,text="TIC-TAC-TOE",font=("lucida handwriting",18,"bold"),width=22,height=1,background="mistyrose",foreground="black",relief=FLAT,command=tic)
btn1.place(x=100,y=200)
btn2=Button(root,text="JUMBLED WORDS",font=("lucida handwriting",18,"bold"),width=22,height=1,background="black",foreground="mistyrose",relief=FLAT,command=jumbled)
btn2.place(x=100,y=280)
btn3=Button(root,text="COLOUR-CROSS",font=("lucida handwriting",18,"bold"),width=22,height=1,background="mistyrose",foreground="black",relief=FLAT,command=colourcross)
btn3.place(x=100,y=360)
btn4=Button(root,text="ROCK-PAPER-SCISSORS",font=("lucida handwriting",18,"bold"),width=22,height=1,background="black",foreground="mistyrose",relief=FLAT,command=rps)
btn4.place(x=100,y=440)
btn5=Button(root,text="EXIT",font=("lucida handwriting",18,"bold"),width=22,height=1,background="khaki",foreground="crimson",relief=FLAT,command=quitfunc)
btn5.place(x=100,y=520)



root.mainloop()

