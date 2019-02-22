from tkinter import *
w=Tk()
w.title('tik tak toe')
l=[]
turn=True
pl1=[]
pl2=[]
counter=0
selected=IntVar()
def PL1(t):
    global turn
    global pl1
    global counter
    
    r2.select()
    pl1.append(3*t[0]+t[1]+1)
    Button(w,width=25,height=10,bd=3,state='disable',bg='red').grid(row=t[0],column=t[1])
    turn=False
    counter=counter+1

def PL2(t):
    global turn
    global pl2
    global counter
    #global r1
    r1.select()
    pl2.append(3*t[0]+t[1]+1)
    Button(w,width=25,height=10,bd=3,state='disable',bg='green').grid(row=t[0],column=t[1])
    turn=True
    counter=counter+1
    
def button():
    for i in range(3):
        for j in range(3):
            l.append(Button(w,width=25,height=10,bd=3,state='disable',command=lambda x=(i,j): PL1(x) if turn==True else PL2(x)))
            l[-1].grid(row=i,column=j,padx=5,pady=5)
def f():

    for i in l:
        i['state']='active'
    
button()    
stt=Button(w,text='START',width=25,height=2,command=f).grid(row=3,column=1)
r1=Radiobutton(w,text='PLAYER1TURN',variable=selected,state='disable',value=1,width=25,height=2)
r1.grid(row=3,column=0)
r2=Radiobutton(w,text='PLAYER2TURN',variable=selected,state='disable',value=2,width=25,height=2)
r2.grid(row=3,column=2)

w.mainloop()
