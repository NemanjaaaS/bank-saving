import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont

from tkinter import *
import mysql.connector
import hashlib
import random
import string
from funkcije import *


class win_controler:
    def __init__(self, root):
        self.root = root
        self.win = LogIn_Window(root, self)

    def goToLogWin(self):
        self.win.destroy_all()
        self.win = LogIn_Window(self.root, self)

    def goToAdminWin(self,jmbg):
        self.win.destroy_all()
        self.win = Admin_Window(self.root, self, jmbg)

    def goToKlijentWin(self, jmbg):
        self.win.destroy_all()
        self.win = Klijent_Window(self.root, self, jmbg)

    def goToShowClients(self,jmbg):
        self.win.destroy_all()
        self.win = show_clients_Window(self.root, self,jmbg)

    def goToRegWin(self,jmbg):
        self.win.destroy_all()
        self.win = Register_Window(self.root, self,jmbg)

        


class Window:
    def __init__(self, root):
        self.elements = []
        self.root = root
        
        root.protocol("WM_DELETE_WINDOW", self.closeApp)

    def destroy_all(self):
        for el in self.elements:
            el.destroy()

    def closeApp(self):
        if messagebox.askokcancel("Quit?", "Stvarno zelite da iskljucite?"):
            root.destroy()
            return True
        return False


class LogIn_Window(Window):

    def __init__(self, root, controler):
        self.controler = controler
        
        Window.__init__(self, root)
        # setting title
        self.root.config(menu=0)
        root.title("Banka")
        # setting window size
        width = 643
        height = 446
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.labelBanka = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20)
        

        self.labelBanka = tk.Label(root)
        self.labelBanka["font"] = ft
        self.labelBanka["fg"] = "#333333"
        self.labelBanka["justify"] = "left"
        self.labelBanka["text"] = 'BANKA'

        self.labelBanka.place(x=150, y=10, width=350, height=60)
        self.elements.append(self.labelBanka)

        # btn1 = Button(root, text="Encrypted file", bg="#808080", command=addPath1)

        self.entry_username = tk.Entry(root, fg="#333333", justify="center")
        self.entry_username.place(x=250, y=120, width=147, height=30)

        self.entry_password = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password.place(x=250, y=200, width=147, height=30)

        self.lbl_username = tk.Label(root, fg="#333333", justify="center", text="Korisnicko ime")
        self.lbl_username.place(x=250, y=80, width=113, height=37)

        self.lbl_password = tk.Label(root, fg="#333333", justify="center", text="Lozinka")
        self.lbl_password.place(x=230, y=170, width=108, height=30)

        self.btn_login = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Prijavi se!")
        self.btn_login.place(x=260, y=290, width=128, height=30)
        self.btn_login["command"] = self.login


        self.elements.append(self.entry_username)
        self.elements.append(self.entry_password)
        self.elements.append(self.lbl_username)
        self.elements.append(self.lbl_password)
        self.elements.append(self.btn_login)


    def login(self):
        entry_pwd = self.entry_password.get()
        con = mysql.connector.connect(host='localhost', user='root', port='3306', 
                                     password='', database='banka_db')
        csr = con.cursor()
        sql = "SELECT * FROM `klijent` WHERE username='" + self.entry_username.get() +"'and password='"+self.entry_password.get()+"'"
        csr.execute(sql)
        rez = csr.fetchall()
        for row in rez:
            if(row[4]==self.entry_username.get() and row[5]==self.entry_password.get()):
                if(row[6]==1):
                    self.controler.goToAdminWin(rez[0][0])
                elif(row[6]==0):
                    self.controler.goToKlijentWin(rez[0][0])
                    print(rez[0][0])

            else:

                messagebox.showwarning(title="Upozorenje!", message="Pogresno korisnicko ime ili lozinka!")
                
                return






