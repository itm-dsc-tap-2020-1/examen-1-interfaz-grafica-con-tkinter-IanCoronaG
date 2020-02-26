import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mbox

################################  METODOS  ##########################################################################################
ventana=tk.Tk()

################################  PREGUNTAS                      #################################################################

ventana.title("EXAMEN 01 PYTHON GRÁFICO")
ventana.resizable(0, 0)
tabex=ttk.LabelFrame(ventana, text="EXAMEN DE COMPUTACIÓN")
tabex.grid(column=0, row=1, padx=20, pady=20)

ttk.Label(tabex, text="1.- Sistema numerico en que operan las computadoras: ").grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
ttk.Label(tabex, text="2.- Nombre del componente que realiza las operaciones matematicas que hacen funcionar una computadora: ").grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
ttk.Label(tabex, text="3.- Componentes físicos que componen a una computadora: ").grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)
ttk.Label(tabex, text="4.- Conjunto de programas computacionales que ejecuta una computadora: ").grid(column=0, row=6, padx=5, pady=5, sticky=tk.W)
ttk.Label(tabex, text="5.- Es un periférico de una computadora: ").grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)

################################ RESPUESTAS  #################################################################################################

r1= tk.StringVar()
r2= tk.StringVar()
cr1= ttk.Entry(tabex, width=28, textvariable=r1).grid(column = 1, row = 2, padx=5, pady=5, sticky=tk.W)
cr2= ttk.Entry(tabex, width=28, textvariable=r2).grid(column = 1, row = 3, padx=5, pady=5, sticky=tk.W)



###################################### RADIO BUTTONS    ######################################################################################

cradio=ttk.LabelFrame(tabex)
rb=tk.IntVar()

cradio2=ttk.LabelFrame(tabex)
rb2=tk.IntVar()

r1=ttk.Radiobutton(cradio, text="Hardware", variable=rb, value=1)
r2=ttk.Radiobutton(cradio, text="Software", variable=rb, value=2)
r3=ttk.Radiobutton(cradio, text="Sistema", variable=rb, value=3)

r4=ttk.Radiobutton(cradio2, text="Hardware", variable=rb2, value=1)
r5=ttk.Radiobutton(cradio2, text="Software", variable=rb2, value=2)
r6=ttk.Radiobutton(cradio2, text="Sistema", variable=rb2, value=3)


r1.grid(column=0,row=0, sticky=tk.W, padx=10, pady=10)
r2.grid(column=1,row=0, sticky=tk.W, padx=10, pady=10)
r3.grid(column=2,row=0, sticky=tk.W, padx=10, pady=10)

r4.grid(column=0,row=0, sticky=tk.W, padx=10, pady=10)
r5.grid(column=1,row=0, sticky=tk.W, padx=10, pady=10)
r6.grid(column=2,row=0, sticky=tk.W, padx=10, pady=10)

cradio.grid(column=1, row=5, padx=10, pady=10, sticky=tk.W)

cradio2.grid(column=1, row=7, padx=10, pady=10, sticky=tk.W)

#################################### CHECH BUTTONS ########################################################################################
check=ttk.LabelFrame(tabex)
check.grid(column=1, row=9, padx=10, pady=10, sticky=tk.W)

opc1=tk.IntVar()
opc2=tk.IntVar()
opc3=tk.IntVar()
opc4=tk.IntVar()
opc5=tk.IntVar()

c1=ttk.Checkbutton(check, text="Mouse", variable=opc1)
c2=ttk.Checkbutton(check, text="Programa Ofimático", variable=opc2)
c3=ttk.Checkbutton(check, text="Pantalla", variable=opc3)
c4=ttk.Checkbutton(check, text="Sistema Operativo", variable=opc4)
c5=ttk.Checkbutton(check, text="Disco Duro", variable=opc5)

c1.grid(column=0,row=1, sticky=tk.W, padx=10, pady=10)
c2.grid(column=1,row=1, sticky=tk.W, padx=10, pady=10)
c3.grid(column=2,row=1, sticky=tk.W, padx=10, pady=10)
c4.grid(column=0,row=1, sticky=tk.W, padx=10, pady=10)
c5.grid(column=1,row=1, sticky=tk.W, padx=10, pady=10)




##########################################################################################################################
ventana.mainloop()
