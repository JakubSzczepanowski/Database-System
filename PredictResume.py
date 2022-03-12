import tkinter as tk
import tkinter.ttk as ttk


class PredictResume:
    def __init__(self, master=None):
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.treeview_1 = ttk.Treeview(self.frame_1)
        self.treeview_1['columns'] = ('Nazwa', 'Przewidywana data dostawy','Stosunek procentowy nowej sprzedaży do starej','Średnia sprzedaż dzienna')
        self.treeview_1.column("#0", width=0)
        self.treeview_1.column("Nazwa", width=100)
        self.treeview_1.column('Przewidywana data dostawy', width=100)
        self.treeview_1.column('Stosunek procentowy nowej sprzedaży do starej', width=130)
        self.treeview_1.column('Średnia sprzedaż dzienna', width=100)
        self.treeview_1.heading("#0", text='', anchor="w")
        self.treeview_1.heading('Nazwa', text='Nazwa')
        self.treeview_1.heading('Przewidywana data dostawy', text='Przewidywana data dostawy')
        self.treeview_1.heading('Stosunek procentowy nowej sprzedaży do starej', text='Stosunek procentowy nowej sprzedaży do starej')
        self.treeview_1.heading('Średnia sprzedaż dzienna', text='Średnia sprzedaż dzienna')
        self.treeview_1.pack(fill='both', expand=True, side='top')

        self.frame_1.configure(height='1000', width='1000')
        self.frame_1.pack(fill='both', expand=True, side='top')

        self.mainwindow = self.frame_1
        x = self.master.winfo_screenwidth() // 2 - 1200 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 400 // 2 - 10
        self.master.resizable(0,0)
        self.master.geometry(f'1200x400+{x}+{y}')
        self.master.title('Przewidywanie dostaw i współczynniki sprzedażowe')

    def add_item(self,record):
        self.treeview_1.insert("", "end", values=record)

    def run(self):
        self.mainwindow.mainloop()