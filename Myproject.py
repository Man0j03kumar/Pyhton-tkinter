from tkinter import *
from PIL import Image, ImageTk



work = Tk()
work.geometry("1000x500")
 ####    A  FOR APPLE 
def click():
    img = Image.open("Apple.jpg")
    img = img.resize((500,450))


    img = ImageTk.PhotoImage(img)
    l.config(image=img)
    l.image = img
btn = Button(work, text="A for", command=click, bg="black",fg="white",border=10,borderwidth=10)
btn.place(x=0,y=0)
l = Label(work)
l.place(x=600,y=200)
# #### B FOR BOY
def click():
    image = Image.open("Boy.jpg")
    image = image.resize((200,250))
    img = ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image = img
btn = Button(work, text="B for", command=click, bg="black",fg="white",border=10,borderwidth=10)
btn.place(x=100,y=0)
l = Label(work)
l.place(x=600,y=200)



###  C FOR CAT
def click():
    image = Image.open("cat.jpg")
    image=image.resize((200,250))
    img = ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=img
btn = Button(work,text="C for", command = click ,bg="black",fg="white",border=10,borderwidth=10 )
#btn.place()
btn.place(x=200,y=0)

l = Label(work)
l.place(x=600,y=200)
###  D FOR DOG 
def click():
    image= Image.open("dog.jpg")
    image= image.resize((200,250))
    img=ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="D for",command=click,bg="black",fg="white",border=10,borderwidth=10)
btn.place(x=300,y=0)
l =Label(work)
l.place(x=600,y=200)
# ####  E FOR ELEPHANT
def click():
    image= Image.open("elephant.jpg")
    image=image.resize((200,250))
    img=ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=img
btn = Button(work,text="E for ",command=click,bg="black",fg="white",border=2,borderwidth=10)
#btn.place()
btn.place(x=400,y=0)

l = Label(work)
l.place(x=600,y=200)
####  F FOR FISH
def click():
    image=Image.open("fish.jpg")
    image= image.resize((200,250))
    img=ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=img
btn = Button(work,text="F for",command=click,bg="black",fg="white",border=10,borderwidth=10)
btn.place(x=500,y=0)
l= Label(work)
l.place(x=600,y=200)
### G FOR GRAPES
def click(): 
    image=Image.open("grapes.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="G for",command=click,bg="black",fg="white",border=10,borderwidth=10)
btn.place(x=600,y=0)
l=Label(work)
l.place(x=600,y=200)

# ###  H FOR HORSE

def click(): 
    image=Image.open("horse.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="H for",command=click,bg="black",fg="white",border=10,borderwidth=10)

btn.place(x=700,y=0)

l=Label(work)
l.place(x=600,y=200)

# ###  I FOR ICECREAM

def click(): 
    image=Image.open("ice cream.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="I for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=800,y=0)

l=Label(work)
l.place(x=600,y=200)

# ###  J FOR JOKER

def click(): 
    image=Image.open("joker.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="J for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=900,y=0)

l=Label(work)
l.place(x=600,y=200)

# # ###  K FOR KITE

def click(): 
    image=Image.open("kite.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="K for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=1000,y=0)

l=Label(work)
l.place(x=600,y=200)

# ###  L FOR LION

def click(): 
    image=Image.open("lion.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="L for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=0,y=100)

l=Label(work)
l.place(x=600,y=200)

#### M FOR MANGO
def click(): 
    image=Image.open("mango.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="M for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=100,y=100)

l=Label(work)
l.place(x=600,y=200)

# # # ###  N FOR NEST

def click(): 
    image=Image.open("nest.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="N for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=200,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  O FOR ORANGE

def click(): 
    image=Image.open("orange.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="O for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=300,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  P FOR PARROT

def click(): 
    image=Image.open("parrot.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="P for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=400,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  Q FOR QUEEEN

def click(): 
    image=Image.open("queen.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="Q for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=500,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  R FOR RABBIT

def click(): 
    image=Image.open("rabbit.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="R for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=600,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  S FOR SUN

def click(): 
    image=Image.open("sun.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="S for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=700,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  T FOR TIGER

def click(): 
    image=Image.open("tiger.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="T for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=800,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  U FOR UMBERRLA

def click(): 
    image=Image.open("umberrla.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="U for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=900,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  V FOR VAN

def click(): 
    image=Image.open("van.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="H for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=1000,y=100)

l=Label(work)
l.place(x=600,y=200)

# ###  W FOR WATCH

def click(): 
    image=Image.open("watch.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="W for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=0,y=200)

l=Label(work)
l.place(x=600,y=200)

###  X FOR X RAY

def click(): 
    image=Image.open("x ray.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="X for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=100,y=200)

l=Label(work)
l.place(x=600,y=200)

# ###  Y FOR YAK

def click(): 
    image=Image.open("yak.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="Y for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=200,y=200)

l=Label(work)
l.place(x=600,y=200)

# ###  Z FOR ZEBRA

def click(): 
    image=Image.open("zebra.jpg")
    image=image.resize((200,250) )
    img= ImageTk.PhotoImage(image)
    l.config(image=img)
    l.image=(img)
btn = Button(work,text="Z for",command=click,bg="black",fg="white",border=10,borderwidth=10)
#btn.place()
btn.place(x=300,y=200)

l=Label(work)
l.place(x=600,y=200)




work.mainloop()













