import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import DB_Connection

class Login:
    def __init__(self, master=None):
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(anchor='center', font='{Arial} 24 {}', text='Zaloguj się')
        self.label_1.pack(expand='true', fill='x', padx='2', pady='2', side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_3 = ttk.Label(self.frame_2)
        self.label_3.configure(anchor='center', text='Login:', width='15')
        self.label_3.pack(padx='5', pady='5', side='left')
        self.entry_1 = ttk.Entry(self.frame_2)
        self.entry_1.pack(padx='5', pady='5', side='left')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(side='top')
        self.frame_3 = ttk.Frame(self.frame_1)
        self.label_4 = ttk.Label(self.frame_3)
        self.label_4.configure(anchor='center', text='Hasło:', width='15')
        self.label_4.pack(padx='5', pady='5', side='left')
        self.entry_2 = ttk.Entry(self.frame_3,show='*')
        self.entry_2.pack(padx='5', pady='5', side='left')
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(side='top')
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Zaloguj się')
        self.button_1.pack(fill='x', ipadx='5', ipady='5', padx='5', pady='5', side='top')
        self.button_1.bind('<Button>', self.login)
        self.frame_1.configure(height='200', width='200')
        self.frame_1.pack(side='top')

        self.mainwindow = self.frame_1
        self.master.resizable(0,0)
        x = self.master.winfo_screenwidth() // 2 - 240 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 151 // 2 - 10
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Zaloguj się')

    def login(self,event):
        import hashlib
        import os.path
        if os.path.isfile('login.user'):
            sh = hashlib.sha3_256()
            sh.update(self.entry_1.get().encode('utf-8'))
            hash_value1 = sh.digest()
            del sh
            sh = hashlib.sha3_256()
            sh.update(self.entry_2.get().encode('utf-8'))
            hash_value2 = sh.digest()
            del sh
            with open('login.user','br') as f:
                content = f.read()
                if hash_value1 == content[:32] and hash_value2 == content[32:]:
                    if not os.path.isfile('database.db'):
                        import DB_Setup
                        r = tk.Tk()
                        db_setup = DB_Setup.DB_Setup(r)
                        self.master.destroy()
                        db_setup.run()
                    else:
                        import main
                        root = tk.Tk()
                        app = main.Main(root)
                        self.master.destroy()
                        DB_Connection.open_connection()
                        app.run()
                else:
                    messagebox.showerror('Błąd logowania','Niepoprawne login lub hasło')
        else:
            messagebox.showerror('Błąd logowania','Brakuje pliku konfiguracyjnego login.user')


    def run(self):
        self.mainwindow.mainloop()
