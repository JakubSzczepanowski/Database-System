import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import DB_Connection
from analytics import predict_resume
import threading
import os

class Main:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Panel główny')
        self.menu = tk.Menu(self.master, tearoff=0)
        self.database_menu = tk.Menu(self.menu, tearoff=0)
        self.database_menu.add_command(label='Eksportuj', command=self.export_database)
        self.database_menu.add_command(label='Importuj', command=self.import_database)
        self.database_menu.add_command(label='Usuń', command=self.delete_database)
        self.menu.add_cascade(label='Baza danych', menu=self.database_menu)
        self.master.config(menu=self.menu)
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(anchor='w', font='{Arial} 24 {}', takefocus=False, text='Analizator procesu sprzedaży')
        self.label_1.pack(padx='3', pady='3', side='top')
        self.labelframe_1 = ttk.Labelframe(self.frame_1)
        self.button_1 = ttk.Button(self.labelframe_1)
        self.button_1.configure(text='Wizualizuj dane')
        self.button_1.pack(fill='x', ipady='5', padx='3', pady='3', side='top')
        self.button_1.bind('<Button>', self.open_visualisation)
        self.button_2 = ttk.Button(self.labelframe_1)
        self.button_2.configure(text='Pokaż sezonowe produkty')
        self.button_2.pack(fill='x', ipady='5', padx='3', side='top')
        self.button_2.bind('<Button>', self.open_seasonal_result)
        self.button_3 = ttk.Button(self.labelframe_1)
        self.button_3.configure(text='Analizuj sprzedaż')
        self.button_3.pack(fill='x', ipady='5', padx='3', pady='3', side='top')
        self.button_3.bind('<Button>', self.open_predict_resume)
        self.labelframe_1.configure(height='200', text='Analiza danych', width='200')
        self.labelframe_1.pack(expand='true', fill='both', padx='5', pady='5', side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.button_4 = ttk.Button(self.frame_2)
        self.button_4.configure(text='Produkt')
        self.button_4.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
        self.button_4.bind('<Button>',self.open_adding)
        self.button_5 = ttk.Button(self.frame_2)
        self.button_5.configure(text='Dostawa')
        self.button_5.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
        self.button_5.bind('<Button>',self.open_supply)
        self.button_6 = ttk.Button(self.frame_2)
        self.button_6.configure(text='Sprzedaż')
        self.button_6.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='left')
        self.button_6.bind('<Button>',self.open_sale)
        self.labelframe_2 = ttk.Labelframe(self.frame_2)
        self.combobox_1 = ttk.Combobox(self.labelframe_2,state="readonly",values=('Produkty','Dostawy','Sprzedaże'))
        self.combobox_1.pack(padx='5', pady='5', side='top')
        self.combobox_1.current(0)
        self.button_6 = ttk.Button(self.labelframe_2)
        self.button_6.configure(text='Edytuj')
        self.button_6.pack(expand='true', fill='x', ipadx='3', ipady='3', side='top')
        self.button_6.bind('<Button>',lambda x: self.open_edit(self.combobox_1.current()))
        self.labelframe_2.configure(height='200', text='Edycja danych', width='200')
        self.labelframe_2.pack(expand='true', fill='x', ipadx='8', ipady='8', padx='2', pady='2', side='top')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(fill='x', side='top')
        self.frame_1.configure(height='200', padding='8', width='200')
        self.frame_1.pack(side='top')

        self.mainwindow = self.frame_1
        self.master.resizable(0,0)
        x = self.master.winfo_screenwidth() // 2 - 514 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 309 // 2 - 10
        self.master.geometry(f'+{x}+{y}')
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)

    def open_sale(self,event):
        if self.check_database(): return
        import Sale
        dlg = tk.Toplevel(self.master)
        dialog = Sale.Sale(dlg)
        dialog.fill_combobox1()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window() 

    def open_adding(self,event):
        if self.check_database(): return
        import AddProd
        dlg = tk.Toplevel(self.master)
        dialog = AddProd.AddProd(dlg)
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window()

    def open_edit(self,type):
        if self.check_database(): return
        import Edit
        dlg = tk.Toplevel(self.master)
        dialog = Edit.Edit(dlg,type)
        dialog.fill_combobox1()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window()

    def open_supply(self,event):
        if self.check_database(): return
        import Supply
        dlg = tk.Toplevel(self.master)
        dialog = Supply.Supply(dlg)
        dialog.fill_combobox1()
        dialog.master.protocol("WM_DELETE_WINDOW", lambda arg=dialog.master: self.close_dialog(arg))
        dialog.master.transient(self.master)
        dialog.master.wait_visibility()
        dialog.master.grab_set()
        dialog.master.wait_window()

    def open_visualisation(self,event):
        if self.check_database(): return
        import Visualization
        r = tk.Tk()
        dialog = Visualization.Visualization(r)
        dialog.fill_combobox1()
        dialog.run()
    
    def calculate_predicts(self):
        self.button_3.config(state=tk.DISABLED)
        import PredictResume
        r = tk.Tk()
        dialog = PredictResume.PredictResume(r)
        for name in DB_Connection.select_products_names():
            try:
                resume = predict_resume(name[0])
            except IndexError:
                resume = (name[0], 'Brak danych', 'Brak danych', 'Brak danych')
            except ZeroDivisionError:
                resume = (name[0], 'Nie potrzebujesz dostawy', 'Większa obniżka', 0)
            dialog.add_item(resume)
        self.button_3.config(state=tk.NORMAL)
        dialog.run()

    def open_predict_resume(self, event):
        if self.check_database(): return
        threading.Thread(target=self.calculate_predicts).start()
        

    def open_seasonal_result(self, event):
        if self.check_database(): return
        import SeasonalResume
        r = tk.Tk()
        dialog = SeasonalResume.SeasonalResume(r)
        dialog.get_seasonal_products()
        dialog.run()

    def close_dialog(self,dialog):
        dialog.grab_release()
        dialog.destroy()

    def export_database(self):
        from datetime import datetime
        today = datetime.today()
        default_filename = f'Export {today.date()} {today.hour}-{today.minute}.zip'
        f = filedialog.asksaveasfile(parent=self.master, defaultextension='.zip', filetypes=(("Archiwum ZIP", "*.zip"),("Wszystkie pliki", "*.*")), initialfile=default_filename)
        if f is None:
            return
        
        import zipfile, os
        path = os.path.join(os.path.curdir, 'database.db')
        archive = zipfile.ZipFile(f.name, 'w')
        archive.write(path)
        archive.close()
        f.close()

    def import_database(self):
        import os, shutil
        path = os.path.join(os.path.curdir, 'database.db')
        if os.path.isfile(path):
            return messagebox.showerror(parent=self.master,title='Błąd',message='Istnieje już plik bazy danych')
        f = filedialog.askopenfilename(parent=self.master, defaultextension='.db', filetypes=(("Plik bazy danych", "*.db"),("Wszystkie pliki", "*.*")))
        if f == '':
            return
        shutil.copy(f, os.path.curdir)
        DB_Connection.open_connection()

    def delete_database(self):
        import os
        path = os.path.join(os.path.curdir, 'database.db')
        if os.path.isfile(path):
            DB_Connection.close_connection()
            os.remove(path)
            messagebox.showinfo(parent=self.master,title='Info',message='Baza danych została pomyślnie usunięta')
        else:
            messagebox.showerror(parent=self.master,title='Błąd',message='Nie znaleziono pliku bazy danych')

    def check_database(self):
        if not os.path.isfile('database.db'):
            if messagebox.askquestion(title='Pytanie', message='Brakuje pliku z bazą danych. Chcesz ją utworzyć?', parent=self.master) == 'yes':
                import DB_Setup
                r = tk.Tk()
                db_setup = DB_Setup.DB_Setup(r)
                self.master.destroy()
                db_setup.run()
            return True
        return False

    def close_window(self):
        DB_Connection.close_connection()
        self.master.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    import Login
    l = tk.Tk()
    log = Login.Login(l)
    log.run()