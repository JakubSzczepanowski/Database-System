import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import DB_Connection
import Exceptions as E


class Sale:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Raport sprzedaży')
        self.label_1.pack(side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_2 = ttk.Label(self.frame_2)
        self.label_2.configure(text='Dział', width='5')
        self.label_2.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.combobox_1 = ttk.Combobox(self.frame_2)
        self.combobox_1.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.combobox_1.bind('<<ComboboxSelected>>',self.fill_combobox2)
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(expand='true', fill='x', side='top')
        self.frame_3 = ttk.Frame(self.frame_1)
        self.label_3 = ttk.Label(self.frame_3)
        self.label_3.configure(text='Nazwa', width='5')
        self.label_3.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.combobox_2 = ttk.Combobox(self.frame_3)
        self.combobox_2.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(expand='true', fill='x', side='top')
        self.frame_4 = ttk.Frame(self.frame_1)
        self.label_4 = ttk.Label(self.frame_4)
        self.label_4.configure(text='Ilość', width='5')
        self.label_4.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.entry_1 = ttk.Entry(self.frame_4)
        self.entry_1.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_4.configure(height='200', width='200')
        self.frame_4.pack(expand='true', fill='x', side='top')
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Dodaj')
        self.button_1.pack(expand='true', fill='x', ipady='10', padx='3', pady='5', side='top')
        self.button_1.bind('<Button>',self.add_sale)
        self.frame_1.configure(height='200', padding='10', width='200')
        self.frame_1.pack(side='top')

    def fill_combobox1(self):
        self.combobox_1['values'] = DB_Connection.get_sections()

    def fill_combobox2(self,event):
        self.combobox_2['values'] = DB_Connection.get_products(self.combobox_1['values'][self.combobox_1.current()])

    def add_sale(self,event):
        import Product as P
        from datetime import datetime
        pr = P.Product(*DB_Connection.get_settings())
        pr.Section = (self.combobox_1['values'][self.combobox_1.current()],self.master)
        pr.Name = (self.combobox_2['values'][self.combobox_2.current()],self.master)
        pr.Amount = (self.entry_1.get(),self.master)
        if DB_Connection.check_amount_correctness(self.master):
            pr.Date = datetime.today().strftime('%Y-%m-%d')
            if self.final_prod_check([pr.Amount,pr.Date]):
                DB_Connection.insert_sale(self.master,pr)

    def final_prod_check(self,prod):
        for p in prod:
            if p is None:
                return False
        return True