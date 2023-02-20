from tkinter import *
import tkinter.messagebox as mb
import os
from database_create import base
from base_insert import database_insert
from base_select import base_select
from base_delete import base_delete

#Definisanje Tkinter prozora
top_win = Tk()
top_win.geometry("250x250")

def base_create():
    try:
        base()
        mb.showinfo("Kreiranje..", "Baza podataka je kreirana")
    except:
        mb.showinfo("Kreiranje nije uspjelo", "Provjerite da baza podataka vec ne postoji")


def package_install():
    mb.showinfo("Instalacija paketa", "Sledeci paketi ce biti instalirani: 1. PyFiglet")
    try:
        os.system("pip install pyfiglet")
    except:
        mb.showinfo("Greska", "Doslo je do greske prilikom instalacije")


def base_insert():
    try:
        database_insert()
    except:
        mb.showinfo("Greska", "Doslo je do greske prilikom unosta provjerite da li ste ispravno unijeli podatke")


def dbase_select():
    try:
        base_select()
    except:
        mb.showinfo("Greska", "Doslo je do greske prilikom citanja podataka iz baze")


def dbase_delete():
    try:
        base_delete()
    except:
        mb.showinfo("Greska", "Doslo je do greske prilikom pokusaja brisanja iz baze podataka.")

#Dzgme broj 1 za kreiranje baze
button1 = Button(top_win, text="Kreiranje Baza Podataka",
                  activebackground= "white",
                  activeforeground= "red",
                  command = base_create)
button1.place(x = 2, y = 0)
#Dugme broj 2 za instalaciju paketa
button2 = Button(top_win, text="Instalacija potrebnih paketa",
                  activebackground= "white",
                  activeforeground= "red",
                  command= package_install)
button2.place(x = 2, y = 30)
#Dugme broj 3 za unos podataka u bazu
button3 = Button(top_win, text="Unos podataka u bazu",
                  activebackground= "white",
                  activeforeground= "red",
                  command = base_insert)
button3.place(x = 2, y= 60)
#Dugme broj 4 za ispis podataka iz baze
button4 = Button(top_win, text="Citanje iz baze podataka",
                  activebackground= "white",
                  activeforeground= "red",
                  command = dbase_select)
button4.place(x = 2, y = 90)
#Dugme broj 5 za brisanje podataka iz baze
button5 = Button(top_win, text="Brisanje iz baze podataka",
                  activebackground= "white",
                  activeforeground= "red",
                  command = dbase_delete)
button5.place(x = 2, y = 120)

top_win.mainloop()