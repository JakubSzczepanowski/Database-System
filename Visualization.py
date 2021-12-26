import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import DB_Connection
import analytics

class Visualization:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Wybierz produkt do wizualizacji')
        self.label_1.pack(anchor='center', fill='y', side='top')
        self.frame_6 = ttk.Frame(self.frame_1)
        self.label_6 = ttk.Label(self.frame_6)
        self.label_6.configure(text='Dział', width='15')
        self.label_6.pack(fill='x', padx='5', pady='5', side='left')
        self.combobox_1 = ttk.Combobox(self.frame_6, state="readonly")
        self.combobox_1.pack(expand='true', fill='x', side='left')
        self.combobox_1.bind('<<ComboboxSelected>>',self.fill_combobox2)
        self.frame_6.configure(height='200', width='200')
        self.frame_6.pack(expand='true', fill='x', side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_2 = ttk.Label(self.frame_2)
        self.label_2.configure(text='Nazwa', width='15')
        self.label_2.pack(fill='x', padx='5', pady='5', side='left')
        self.combobox_2 = ttk.Combobox(self.frame_2 ,state="readonly")
        self.combobox_2.pack(expand='true', fill='x', side='left')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(expand='true', fill='x', side='top')
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Pokaż wykres dostaw w funkcji czasu')
        self.button_1.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='top')
        self.button_1.bind('<Button>', self.show_supplies_in_time)
        self.button_1_1 = ttk.Button(self.frame_1)
        self.button_1_1.configure(text='Pokaż wykres sprzedaży w funkcji czasu')
        self.button_1_1.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='top')
        self.button_1_1.bind('<Button>', self.show_sales_in_time)
        self.button_1_2 = ttk.Button(self.frame_1)
        self.button_1_2.configure(text='Pokaż wykres ilościowy w funkcji czasu')
        self.button_1_2.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='top')
        self.button_1_2.bind('<Button>', self.show_amount_in_time)
        self.frame_1.configure(height='200', padding='10', width='200')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1
        x = self.master.winfo_screenwidth() // 2 - 278 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 231 // 2 - 10
        self.master.resizable(0,0)
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Wizualizuj dane sprzedaży')

    def run(self):
        self.mainwindow.mainloop()

    def show_supplies_in_time(self,event):
        try:
            analytics.show_supply_plot(self.combobox_2['values'][self.combobox_2.current()])
        except IndexError:
            messagebox.showerror(parent=self.master,title='Błąd',message='Nie można utworzyć wykresu z powodu braku danych')

    def show_sales_in_time(self,event):
        try:
            analytics.show_sale_plot(self.combobox_2['values'][self.combobox_2.current()])
        except IndexError:
            messagebox.showerror(parent=self.master,title='Błąd',message='Nie można utworzyć wykresu z powodu braku danych')

    def show_amount_in_time(self, event):
        try:
            analytics.show_cumulative_amount_plot(self.combobox_2['values'][self.combobox_2.current()])
        except IndexError:
            messagebox.showerror(parent=self.master,title='Błąd',message='Nie można utworzyć wykresu z powodu braku danych')

    def fill_combobox1(self):
        self.combobox_1['values'] = DB_Connection.get_sections()

    def fill_combobox2(self,event):
        self.combobox_2['values'] = DB_Connection.get_products(self.combobox_1['values'][self.combobox_1.current()])