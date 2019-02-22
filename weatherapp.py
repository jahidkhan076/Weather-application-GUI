from tkinter import *
import requests
w=Tk()
w.title('Weather application')
def weather():
    s=E1.get()
    url="http://api.openweathermap.org/data/2.5/weather?q={}&APPID=14fc8e75ac7a90b89f2e93b0914723bf&units=matric",format(s)
    response=requests.get(url)
    x=response.json()
    pprint(x)

F1=Frame(w)
text=StringVar()
L1=Label(F1,text='Enter Name Of City :')
L1.pack(side=LEFT)
E1=Entry(F1,textvariable=text)
E1.pack(side=LEFT)
F1.pack()

F2=Frame(w)
L2=Label(F2,text='TEMPERATURE :')
L2.pack(side=LEFT)
#text=StringVar()
E2=Entry(F2)
E2.pack(side=LEFT)
F2.pack()

F3=Frame(w)
L3=Label(F3,text='HUMIDITY :')
L3.pack(side=LEFT)
#text=StringVar()
E3=Entry(F3)
E3.pack(side=LEFT)
F3.pack()

F4=Frame(w)
L4=Label(F4,text='WIND :')
L4.pack(side=LEFT)
#text=StringVar()
E4=Entry(F4)
E4.pack(side=LEFT)
F4.pack()

F5=Frame(w)
B1=Button(F5,text=' CLEAR ')
B1.pack(side=LEFT)
F5.pack()

F6=Frame(w)
B2=Button(F6,text='OK',command= weather())
B2.pack(side=LEFT)
F6.pack()

w.mainloop()