class Register_Window(Window):
    def __init__(self, root, controler,jmbg):
        Window.__init__(self, root)
        self.jmbg = jmbg
        self.controler = controler
        self.root.config(menu=0)
        # setting title
        root.title("Banka")
        # setting window size
        width = 643
        height = 445
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.entry_name = tk.Entry(root, fg="#333333", justify="center")
        self.entry_name.place(x=180, y=60, width=122, height=30)
        self.elements.append(self.entry_name)

        self.entry_surname = tk.Entry(root, fg="#333333", justify="center")
        self.entry_surname.place(x=310, y=60, width=122, height=30)
        self.elements.append(self.entry_surname)

        self.entry_username = tk.Entry(root, fg="#333333", justify="center")
        self.entry_username.place(x=180, y=120, width=250, height=30)
        self.elements.append(self.entry_username)

        self.entry_adresa = tk.Entry(root, fg="#333333", justify="center")
        self.entry_adresa.place(x=180, y=180, width=250, height=30)
        self.elements.append(self.entry_adresa)

        self.entry_password = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password.place(x=180, y=300, width=122, height=30)
        self.elements.append(self.entry_password)

        self.entry_password2 = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password2.place(x=310, y=300, width=122, height=30)
        self.elements.append(self.entry_password2)

        self.entry_jmbg = tk.Entry(root, fg="#333333", justify="center")
        self.entry_jmbg.place(x=180, y=240, width=122, height=30)
        self.elements.append(self.entry_jmbg)

        self.entry_br_racuna = tk.Entry(root, fg="#333333", justify="center")
        self.entry_br_racuna.place(x=310, y=240, width=122, height=30)
        self.elements.append(self.entry_br_racuna)

        self.btn_register = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Registruj se")
        self.btn_register.place(x=230, y=360, width=151, height=30)
        self.btn_register["command"] = self.register
        self.elements.append(self.btn_register)


        self.lbl_name = tk.Label(root, fg="#333333", justify="center", text="Ime")
        self.lbl_name.place(x=160, y=30, width=82, height=30)
        self.elements.append(self.lbl_name)

        self.lbl_surname = tk.Label(root, fg="#333333", justify="center", text="Prezime")
        self.lbl_surname.place(x=300, y=30, width=70, height=25)
        self.elements.append(self.lbl_surname)

        self.lbl_username = tk.Label(root, fg="#333333", justify="center", text="Korisnicko ime")
        self.lbl_username.place(x=170, y=90, width=123, height=20)
        self.elements.append(self.lbl_username)

        self.lbl_adresa = tk.Label(root, fg="#333333", justify="center", text="Adresa")
        self.lbl_adresa.place(x=170, y=160, width=123, height=20)
        self.elements.append(self.lbl_adresa)

        self.lbl_password1 = tk.Label(root, fg="#333333", justify="center", text="Lozinka")
        self.lbl_password1.place(x=160, y=280, width=95, height=20)
        self.elements.append(self.lbl_password1)

        self.lbl_password2 = tk.Label(root, fg="#333333", justify="center", text="Ponovo unesi lozinku")
        self.lbl_password2.place(x=300, y=280, width=139, height=20)
        self.elements.append(self.lbl_password2)

        self.lbl_jmbg = tk.Label(root, fg="#333333", justify="center", text="JMBG")
        self.lbl_jmbg.place(x=160, y=210, width=95, height=20)
        self.elements.append(self.lbl_jmbg)

        self.lbl_br_racuna = tk.Label(root, fg="#333333", justify="center", text="Broj racuna")
        self.lbl_br_racuna .place(x=300, y=210, width=139, height=20)
        self.elements.append(self.lbl_br_racuna )

    def register(self):
        # messagebox.showwarning(title="Warning!", message="Add encrypted file first!")
        if self.entry_password.get() != self.entry_password2.get():
            messagebox.showerror(title="Greska!", message="Unete lozinke se ne podudaraju!")
            return
        if len(self.entry_password.get()) < 6:
            messagebox.showerror(title="Greska!", message="Lozinka mora imati bar 6 karaktera!")
            return
        # potencijalno promeniti u regularan izraz
        for letter in self.entry_name.get():
            if letter.upper() not in "QWERTYUIOPASDFGHJKLZXCVBNM":
                messagebox.showerror(title="Greska!", message="Ime i prezime moraju biti slova!")
        for letter in self.entry_surname.get():
            if letter.upper() not in "QWERTYUIOPASDFGHJKLZXCVBNM":
                messagebox.showerror(title="Greska!", message="Ime i prezime moraju biti slova!")

        # provera da li username postoji u bazi
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "select count(username) from klijent where username='" + self.entry_username.get() + "'"
        csr.execute(sql)
        rez = csr.fetchone()
        if rez[0] != 0:
            messagebox.showwarning(title="Upozorenje!", message="Korisnik sa tim korisnickim imenom vec postoji!")
            con.close()
            return

        
        pwd = self.entry_password.get()
        
        admin = 0
        # dodaj vrednosti u tabelu "klijent"
        sql = "insert into klijent values ('"+self.entry_jmbg.get()+"', '" + self.entry_name.get() + "', '" + self.entry_surname.get() + "', '"+self.entry_adresa.get()+"','"\
              + self.entry_username.get().lower() + "','"+str(pwd)+"','"+str(admin)+"')"
        print(sql)
        csr.execute(sql)
        con.close()

        svota_novca = 0
        kamatna_stopa = 0

        #Dodaj vrednosti u tabelu "stedni racun"
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "insert into stedni_racun values ('"+self.entry_br_racuna.get()+"', '"+str(svota_novca)+"', '"+str(kamatna_stopa)+"', '"+self.entry_name.get()+"','"\
              + self.entry_surname.get() + "')"
        print(sql)
        csr.execute(sql)
        con.close()
        #dodaj vrednosti u tabelu "stedna knjizica"
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "insert into `stedna knjizica` values ('0', '"+self.entry_name.get()+"', '"+ self.entry_surname.get() +"', '"+self.entry_jmbg.get()+"')"
        print(sql)
        csr.execute(sql)
        con.close()

        #dodaj vrednosti u tabelu "racun"
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "insert into racun values ('"+self.entry_br_racuna.get()+"', '"+self.entry_jmbg.get()+"')"
        print(sql)
        csr.execute(sql)
        con.close()

        #dodaj vrednosti u tabelu "orocava"
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "insert into orocava values (0, '"+self.entry_jmbg.get()+"',0)"
        print(sql)
        csr.execute(sql)
        con.close()
        
        messagebox.showinfo(title="Uspesno!", message="Registracija uspesno izvrsena!")
        self.goBack()

    def goBack(self):
        self.controler.goToAdminWin(self.jmbg)


