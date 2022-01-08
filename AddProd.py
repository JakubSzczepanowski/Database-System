import tkinter as tk
import tkinter.ttk as ttk


class AddProd:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Dodaj nowy produkt')
        self.label_1.pack(side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_2 = ttk.Label(self.frame_2)
        self.label_2.configure(text='Dział', width='5')
        self.label_2.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.entry_1 = ttk.Entry(self.frame_2)
        self.entry_1.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(expand='true', fill='x', side='top')
        self.frame_3 = ttk.Frame(self.frame_1)
        self.label_3 = ttk.Label(self.frame_3)
        self.label_3.configure(text='Nazwa', width='5')
        self.label_3.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.entry_2 = ttk.Entry(self.frame_3)
        self.entry_2.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(expand='true', fill='x', side='top')
        self.frame_4 = ttk.Frame(self.frame_1)
        self.label_4 = ttk.Label(self.frame_4)
        self.label_4.configure(text='Cena netto', width='5')
        self.label_4.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.entry_3 = ttk.Entry(self.frame_4)
        self.entry_3.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_4.configure(height='200', width='200')
        self.frame_4.pack(expand='true', fill='x', side='top')
        self.frame_5 = ttk.Frame(self.frame_1)
        self.label_5 = ttk.Label(self.frame_5)
        self.label_5.configure(text='Procent VAT', width='5')
        self.label_5.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.entry_4 = ttk.Entry(self.frame_5)
        self.entry_4.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_5.configure(height='200', width='200')
        self.frame_5.pack(expand='true', fill='x', side='top')
        self.frame_6 = ttk.Frame(self.frame_1)
        self.label_6 = ttk.Label(self.frame_6)
        self.label_6.configure(text='Sezon', width='5')
        self.label_6.pack(expand='true', fill='x', padx='3', pady='3', side='left')

        self.combobox_1 = ttk.Combobox(self.frame_6,state="readonly", values=('','Letni','Zimowy'))
        self.combobox_1.pack(expand='true', fill='x', padx='3', pady='3', side='left')
        self.frame_6.configure(height='200', width='200')
        self.frame_6.pack(expand='true', fill='x', side='top')
        
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Dodaj produkt')
        self.button_1.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='top')
        self.button_1.bind('<Button>',self.add_product)
        self.frame_1.configure(height='200', padding='10', width='200')
        self.frame_1.pack(side='top')

        x = self.master.winfo_screenwidth() // 2 - 301 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 223 // 2 - 10
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Dodaj nowy produkt')
    
    def add_product(self,event):
        import Product as P
        import DB_Connection
        pr = P.Product(*DB_Connection.get_settings())
        pr.Section = (self.entry_1.get(),self.master)
        pr.Name = (self.entry_2.get(),self.master)
        pr.Netto_price = (self.entry_3.get(),self.master)
        pr.Vat_percentage = (self.entry_4.get(),self.master)
        pr.Season = self.combobox_1['values'][self.combobox_1.current()]
        if pr.final_prod_check([pr.Section,pr.Name,pr.Netto_price,pr.Vat_percentage]):
            DB_Connection.insert_product(self.master,pr)