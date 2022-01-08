import tkinter as tk
import tkinter.ttk as ttk
from datetime import date
import DB_Connection

class SeasonalResume:
    def __init__(self, master=None):
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}')
        self.label_1.pack(side='top')
        self.treeview_1 = ttk.Treeview(self.frame_1)
        self.treeview_1['columns'] = ('Nazwa', 'Dział')
        self.treeview_1.column("#0", width=0)
        self.treeview_1.column("Nazwa", width=100)
        self.treeview_1.column("Dział", width=120)
        self.treeview_1.heading("#0", text='', anchor="w")
        self.treeview_1.heading('Nazwa', text='Nazwa')
        self.treeview_1.heading('Dział', text='Dział')
        self.treeview_1.pack(fill='both', expand=True, side='top')

        self.frame_1.configure(height='1000', width='1000')
        self.frame_1.pack(fill='both', expand=True, side='top')

        # Main widget
        self.mainwindow = self.frame_1
        x = self.master.winfo_screenwidth() // 2 - 400 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 400 // 2 - 10
        self.master.resizable(0,0)
        self.master.geometry(f'400x400+{x}+{y}')
        self.master.title('Sezonowe produkty')

    def get_seasonal_products(self):
        month_now = date.today().month
        if month_now >= 11 or month_now <= 2:
            products = DB_Connection.select_seasonal_products('Zimowy')
            self.label_1['text'] = 'Sezon Zimowy'
        elif month_now >= 5 or month_now <= 8:
            products = DB_Connection.select_seasonal_products('Letni')
            self.label_1['text'] = 'Sezon Letni'
        else:
            products = DB_Connection.select_seasonal_products('')
            self.label_1['text'] = 'Produkty całoroczne'
        self.add_items(products)

    def add_items(self,records):
        for r in records:
            self.treeview_1.insert("", "end", values=r)

    def run(self):
        self.mainwindow.mainloop()