class Admin_Window(Window):
    def __init__(self, root, controler,jmbg):
        self.controler = controler
        self.jmbg = jmbg
        Window.__init__(self, root)
        # setting title
        root.title("Banka - Admin")
        # setting window size
        width = 645
        height = 445

        con = mysql.connector.connect(host='localhost', user='root', port='3306', 
                                     password='', database='banka_db')
        csr = con.cursor()
        sql = "SELECT * FROM `klijent` WHERE jmbg= "+str(self.jmbg)+""
        csr.execute(sql)
        rez = csr.fetchall()
        

        self.labelAgencije = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20)
        

        self.labelAdmin = tk.Label(root)
        self.labelAdmin["font"] = ft
        self.labelAdmin["fg"] = "#333333"
        self.labelAdmin["justify"] = "left"
        self.labelAdmin["text"] = 'Admin\n '+rez[0][1]+' '+rez[0][2]
        
        self.labelAdmin.place(x=-10, y=20, width=350, height=60)
        self.elements.append(self.labelAdmin)
        
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.btn_switch_page = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Dodaj klijenta")
        self.btn_switch_page.place(x=280, y=120, width=100, height=40)
        self.btn_switch_page["command"] = self.switchToReg
        self.elements.append(self.btn_switch_page)


        self.show_clientBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Prikazi klijente")
        self.show_clientBtn.place(x=280, y=200, width=100, height=40)
        self.show_clientBtn["command"] = self.showClients
        self.elements.append(self.show_clientBtn)


        self.logOutBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Odjavi se")
        self.logOutBtn.place(x=280, y=280, width=100, height=40)
        self.logOutBtn["command"] = self.logOut
        self.elements.append(self.logOutBtn)



    def logOut(self):
        self.controler.goToLogWin()

    def showClients(self):
        self.controler.goToShowClients(self.jmbg)

    def switchToReg(self):
        self.controler.goToRegWin(self.jmbg)


