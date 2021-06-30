from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

#def semComando():
    #print("")
    
def calibrar():
  exec(open(pastaApp+"\\Calibrar.py").read())
     
    
#def Acelerador():
    #exec(open(pastaApp+"\\Acelerador.py").read())
    
#def Freio():
   # exec(open(pastaApp+"\\Freio.py").read())
    
#def Embreagem():
   # exec(open(pastaApp+"\\Embreagem.py").read())
    
#def HandBrake():
   # exec(open(pastaApp+"\\Hand Brake.py").read())

#def Seach():
   # exec(open(pastaApp+"\\Seach.py").read())
    
#def Sobre():
   # exec(open(pastaApp+"\\Sobre.py").read())
    
#def Cambio():
    #exec(open(pastaApp+"\\Cambio.py").read())
    
        

app=Tk()
app.title("SimRacing™")
app.geometry("1350x700")
app.configure(background="#a9a9a9")

imgLogo=PhotoImage(file=pastaApp+"\\pedais.png")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=0,y=0)


#txt1=Label(app,text="",background="#a9a9a9",foreground="#fff")
#txt1.place(x=10,y=10,width=100,height=20)

barraDeMenus=Menu(app)
menuContatos=Menu(barraDeMenus,tearoff=0)
menuContatos.add_command(label="Calibragem",command=calibrar)
#menuContatos.add_command(label="Acelerador",command=Acelerador)
#menuContatos.add_command(label="Cambio",command=Cambio)
#menuContatos.add_command(label="Freio",command=Freio)
#menuContatos.add_command(label="Embreagem",command=Embreagem)
#menuContatos.add_command(label="Hand Brake",command=HandBrake)
#menuContatos.add_separator()
#menuContatos.add_command(label="Fechar",command=app.quit)
barraDeMenus.add_cascade(label="Configurar",menu=menuContatos)

menuContatos=Menu(barraDeMenus,tearoff=0)
#menuContatos.add_command(label="Mod.Arduino",command=Seach)
barraDeMenus.add_cascade(label="Pesquisar",menu=menuContatos)

menuContatos=Menu(barraDeMenus,tearoff=0)
#menuContatos.add_command(label="Dev",command=Sobre)
barraDeMenus.add_cascade(label="Sobre",menu=menuContatos)

b = Button(app,text = "Acelerador")
b.pack()


app.config(menu=barraDeMenus)
app.mainloop()