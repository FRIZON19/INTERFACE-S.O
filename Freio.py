from tkinter import *
import os

app=Tk()
app.title("Freio")
app.geometry("1200x700")
app.configure(background="#a9a9a9")

pastaApp=os.path.dirname(__file__)

imgLogo=PhotoImage(file=pastaApp+"\\pedais2.png")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=0,y=0)