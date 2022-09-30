import mysql.connector
import random
import string
import tkinter as tk
from tkinter import filedialog



def loadBrRacuna(jmbg):
    print("LOAD BROJ RACUNA PRIMA: ",jmbg)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select br_racuna from racun where jmbg="+str(jmbg)
    csr.execute(sql)
    rez = csr.fetchall()
    print("REZ U BRRACUNA   ",rez)
    return rez
def loadOrocava(jmbg):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from orocava where jmbg="+str(jmbg)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez
def loadStedni(br_racuna):
    print("loadStedni prima ovo: ",br_racuna)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from stedni_racun where br_racuna="+str(br_racuna[0])
    csr.execute(sql)
    rez = csr.fetchall()

    return rez
def loadNovac(id_trans):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from novac where id_trans="+str(id_trans)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def loadClients():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from klijent"
    csr.execute(sql)
    rez = csr.fetchall()
    #print(rez)
    return rez

def jmbgSearch(jmbg):
    print("OVO PRIMA JMBGSEARCH: ",jmbg)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from klijent where jmbg = '" + str(jmbg[0]) + "'"
    csr.execute(sql)
    rez = csr.fetchall()
    return rez



def loadExamine(jmbg):
    #print(jmbg)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
    csr = con.cursor()
    sql = "select * from klijent where jmbg =" + str(jmbg)
    csr.execute(sql)
    rez = csr.fetchall()
    #print(rez)
    return rez

