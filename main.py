import tkinter as tk
import tkinter.ttk as ttk
import DB_Connection

class Main:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(anchor='w', font='{Arial} 24 {}', takefocus=False, text='Analizator procesu sprzedaży')
        self.label_1.pack(padx='3', pady='3', side='top')
        self.labelframe_1 = ttk.Labelframe(self.frame_1)
        self.button_1 = ttk.Button(self.labelframe_1)
        self.button_1.configure(text='Analizuj dane sprzedaży')
        self.button_1.pack(fill='x', ipady='5', padx='3', pady='3', side='top')
        self.button_2 = ttk.Button(self.labelframe_1)
        self.button_2.configure(text='Pokaż dane sprzedaży towaru')
        self.button_2.pack(fill='x', ipady='5', padx='3', side='top')
        self.button_3 = ttk.Button(self.labelframe_1)
        self.button_3.configure(text='Sprawdź czy nie potrzebuję dostawy')
        self.button_3.pack(fill='x', ipady='5', padx='3', pady='3', side='top')
        self.labelframe_1.configure(height='200', text='Analiza danych', width='200')
        self.labelframe_1.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.button_4 = ttk.Button(self.frame_1)
        self.button_4.configure(text='Dostawa')
        self.button_4.pack(expand='true', fill='x', ipady='5', padx='3', pady='3', side='left')
        self.button_4.bind('<Button>',self.open_delivery)
        self.button_5 = ttk.Button(self.frame_1)
        self.button_5.configure(text='Aktualizacja')
        self.button_5.pack(expand='true', fill='x', ipady='5', padx='3', pady='3', side='right')
        self.button_1_2 = ttk.Button(self.frame_1)
        self.button_1_2.configure(text='Dodaj produkt')
        self.button_1_2.pack(expand='true', fill='x', ipady='5', padx='3', pady='3', side='left')
        self.button_1_2.bind('<Button>',self.open_adding)
        self.button_3_4 = ttk.Button(self.frame_1)
        self.button_3_4.configure(text='Raport sprzedaży')
        self.button_3_4.pack(expand='true', fill='x', ipady='5', padx='3', pady='3', side='right')
        self.button_3_4.bind('<Button>',self.open_sale)
        self.frame_1.configure(height='200', padding='8', width='200')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1

    def open_sale(self,event):
        import Sale
        dlg = tk.Toplevel(self.master)
        dialog = Sale.Sale(dlg)
        DB_Connection.open_connection()
        dialog.fill_combobox1()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window() 

    def open_adding(self,event):
        import AddProd
        dlg = tk.Toplevel(self.master)
        dialog = AddProd.AddProd(dlg)
        DB_Connection.open_connection()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window() 

    def open_delivery(self,event):
        import Delivery
        dlg = tk.Toplevel(self.master)
        dialog = Delivery.Delivery(dlg)
        DB_Connection.open_connection()
        dialog.fill_combobox1()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg)) # intercept close button
        dialog.master.transient(self.master)   # dialog window is related to main
        dialog.master.wait_visibility() # can't grab until window appears, so we wait
        dialog.master.grab_set()        # ensure all input goes to our window
        dialog.master.wait_window()     # block until window is destroyed

    def close_dialog(self,dialog):
        dialog.grab_release()
        DB_Connection.close_connection()
        dialog.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    import Login
    l = tk.Tk()
    log = Login.Login(l)
    log.run()