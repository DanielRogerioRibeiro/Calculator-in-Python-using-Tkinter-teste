#Importando Tkinter

from tkinter import *
from tkinter import ttk

#Table of the Colors using Color Picker

cor1 = '#3b3b3b' #black
cor2 = '#feffff' #white
cor3 = '#38576b' #Azul carregado
cor4 = '#ECEFF1' #Cinzento
cor5 = '#FFAB40' #Orange


#Configuração da Calculador
janela = Tk()
janela.title ("Calculator")
janela.geometry ("235x318")
janela.config (bg=cor1)

#Display
frame_display = Frame(janela, width=235, height=50, bg=cor3)
frame_display.grid(row=0, column=0)

#Keyboard
frame_keyboard = Frame(janela, width=235, height=268)
frame_keyboard.grid(row=1, column=0)


#Buttons
b_clear = Button (frame_keyboard, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_perc = Button (frame_keyboard, text="%", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_perc.place(x=118, y=0)

b_div = Button (frame_keyboard, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=177, y=0)




#Mantém a janela aberta
janela.mainloop()
