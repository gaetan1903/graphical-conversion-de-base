#  *__author__*  Gaetan Jonathan
#-*- coding:Utf-8 -*-

from tkinter import *
import baseconverter

class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('Conversion de Base')
        self.root.geometry('1360x760')
        
        

    def corps(self):

        self.image = PhotoImage(file='math.png')
        self.background = Label(self.root, image = self.image ).place(relx =0 , rely =0)

        self.text = Label(self.root, text = 'Base decimal en base quelconque', fg ='red').place(relx = 0.1, rely = 0.01)
        self.variable = IntVar()
        self.text_valeur_entre = Label(self.root, text = " Nombre decimal: ").place(relx=0.01, rely = 0.1)
        self.valeur_entre = Entry(self.root, textvariable = self.variable, width = 25).place(relx=0.11, rely=0.15)

        self.radio_var =  IntVar()
        self.radio1 = Radiobutton(self.root, text = 'Base Binaire', variable = self.radio_var, value = 2).place(relx = 0.01, rely = 0.2)
        self.radio2 = Radiobutton(self.root, text = 'Base Octal', variable = self.radio_var, value = 8).place(relx = 0.11, rely = 0.2)
        self.radio2 = Radiobutton(self.root, text = 'Base Hexadecimal', variable = self.radio_var, value = 16).place(relx = 0.2, rely = 0.2)
        self.bouton_convertir = Button(self.root, text = 'CONVERTIR',bg ='lightblue', command = self.conversion).place(relx = 0.11, rely = 0.3)

        self.liste_options = (3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15)
        self.listebox = OptionMenu(self.root, self.radio_var, *self.liste_options).place(relx = 0.11, rely = 0.24)


#  ********************************************************************'''**********************************************************************
        
        self.stext = Label(self.root, text =' Base quelconque en base decimal', fg = 'red').place(relx = 0.65, rely = 0.01)
        self.svariable = StringVar()
        self.stext_valeur_entre = Label(self.root, text = " Nombre non-decimal: ").place(relx=0.61, rely = 0.1)
        self.svaleur_entre = Entry(self.root, textvariable = self.svariable, width = 25).place(relx=0.73, rely=0.15)

        self.sradio_var =  IntVar()
        self.sradio1 = Radiobutton(self.root, text = 'Base Binaire', variable = self.sradio_var, value = 2).place(relx = 0.63, rely = 0.2)
        self.sradio2 = Radiobutton(self.root, text = 'Base Octal', variable = self.sradio_var, value = 8).place(relx = 0.73, rely = 0.2)
        self.sradio2 = Radiobutton(self.root, text = 'Base Hexadecimal', variable = self.sradio_var, value = 16).place(relx = 0.83, rely = 0.2)
        self.sbouton_convertir = Button(self.root, text = 'CONVERTIR', bg = 'lightblue', command = self.sconversion).place(relx = 0.73, rely = 0.3)

        self.sliste_options = (3, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15)
        self.slistebox = OptionMenu(self.root, self.sradio_var, *self.sliste_options).place(relx = 0.73, rely = 0.24)

#  ***********************************************************************''*******************************************************************
        self.ssvariable = StringVar()
        self.ssvariable1 = IntVar()
        self.ssvariable2 = IntVar()

        self.ssliste_options = (2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16)
        self.sslistebox1 = OptionMenu(self.root, self.ssvariable1, *self.ssliste_options).place(relx = 0.45, rely = 0.58)
        self.sslistebox2 = OptionMenu(self.root, self.ssvariable2, *self.ssliste_options).place(relx = 0.45, rely = 0.64)

        self.sstext = Label(self.root, text =' Base quelconque en base quelconque', fg = 'red').place(relx = 0.38, rely = 0.45)
        self.sstext_valeur_entre = Label(self.root, text = 'Nombre à convertir').place(relx = 0.425, rely = 0.5)
        self.ssvaleur_entre = Entry(self.root, textvariable = self.ssvariable).place(relx=0.41, rely =0.54)
        self.ssbouton_convertir = Button(self.root, text = 'CONVERTIR', bg = 'lightblue', command = self.ssconversion).place(relx = 0.43, rely = 0.7)

    def conversion(self):
        self.answer = baseconverter.base(self.radio_var.get(), self.variable.get())
        self.blank = Label(self.root, text = '                                                                                                                                  ' ).place(relx = 0, rely = 0.5)
        self.valeur_resultant = Label(self.root, text = self.answer, bg = 'green').place(relx = 0, rely = 0.5)

    def sconversion(self):
        self.answer = baseconverter.decimal(self.sradio_var.get(), self.svariable.get())
        self.blank = Label(self.root, text = '                                                                                                                                  ' ).place(relx = 0.59, rely = 0.5)
        self.valeur_resultant = Label(self.root, text = self.answer, bg = 'green').place(relx = 0.59, rely = 0.5)
    
    def ssconversion(self):
        self.answer = baseconverter.base_to_base(self.ssvariable1.get(), self.ssvariable2.get(), self.ssvariable.get())
        self.blank = Label(self.root, text = '                                                                                                                                   ').place(relx = 0.37, rely = 0.75)
        self.valeur_resultant = Label(self.root, text = self.answer, bg = 'green').place(relx = 0.37, rely = 0.75)


    def finale(self):
        self.root.mainloop()


if __name__ =='__main__':
    fen = Interface()
    fen.corps()
    fen.finale()