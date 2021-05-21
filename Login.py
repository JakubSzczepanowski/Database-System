import tkinter as tk
import tkinter.ttk as ttk


class Login:
    def __init__(self, master=None):
        # build ui
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

        # Main widget
        self.mainwindow = self.frame_1

    def login(self,event):
        import hashlib
        pary = {}
        sh = hashlib.sha1()
        sh.update(self.entry_1.get().encode('utf-8'))
        hash_value1 = sh.hexdigest()
        del sh
        sh = hashlib.sha1()
        sh.update(self.entry_2.get().encode('utf-8'))
        hash_value2 = sh.hexdigest()
        podane = (hash_value1, hash_value2)
        del sh
        with open('login.users','r') as f:
            for linia in f:
                p = linia.strip().split(' - ')
                pary[p[0]] = p[1]
        for i in pary.items():
            if podane == i:
                import os.path
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
                    app.run()


    def run(self):
        self.mainwindow.mainloop()