class Klijent_Window(Window):

    def __init__(self, root, controler, jmbg):
        self.controler=controler
        self.jmbg = jmbg
        super().__init__(root)
        root.title("Banka - Klijent")

                # setting window size
        width = 845
        height = 445

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        def logOut():
            self.controler.goToLogWin()

        def search():
            self.controler.goToSearchWin()
#OVDE SAM U REZ SMESTIO SVE PODATKE KORISNIKA KOJI SE ULOGOVAO
# ISPRAVI TO I ZA ADMINA I ISPISI SVE PODATKE KORISNIKA DA PISU KAD SE ULOGUJE
        con = mysql.connector.connect(host='localhost', user='root', port='3306', 
                                     password='', database='banka_db')
        csr = con.cursor()
        sql = "SELECT * FROM `klijent` WHERE jmbg= "+str(self.jmbg)+""
        csr.execute(sql)
        rez = csr.fetchall()
        

        self.labelAgencije = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        

        self.labelKlijenti = tk.Label(root)
        self.labelKlijenti["font"] = ft
        self.labelKlijenti["fg"] = "#333333"
        self.labelKlijenti["justify"] = "left"
        self.labelKlijenti["text"] = 'Dobrodosli\n '+rez[0][1]+' '+rez[0][2]
        self.labelKlijenti.place(x=0, y=20, width=350, height=60)
        self.elements.append(self.labelKlijenti)

        cols = ('Broj racuna', 'Orocen novac', 'Period', 'Kamatna stopa','Novac posle perioda')
        
        self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=10)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox.configure(xscrollcommand=verscrlbar.set)

        self.listBox.column("Broj racuna", width=100, anchor='center')
        self.listBox.column("Orocen novac", width=100, anchor='center')
        self.listBox.column("Period", width=50, anchor='center')
        self.listBox.column("Kamatna stopa", width=100, anchor='center')
        self.listBox.column("Novac posle perioda", width=120, anchor='center')


        self.labelSuma = tk.Label(root, fg="#333333", justify="center", text="Unesite sumu:")
        self.labelSuma.place(x=490, y=70, width=180, height=30)
        self.elements.append(self.labelSuma)

        self.entrySuma = tk.Entry(root, fg="#333333", justify="center")
        self.entrySuma.place(x=530, y=100, width=259, height=30)
        self.elements.append(self.entrySuma)

        self.labelRacun = tk.Label(root, fg="#333333", justify="center", text="Unesite racun:")
        self.labelRacun.place(x=490, y=160, width=180, height=30)
        self.elements.append(self.labelRacun)

        self.entryRacun = tk.Entry(root, fg="#333333", justify="center")
        self.entryRacun.place(x=530, y=200, width=259, height=30)
        self.elements.append(self.entryRacun)

        self.uplatiBtn = tk.Button(root,bg="#7EEBFF", fg="#000000", justify="center", text="Uplati")
        self.uplatiBtn.place(x=610, y=240, width=80, height=30)
        self.uplatiBtn["command"] = self.uplati
        self.elements.append(self.uplatiBtn)

        

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.place(x=10, y=100)

        #id_trans = loadIdTrans(self.jmbg)

        orocava = loadOrocava(self.jmbg)
       
        br_racuna = loadBrRacuna(self.jmbg)
        print("OVO JE BR_RACUNA",br_racuna)


        stedni_racun = loadStedni(br_racuna[0])
        #print(stedni_racun)
        novac_posle = stedni_racun[0][1]+((stedni_racun[0][1]*stedni_racun[0][2])/100)*orocava[0][2]
        self.listBox.insert("", "end", values=(stedni_racun[0][0],stedni_racun[0][1],orocava[0][2],stedni_racun[0][2],novac_posle))
        self.listBox.bind('<Double-Button-1>', lambda event: self.showAgency(event, agencies))
        self.elements.append(self.listBox)


        #clients = loadClients()
       # for client in clients:
       #     self.listBox2.insert("", "end", values=(client[0], client[2]))
        #self.listBox.bind('<Double-Button-1>', lambda event: self.showAgency(event, agencies))
       # self.elements.append(self.listBox2)
       


        self.btnOdjava = tk.Button(root, bg="#f0f0f0", fg="#000000", justify="center", text="Odjava")
        self.btnOdjava.place(x=220, y=360, width=76, height=30)
        self.btnOdjava["command"] = logOut
        self.elements.append(self.btnOdjava)

    
    def uplati(self):
        jmbg = self.jmbg
        br_racuna = loadBrRacuna(jmbg)
        print("broj racuna u uplati::::",br_racuna[0][0])
        suma = self.entrySuma.get()
        racun = self.entryRacun.get()


        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "update stedni_racun set svota_novca = svota_novca+"+suma+" where br_racuna ='"+racun+"'"
        csr.execute(sql)
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "update stedni_racun set svota_novca = svota_novca-"+suma+" where br_racuna ='"+str(br_racuna[0][0])+"'"
        csr.execute(sql)
        con.close()
        

        messagebox.showinfo(title="Uspesno!", message="Uspesno ste orocili novac!")
        self.destroy_all()
        self.__init__(root,controler,jmbg)
        

        

    def povratak(self):
        self.controler.goToLogWin()
        self.controler.goToStudentWin(2)

