from tkinter import *
import os

app=Tk()
app.title("Acelerador")
app.geometry("1200x700")
app.configure(background="#a9a9a9")

pastaApp=os.path.dirname(__file__)

imgLogo=PhotoImage(file=pastaApp+"\\Pedais2.png")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=0,y=0)

barraDeMenus=Menu(app)
menuContatos=Menu(barraDeMenus,tearoff=0)
menuContatos.add_command(label="Calibragem",command=calibrar)
menuContatos.add_command(label="Acelerador",command=Acelerador)
menuContatos.add_command(label="Cambio",command=Cambio)
menuContatos.add_command(label="Freio",command=Freio)
menuContatos.add_command(label="Embreagem",command=Embreagem)
menuContatos.add_command(label="Hand Brake",command=HandBrake)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar",command=app.quit)
barraDeMenus.add_cascade(label="Configurar",menu=menuContatos)

menuContatos=Menu(barraDeMenus,tearoff=0)
#menuContatos.add_command(label="Mod.Arduino",command=Seach)
barraDeMenus.add_cascade(label="Pesquisar",menu=menuContatos)

menuContatos=Menu(barraDeMenus,tearoff=0)
#menuContatos.add_command(label="Dev",command=Sobre)
barraDeMenus.add_cascade(label="Sobre",menu=menuContatos)

app.config(menu=barraDeMenus)
app.mainloop()