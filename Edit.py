import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import DISABLED, END
import DB_Connection
from tkinter import messagebox
from tkcalendar import DateEntry

class Edit:
    def __init__(self, master,type):
        self.master = master
        self.type = type
        self.frame_1 = ttk.Frame(self.master)
        self.frame_4 = ttk.Frame(self.frame_1)
        self.treeview_1 = ttk.Treeview(self.frame_4)
        self.treeview_1.pack(side='left')
        self.frame_4.configure(height='200', width='200')
        self.frame_4.pack(expand='true', fill='x', padx='10', pady='10', side='top')

        self.frame_5 = ttk.Frame(self.frame_4)
        self.label_1 = ttk.Label(self.frame_5)
        self.label_1.configure(text='Dział', width='15')
        self.label_1.pack(padx='5', pady='5', side='left')
        self.combobox_1 = ttk.Combobox(self.frame_5,state="readonly")
        self.combobox_1.pack(expand='true', fill='x', side='left')
        self.combobox_1.bind('<<ComboboxSelected>>',self.fill_combobox2)
        self.frame_5.configure(height='200', width='200')
        self.frame_5.pack(expand='true', fill='x', side='top')
        self.frame_6 = ttk.Frame(self.frame_4)
        self.label_2 = ttk.Label(self.frame_6)
        self.label_2.configure(text='Nazwa', width='15')
        self.label_2.pack(padx='5', pady='5', side='left')
        self.combobox_2 = ttk.Combobox(self.frame_6,state="readonly")
        self.combobox_2.pack(expand='true', fill='x', side='left')
        self.frame_6.configure(height='200', width='200')
        self.frame_6.pack(expand='true', fill='x', side='top')

        self.frame_7 = ttk.Frame(self.frame_4)
        self.label_3 = ttk.Label(self.frame_7)
        self.label_3.configure(text='Cena hurtowa', width='15')
        self.label_3.pack(padx='3', pady='3', side='left')
        self.entry_5 = ttk.Entry(self.frame_7)
        self.entry_5.pack(expand='true', fill='x', side='left')
        self.frame_7.configure(height='200', width='200')
        self.frame_7.pack(expand='true', fill='x', side='top')

        self.frame_8 = ttk.Frame(self.frame_4)
        self.label_4 = ttk.Label(self.frame_8)
        self.label_4.configure(text='Ilość', width='15')
        self.label_4.pack(padx='3', pady='3', side='left')
        self.entry_6 = ttk.Entry(self.frame_8)
        self.entry_6.pack(expand='true', fill='x', side='left')
        self.frame_8.configure(height='200', width='200')
        self.frame_8.pack(expand='true', fill='x', side='top')

        self.frame_9 = ttk.Frame(self.frame_4)
        self.label_5 = ttk.Label(self.frame_9)
        self.label_5.configure(text='Cena netto', width='15')
        self.label_5.pack(padx='3', pady='3', side='left')
        self.entry_7 = ttk.Entry(self.frame_9)
        self.entry_7.pack(expand='true', fill='x', side='left')
        self.frame_9.configure(height='200', width='200')
        self.frame_9.pack(expand='true', fill='x', side='top')

        self.frame_10 = ttk.Frame(self.frame_4)
        self.label_6 = ttk.Label(self.frame_10)
        self.label_6.configure(text='Procent VAT', width='15')
        self.label_6.pack(padx='3', pady='3', side='left')
        self.entry_8 = ttk.Entry(self.frame_10)
        self.entry_8.pack(expand='true', fill='x', side='left')
        self.frame_10.configure(height='200', width='200')
        self.frame_10.pack(expand='true', fill='x', side='top')

        self.frame_11 = ttk.Frame(self.frame_4)
        self.label_7 = ttk.Label(self.frame_11)
        self.label_7.configure(text='Data', width='15')
        self.label_7.pack(padx='3', pady='3', side='left')
        self.dateEntry = DateEntry(self.frame_11, width=12, background='darkblue',locale="pl_PL",date_pattern="yyyy-mm-dd", foreground='white', borderwidth=2)
        self.dateEntry.delete(0,END)
        self.dateEntry.pack(expand='true', fill='x', side='left')
        self.frame_11.configure(height='200', width='200')
        self.frame_11.pack(expand='true', fill='x', side='top')

        self.frame_13 = ttk.Frame(self.frame_4)
        self.label_8 = ttk.Label(self.frame_13)
        self.label_8.configure(text='Sezon', width='15')
        self.label_8.pack(padx='5', pady='5', side='left')
        self.combobox_4 = ttk.Combobox(self.frame_13,state="readonly", values=('Całoroczne','Letni','Zimowy'))
        self.combobox_4.pack(expand='true', fill='x', side='left')
        self.frame_13.configure(height='200', width='200')
        self.frame_13.pack(expand='true', fill='x', side='top')

        self.frame_12 = ttk.Frame(self.frame_4)
        self.button_3 = ttk.Button(self.frame_12)
        self.button_3.configure(text='Filtruj')
        self.button_3.bind('<Button>', self.filter)
        self.button_3.pack(expand='true', fill='x', side='left')
        self.button_4 = ttk.Button(self.frame_12)
        self.button_4.configure(text='Wyczyść')
        self.button_4.bind('<Button>', self.clear)
        self.button_4.pack(expand='true', fill='x', side='left')
        self.frame_12.configure(height='200', width='200')
        self.frame_12.pack(expand='true', fill='x', side='top', padx='3')
        
        self.frame_1.configure(height='200', width='200')
        self.frame_1.pack(side='top')
        self.id = None
        if self.type == 0:
            self.treeview_1['columns'] = ('ID','Nazwa','Cena netto','Procent VAT','Dział','Sezon')
            self.treeview_1.column("#0", width=0)
            self.treeview_1.column('ID', width=30)
            self.treeview_1.column('Nazwa', width=130)
            self.treeview_1.column('Cena netto', width=80)
            self.treeview_1.column('Procent VAT', width=80)
            self.treeview_1.column('Dział', width=150)
            self.treeview_1.column('Sezon', width=80)
            self.treeview_1.heading("#0", text='', anchor="w")
            self.treeview_1.heading('ID', text='ID')
            self.treeview_1.heading('Nazwa', text='Nazwa')
            self.treeview_1.heading('Cena netto', text='Cena netto')
            self.treeview_1.heading('Procent VAT', text='Procent VAT')
            self.treeview_1.heading('Dział', text='Dział')
            self.treeview_1.heading('Sezon', text='Sezon')
            self.add_items(DB_Connection.select_products())
            self.treeview_1.bind('<<TreeviewSelect>>', self.on_select_products)

            self.entry_5.config(state='disabled')
            self.entry_6.config(state='disabled')
            self.dateEntry.config(state='disabled')

            self.frame_2 = ttk.Frame(self.frame_1)
            self.entry_1 = ttk.Entry(self.frame_2)
            self.entry_1.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_2 = ttk.Entry(self.frame_2)
            self.entry_2.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_3 = ttk.Entry(self.frame_2)
            self.entry_3.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_4 = ttk.Entry(self.frame_2)
            self.entry_4.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.combobox_3 = ttk.Combobox(self.frame_2, state="readonly", values=('','Letni','Zimowy'))
            self.combobox_3.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.frame_2.configure(height='200', width='200')
            self.frame_2.pack(fill='x', side='top')

        elif self.type == 1:
            self.treeview_1['columns'] = ('ID','Data','Nazwa','Cena hurtowa','Ilość','Dział')
            self.treeview_1.column("#0", width=0)
            self.treeview_1.column('ID', width=30)
            self.treeview_1.column('Data', width=80)
            self.treeview_1.column('Nazwa', width=130)
            self.treeview_1.column('Cena hurtowa', width=100)
            self.treeview_1.column('Ilość', width=80)
            self.treeview_1.column('Dział', width=150)
            self.treeview_1.heading("#0", text='', anchor="w")
            self.treeview_1.heading('ID', text='ID')
            self.treeview_1.heading('Data', text='Data')
            self.treeview_1.heading('Nazwa', text='Nazwa')
            self.treeview_1.heading('Cena hurtowa', text='Cena hurtowa')
            self.treeview_1.heading('Ilość', text='Ilość')
            self.treeview_1.heading('Dział', text='Dział')
            self.add_items(DB_Connection.select_supplies())
            self.treeview_1.bind('<<TreeviewSelect>>', self.on_select_supplies)

            self.entry_7.config(state='disabled')
            self.entry_8.config(state='disabled')
            self.combobox_4.config(state='disabled')

            self.frame_2 = ttk.Frame(self.frame_1)
            self.entry_1 = ttk.Entry(self.frame_2)
            self.entry_1.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.entry_2 = ttk.Entry(self.frame_2)
            self.entry_2.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.frame_2.configure(height='200', width='200')
            self.frame_2.pack(fill='x', side='top')

        elif self.type == 2:
            self.treeview_1['columns'] = ('ID','Data','Nazwa','Ilość','Dział')
            self.treeview_1.column("#0", width=0)
            self.treeview_1.column('ID', width=30)
            self.treeview_1.column('Data', width=80)
            self.treeview_1.column('Nazwa', width=130)
            self.treeview_1.column('Ilość', width=80)
            self.treeview_1.column('Dział', width=150)
            self.treeview_1.heading("#0", text='', anchor="w")
            self.treeview_1.heading('ID', text='ID')
            self.treeview_1.heading('Data', text='Data')
            self.treeview_1.heading('Nazwa', text='Nazwa')
            self.treeview_1.heading('Ilość', text='Ilość')
            self.treeview_1.heading('Dział', text='Dział')
            self.add_items(DB_Connection.select_sales())
            self.treeview_1.bind('<<TreeviewSelect>>', self.on_select_sales)

            self.entry_5.config(state='disabled')
            self.entry_7.config(state='disabled')
            self.entry_8.config(state='disabled')
            self.combobox_4.config(state='disabled')

            self.frame_2 = ttk.Frame(self.frame_1)
            self.entry_1 = ttk.Entry(self.frame_2)
            self.entry_1.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
            self.frame_2.configure(height='200', width='200')
            self.frame_2.pack(fill='x', side='top')

        self.frame_3 = ttk.Frame(self.frame_1)
        self.button_1 = ttk.Button(self.frame_3)
        self.button_1.configure(text='Edytuj')
        self.button_1.pack(expand='true', fill='x', ipadx='3', ipady='3', side='top')
        self.button_1.bind('<Button>', self.edit)
        self.button_2 = ttk.Button(self.frame_3)
        self.button_2.configure(text='Usuń')
        self.button_2.pack(expand='true', fill='x', ipadx='3', ipady='3', side='top')
        self.button_2.bind('<Button>', self.delete)
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(fill='x', side='top')
        self.frame_1.configure(height='200', padding='8', width='200')
        self.frame_1.pack(side='top')
        
        self.mainwindow = self.frame_1
        if self.type == 0:
            a,b = 720,349
        elif self.type == 1:
            a,b = 839,346
        else:
            a,b = 739,346
        x = self.master.winfo_screenwidth() // 2 - a // 2 - 10
        y = self.master.winfo_screenheight() // 2 - b // 2 - 10
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Edytuj')

    def fill_combobox1(self):
        self.combobox_1['values'] = DB_Connection.get_sections()

    def fill_combobox2(self,event):
        self.combobox_2.set('')
        self.combobox_2['values'] = DB_Connection.get_products_for_section(self.combobox_1['values'][self.combobox_1.current()])

    def filter(self, event):
        params = {}
        params['Products.section'], params['Products.name'], params['Data.quantity_price'], params['Data.amount'], params['Products.netto_price'], params['Products.vat_percentage'], params['Data.date'], params['Products.season'] = \
            self.combobox_1.get(), self.combobox_2.get(), self.entry_5.get(), self.entry_6.get(), self.entry_7.get(), self.entry_8.get(), self.dateEntry.get_date().strftime('%Y-%m-%d') if self.dateEntry._validate_date() else "", self.combobox_4.get()
        filtered_grid = DB_Connection.select_with_filters(self.type, params)
        self.treeview_1.delete(*self.treeview_1.get_children())
        self.dateEntry.delete(0, END)
        self.add_items(filtered_grid)

    def clear(self, event):
        self.combobox_1.set('')
        self.combobox_2.set('')
        self.entry_5.delete(0, END)
        self.entry_6.delete(0, END)
        self.entry_7.delete(0, END)
        self.entry_8.delete(0, END)
        self.dateEntry.delete(0, END)
        self.combobox_4.set('')

    def add_items(self,records):
        for r in records:
            self.treeview_1.insert("", "end", values=r)

    def edit(self,event):
        if self.id is not None and self.treeview_1.selection() != ():
            import Product as P
            pr = P.Product(*DB_Connection.get_settings())
            if self.type == 0:
                pr.Name = (self.entry_1.get(),self.master)
                pr.Netto_price = (self.entry_2.get(),self.master)
                pr.Vat_percentage = (self.entry_3.get(),self.master)
                pr.Section = (self.entry_4.get(),self.master)
                pr.Season = self.combobox_3['values'][self.combobox_3.current()]
                if pr.final_prod_check([pr.Section,pr.Name,pr.Netto_price,pr.Vat_percentage]):
                    DB_Connection.edit_product(self.master,pr,self.id)
                    focused = self.treeview_1.focus()
                    self.treeview_1.item(focused, values=(self.id,pr.Name,pr.Netto_price,pr.Vat_percentage,pr.Section,pr.Season))
            elif self.type == 1:
                pr.Quantity_price = (self.entry_1.get(),self.master)
                pr.Amount = (self.entry_2.get(),self.master)
                if pr.final_prod_check([pr.Quantity_price,pr.Amount]):
                    DB_Connection.edit_supply(self.master,pr,self.id)
                    focused = self.treeview_1.focus()
                    item = self.treeview_1.item(focused)['values']
                    self.treeview_1.item(focused, values=(self.id,item[1],item[2],pr.Quantity_price,pr.Amount,item[5]))
            else:
                pr.Amount = (self.entry_1.get(),self.master)
                if pr.final_prod_check([pr.Amount]):
                    DB_Connection.edit_sale(self.master,pr,self.id)
                    focused = self.treeview_1.focus()
                    item = self.treeview_1.item(focused)['values']
                    self.treeview_1.item(focused, values=(self.id,item[1],item[2],pr.Amount,item[4]))
        else:
            messagebox.showerror(parent=self.master, title='Błąd',message='Zaznacz element, który chcesz edytować')

    def delete(self,event):
        if self.id is not None and self.treeview_1.selection() != ():
            if self.type == 0:
                DB_Connection.delete_product(self.id)
            else:
                DB_Connection.delete_supply_or_sale(self.id)
            focused = self.treeview_1.focus()
            self.treeview_1.delete(focused)
        else:
            messagebox.showerror(parent=self.master, title='Błąd',message='Zaznacz element, który chcesz usunąć')

    def on_select_products(self,event):
        selected = event.widget.focus()
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END) 
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        self.combobox_3.set('')
        item = self.treeview_1.item(selected)['values']
        self.id = item[0]
        self.entry_1.insert(0,item[1])
        self.entry_2.insert(0,item[2])
        self.entry_3.insert(0,item[3])
        self.entry_4.insert(0,item[4])
        self.combobox_3.set(item[5])

    def on_select_supplies(self,event):
        selected = event.widget.focus()
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        item = self.treeview_1.item(selected)['values']
        self.id = item[0]
        self.entry_1.insert(0,item[3])
        self.entry_2.insert(0,item[4])

    def on_select_sales(self,event):
        selected = event.widget.focus()
        self.entry_1.delete(0,END)
        item = self.treeview_1.item(selected)['values']
        self.id = item[0]
        self.entry_1.insert(0,item[3])

    def run(self):
        self.mainwindow.mainloop()

