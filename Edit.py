import tkinter as tk
from tkinter.constants import END, X
import tkinter.ttk as ttk
import DB_Connection
from tkinter import messagebox

class Edit:
    def __init__(self, master,type):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.treeview_1 = ttk.Treeview(self.frame_1)
        self.treeview_1.pack(side='top')
        self.treeview_1.bind('<<TreeviewSelect>>', self.on_select)
        self.frame_1.configure(height='200', width='200')
        self.frame_1.pack(side='top')
        self.id = None
        if type == 0:
            self.treeview_1['columns'] = ('ID','Nazwa','Cena netto','Procent VAT','Dział')
            self.treeview_1.column("#0", width=0)
            self.treeview_1.column('ID', width=100)
            self.treeview_1.column('Nazwa', width=100)
            self.treeview_1.column('Cena netto', width=100)
            self.treeview_1.column('Procent VAT', width=100)
            self.treeview_1.column('Dział', width=100)
            self.treeview_1.heading("#0", text='', anchor="w")
            self.treeview_1.heading('ID', text='ID')
            self.treeview_1.heading('Nazwa', text='Nazwa')
            self.treeview_1.heading('Cena netto', text='Cena netto')
            self.treeview_1.heading('Procent VAT', text='Procent VAT')
            self.treeview_1.heading('Dział', text='Dział')

            self.frame_2 = ttk.Frame(self.frame_1)
            self.entry_1 = ttk.Entry(self.frame_2)
            self.entry_1.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_2 = ttk.Entry(self.frame_2)
            self.entry_2.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_3 = ttk.Entry(self.frame_2)
            self.entry_3.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_4 = ttk.Entry(self.frame_2)
            self.entry_4.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.frame_2.configure(height='200', width='200')
            self.frame_2.pack(fill='x', side='top')

            self.frame_1.configure(height='200', padding='8', width='200')
            self.frame_1.pack(side='top')

        self.frame_3 = ttk.Frame(self.frame_1)
        self.button_1 = ttk.Button(self.frame_3)
        self.button_1.configure(text='Edytuj')
        self.button_1.pack(expand='true', fill='x', ipadx='3', ipady='3', side='top')
        self.button_1.bind('<Button>', self.edit)
        self.button_2 = ttk.Button(self.frame_3)
        self.button_2.configure(text='Usuń')
        self.button_2.pack(expand='true', fill='x', ipadx='3', ipady='3', side='top')
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(fill='x', side='top')
        self.add_items(DB_Connection.select_products())

        # Main widget
        self.mainwindow = self.frame_1

    def add_items(self,records):
        for r in records:
            self.treeview_1.insert("", "end", values=r)

    def edit(self,event):
        if self.id is not None and self.treeview_1.selection() != ():
            import Product as P
            pr = P.Product(*DB_Connection.get_settings())
            pr.Name = (self.entry_1.get(),self.master)
            pr.Netto_price = (self.entry_2.get(),self.master)
            pr.Vat_percentage = (self.entry_3.get(),self.master)
            pr.Section = (self.entry_4.get(),self.master)
            if self.final_prod_check([pr.Section,pr.Name,pr.Netto_price,pr.Vat_percentage]):
                DB_Connection.edit_product(self.master,pr,self.id)
                focused = self.treeview_1.focus()
                self.treeview_1.insert("", str(focused)[1:], values=(self.id,pr.Name,pr.Netto_price,pr.Vat_percentage,pr.Section))
                self.treeview_1.delete(focused)
        else:
            messagebox.showerror(parent=self.master, title='Błąd',message='Zaznacz element, który chcesz edytować')

    def final_prod_check(self,prod):
        for p in prod:
            if p is None:
                return False
        return True

    def on_select(self,event):
        selected = event.widget.focus()
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        item = self.treeview_1.item(selected)['values']
        self.id = item[0]
        self.entry_1.insert(0,item[1])
        self.entry_2.insert(0,item[2])
        self.entry_3.insert(0,item[3])
        self.entry_4.insert(0,item[4])

    def run(self):
        self.mainwindow.mainloop()
