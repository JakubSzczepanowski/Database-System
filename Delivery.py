import tkinter as tk
import tkinter.ttk as ttk
import DB_Connection

class Delivery:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Dostawa produktu')
        self.label_1.pack(anchor='center', fill='y', side='top')
        self.frame_6 = ttk.Frame(self.frame_1)
        self.label_6 = ttk.Label(self.frame_6)
        self.label_6.configure(text='Dział', width='15')
        self.label_6.pack(fill='x', padx='5', pady='5', side='left')
        self.combobox_1 = ttk.Combobox(self.frame_6)
        self.combobox_1.pack(expand='true', fill='x', side='left')
        self.combobox_1.bind('<<ComboboxSelected>>',self.fill_combobox2)
        self.frame_6.configure(height='200', width='200')
        self.frame_6.pack(expand='true', fill='x', side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_2 = ttk.Label(self.frame_2)
        self.label_2.configure(text='Nazwa', width='15')
        self.label_2.pack(fill='x', padx='5', pady='5', side='left')
        self.combobox_2 = ttk.Combobox(self.frame_2)
        self.combobox_2.pack(expand='true', fill='x', side='left')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(expand='true', fill='x', side='top')
        self.frame_4 = ttk.Frame(self.frame_1)
        self.label_4 = ttk.Label(self.frame_4)
        self.label_4.configure(text='Cena hurtowa', width='15')
        self.label_4.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_3 = ttk.Entry(self.frame_4)
        self.entry_3.pack(expand='true', fill='x', side='left')
        self.frame_4.configure(height='200', width='200')
        self.frame_4.pack(expand='true', fill='x', side='top')
        self.frame_5 = ttk.Frame(self.frame_1)
        self.label_5 = ttk.Label(self.frame_5)
        self.label_5.configure(text='Ilość', width='15')
        self.label_5.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_4 = ttk.Entry(self.frame_5)
        self.entry_4.pack(expand='true', fill='x', side='left')
        self.frame_5.configure(height='200', width='200')
        self.frame_5.pack(expand='true', fill='x', side='top')
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Dodaj')
        self.button_1.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='top')
        self.button_1.bind('<Button>',self.add_delivery)
        self.frame_1.configure(height='200', padding='10', width='200')
        self.frame_1.pack(side='top')

    def fill_combobox1(self):
        self.combobox_1['values'] = DB_Connection.get_sections()

    def fill_combobox2(self,event):
        self.combobox_2['values'] = DB_Connection.get_products(self.combobox_1['values'][self.combobox_1.current()].replace(' ','_'))

    def add_delivery(self,event):
        import Product as P
        from datetime import datetime
        pr = P.Product(*DB_Connection.get_settings())
        pr.Section = (self.combobox_1['values'][self.combobox_1.current()].replace(' ','_'),self.master)
        pr.Name = (self.combobox_2['values'][self.combobox_2.current()],self.master)
        pr.Quantity_price = (self.entry_3.get(),self.master)
        pr.Amount = (self.entry_4.get(),self.master)
        x = DB_Connection.get_last_amount_and_quantity_price(self.master,pr)
        amount = x[0] if x is not None else 0
        pr.Amount = (str(amount + pr.Amount),self.master)
        pr.Date = datetime.today().strftime('%Y-%m-%d')
        if self.final_prod_check([pr.Quantity_price,pr.Amount,pr.Date]):
            DB_Connection.insert_update(self.master,pr)

    def final_prod_check(self,prod):
        for p in prod:
            if p is None:
                return False
        return True
