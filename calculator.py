import tkinter
from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("400x600")
root.resizable(0,0)
root.configure(bg="Blue")
exp=""
def show(value):
    global exp
    exp+=value
    result.config(text=exp)
def clear():
    global exp
    exp=""
    result.config(text=exp)
def calculate():
    global exp
    res=""
    if exp!="":
        try:
            res=eval(exp)
        except:
            res="ouch"
            exp=""
    result.config(text=res)
#result showing row    
result=Label(root,width=25,height=2,text="",font=("sanserif",30))
result.pack()
#row1
Button(root,text="C",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:clear()).place(x=10,y=100)
Button(root,text="*",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("*")).place(x=100,y=100)
Button(root,text="-",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("-")).place(x=200,y=100)
Button(root,text="+",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("+")).place(x=300,y=100)
#row2
Button(root,text="7",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("8")).place(x=100,y=200)
Button(root,text="9",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("9")).place(x=200,y=200)
Button(root,text="/",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("/")).place(x=300,y=200)
#row3
Button(root,text="4",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("5")).place(x=100,y=300)
Button(root,text="6",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("6")).place(x=200,y=300)
Button(root,text="%",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("%")).place(x=300,y=300)
#row4
Button(root,text="1",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("2")).place(x=100,y=400)
Button(root,text="3",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="red",bg="white",command=lambda:show("3")).place(x=200,y=400)
#row5
Button(root,text="0",width=6,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show("0")).place(x=10,y=500)
Button(root,text=".",width=3,height=1,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:show(".")).place(x=200,y=500)


Button(root,text="=",width=3,height=3,font=("sanserif",30,"bold"),bd=1,fg="white",bg="red",command=lambda:calculate()).place(x=300,y=400)

root.mainloop()