class show_clients_Window(Window):
    def __init__(self, root, controler,jmbg):
        self.controler = controler
        self.jmbg = jmbg
        Window.__init__(self, root)


        
        # setting title
        root.title("Banka - Pretraga")
        # setting window size
        width = 700
        height = 445
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        #self.labelUserId = tk.Label(root, fg="#333333", justify="center", text="Pretrazi po broju racuna:")
       # self.labelUserId.place(x=60, y=270, width=180, height=30)
      #  self.elements.append(self.labelUserId)

      #  self.inputId = tk.Entry(root, fg="#333333", justify="center")
      #  self.inputId.place(x=40, y=300, width=259, height=30)
      #  self.elements.append(self.inputId)

        self.labelUserName = tk.Label(root, fg="#333333", justify="center", text="Pretrazi po imenu:")
        self.labelUserName.place(x=60, y=300, width=180, height=30)
        self.elements.append(self.labelUserName)

        self.inputUserName = tk.Entry(root, fg="#333333", justify="center")
        self.inputUserName.place(x=40, y=320, width=259, height=30)
        self.elements.append(self.inputUserName)

        self.btnSearchName = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Pretrazi ime")
        self.btnSearchName.place(x=340, y=320, width=80, height=30)
        self.btnSearchName["command"] = self.searchByName
        self.elements.append(self.btnSearchName)

        #self.btnSearch = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Pretrazi")
       # self.btnSearch.place(x=340, y=300, width=80, height=30)
       # self.btnSearch["command"] = self.searchByJmbg
      #  self.elements.append(self.btnSearch)

        self.goBackBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Vrati se")
        self.goBackBtn.place(x=560, y=400, width=80, height=30)
        self.goBackBtn["command"] = self.goBack
        self.elements.append(self.goBackBtn)




        # Dodati stranicu koja ispisuje sve
        cols = ('Broj racuna','Ime','Prezime', 'Orocen novac', 'Period', 'Kamatna stopa')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=10)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox.configure(xscrollcommand=verscrlbar.set)

        self.listBox.column("Broj racuna", width=100, anchor='center')
        self.listBox.column("Ime", width=100, anchor='center')
        self.listBox.column("Prezime", width=100, anchor='center')
        self.listBox.column("Orocen novac", width=100, anchor='center')
        self.listBox.column("Period", width=50, anchor='center')
        self.listBox.column("Kamatna stopa", width=100, anchor='center')
        self.elements.append(self.listBox)



        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.place(x=10, y=20)

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "select jmbg from klijent where admin = 0"
        csr.execute(sql)
        rez = csr.fetchall()
        #print("OVO VRACA REZ: ",rez)
        #print(len(rez))
        #examines = loadExamine(rez[0])

        #print("RACUNI",racuni)
        #svi_klijenti = loadClients(rez[0])
        #print("SVI_KLIJENTI", svi_klijenti)
        #if svi_klijenti[6] == 0:

        for i in range(len(rez)):
 

            klijenti = loadExamine(rez[i][0])
            #print("KLIJENTI: ",klijenti)
            racun = loadBrRacuna(klijenti[0][0])
            #print("RACUN: ",racun[0][0])
            stedni = loadStedni(racun[0])

            orocava = loadOrocava(klijenti[0][0])
            #print(orocava[i][2])

            self.listBox.insert("", "end", values=(stedni[0][0],klijenti[0][1], klijenti[0][2],stedni[0][1],orocava[0][2],stedni[0][2]))
        
        self.elements.append(self.listBox)




    def searchByName(self):
        
        ime = self.inputUserName.get()
        print("OVO JE IME U SEARCHNAME",ime)
        if self.inputUserName.get() == '':
            messagebox.showinfo(title="Paznja!", message="Unesite tekst u polje za pretragu.")
            return
        else:
            self.listBox.destroy()
            self.goBackBtn2 = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Vrati se")
            self.goBackBtn2.place(x=560, y=400, width=80, height=30)
            self.goBackBtn2["command"] = self.goBackSrc
            self.elements.append(self.goBackBtn2)


            

            cols = ('jmbg', 'Ime', 'Prezime')
            self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=10)
            verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
            self.listBox.configure(xscrollcommand=verscrlbar.set)

            self.listBox.column("jmbg", width=50, anchor='center')
            self.listBox.column("Ime", width=100, anchor='center')
            self.listBox.column("Prezime", width=100, anchor='center')

            con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
            csr = con.cursor()
            sql = "select jmbg from klijent where ime ='"+ime+"'"
            csr.execute(sql)
            jmbg = csr.fetchall()
            print("OVO JE JMBG",jmbg[0])

            for col in cols:
                self.listBox.heading(col, text=col)
                self.listBox.grid(row=1, column=0, columnspan=2)
                self.listBox.place(x=10, y=20)

            rez = jmbgSearch(jmbg[0])

            print(rez)
            for klijent in rez:
                self.listBox.insert("", "end", values=(klijent[0], klijent[1], klijent[2]))
        self.elements.append(self.listBox)

        self.labelAgencije = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)

        self.labelKlijenti = tk.Label(root)
        self.labelKlijenti["font"] = ft
        self.labelKlijenti["fg"] = "#333333"
        self.labelKlijenti["justify"] = "left"
        self.labelKlijenti["text"] = 'Oroci novac '
        self.labelKlijenti.place(x=450, y=20, width=150, height=40)
        self.elements.append(self.labelKlijenti)

        self.labelSuma = tk.Label(root, fg="#333333", justify="center", text="Unesite sumu:")
        self.labelSuma.place(x=370, y=70, width=180, height=30)
        self.elements.append(self.labelSuma)

        self.entrySuma = tk.Entry(root, fg="#333333", justify="center")
        self.entrySuma.place(x=410, y=100, width=259, height=30)
        self.elements.append(self.entrySuma)

        self.labelKamata = tk.Label(root, fg="#333333", justify="center", text="Unesite kamatnu stopu:")
        self.labelKamata.place(x=370, y=130, width=220, height=30)
        self.elements.append(self.labelKamata)

        self.entryKamata = tk.Entry(root, fg="#333333", justify="center")
        self.entryKamata.place(x=410, y=160, width=259, height=30)
        self.elements.append(self.entryKamata)

        self.labelPeriod = tk.Label(root, fg="#333333", justify="center", text="Unesite period:")
        self.labelPeriod.place(x=370, y=190, width=180, height=30)
        self.elements.append(self.labelPeriod)

        self.entryPeriod = tk.Entry(root, fg="#333333", justify="center")
        self.entryPeriod.place(x=410, y=220, width=120, height=30)
        self.elements.append(self.entryPeriod)

        self.orociBtn = tk.Button(root,bg="#7EEBFF", fg="#000000", justify="center", text="Oroci")
        self.orociBtn.place(x=560, y=220, width=80, height=30)
        self.orociBtn["command"] = self.oroci
        self.elements.append(self.orociBtn)

        self.orociBtn = tk.Button(root, bg="#FF3F3F", fg="#000000", justify="center", text="Obrisi korisnika")
        self.orociBtn.place(x=120, y=360, width=100, height=30)
        self.orociBtn["command"] = self.obrisi
        self.elements.append(self.orociBtn)

    def oroci(self):
        print("////////////////////////////////////////")
        br_racuna = self.inputId.get()
        print("OVO JE BR_RACUNA U FUNK OROCI",br_racuna)

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "select jmbg from racun where br_racuna ="+br_racuna+""
        csr.execute(sql)
        jmbg = csr.fetchall()
        print("OVO JE JMBG U FUNK OROCI",jmbg[0][0])

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "select period from orocava where jmbg ="+str(jmbg[0][0])+""
        csr.execute(sql)
        period = csr.fetchall()
        print("PERIOOOD: ",period[0][0])

        if period[0][0] != 0:
            messagebox.showerror(title="Greska!", message="Klijent vec ima orocen racun")
            return


        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
            csr = con.cursor()
            sql = "update `stedni_racun` set svota_novca = "+self.entrySuma.get()+",kamatna_stopa="+self.entryKamata.get()+" where br_racuna ="+br_racuna+""
            csr.execute(sql)
            con.close()

            con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
            csr = con.cursor()
            sql = "UPDATE `orocava` SET `period`='"+self.entryPeriod.get()+"' WHERE jmbg ="+str(jmbg[0][0])+""
            csr.execute(sql)
            con.close()

            con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
            csr = con.cursor()
            sql = "insert into `novac`(kolicina) values("+self.entrySuma.get()+")"
            csr.execute(sql)
            con.close()

            messagebox.showinfo(title="Uspesno!", message="Uspesno ste orocili novac!")
            self.goBackSrc()



    def obrisi(self):

        br_racuna = self.inputId.get()
        print("OVO JE BR_RACUNA U FUNK OROCI",br_racuna)

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "select jmbg from racun where br_racuna ="+br_racuna+""
        csr.execute(sql)
        jmbg = csr.fetchall()
        print("OVO JE JMBG U FUNK OROCI",jmbg[0][0])

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "delete from `klijent` where `jmbg`="+str(jmbg[0][0])+""
        csr.execute(sql)
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "delete from `orocava` where `jmbg`="+str(jmbg[0][0])+""
        csr.execute(sql)
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "delete from `racun` where `jmbg`='"+str(jmbg[0][0])+"'"
        csr.execute(sql)
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "delete from `stedna knjizica` where `jmbg_kor`='"+str(jmbg[0][0])+"'"
        csr.execute(sql)
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="banka_db")
        csr = con.cursor()
        sql = "delete from `stedni_racun` where `br_racuna`="+br_racuna+""
        csr.execute(sql)
        con.close()

        messagebox.showinfo(title="Uspesno!", message="Uspesno ste obrisali korisnika!")
        self.goBackSrc()

        
        

    def goBack(self):
        self.controler.goToAdminWin(self.jmbg)
    def goBackSrc(self):
        self.controler.goToShowClients(self.jmbg)
        

        

if __name__ == "__main__":
    root = tk.Tk()
    controler = win_controler(root)
    root.mainloop()
