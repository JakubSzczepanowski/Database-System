import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class DB_Setup:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame_1 = ttk.Frame(self.master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Ustawienia początkowe')
        self.label_1.pack(anchor='center', fill='y', side='top')
        self.frame_2 = ttk.Frame(self.frame_1)
        self.label_2 = ttk.Label(self.frame_2)
        self.label_2.configure(cursor='arrow', text='Nazwa(min,max)', width='15')
        self.label_2.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_1 = ttk.Entry(self.frame_2)
        self.entry_1.pack(expand='true', fill='x', side='left')
        self.entry_1_2 = ttk.Entry(self.frame_2)
        self.entry_1_2.pack(expand='true', fill='x', padx='5', pady='5', side='left')
        self.frame_2.configure(height='200', width='200')
        self.frame_2.pack(expand='true', fill='x', side='top')
        self.frame_3 = ttk.Frame(self.frame_1)
        self.label_3 = ttk.Label(self.frame_3)
        self.label_3.configure(text='Dział(min,max)', width='15')
        self.label_3.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_2 = ttk.Entry(self.frame_3)
        self.entry_2.pack(expand='true', fill='x', side='left')
        self.entry_2_2 = ttk.Entry(self.frame_3)
        self.entry_2_2.pack(expand='true', fill='x', padx='5', pady='5', side='left')
        self.frame_3.configure(height='200', width='200')
        self.frame_3.pack(expand='true', fill='x', side='top')
        self.frame_4 = ttk.Frame(self.frame_1)
        self.label_4 = ttk.Label(self.frame_4)
        self.label_4.configure(text='Cena hurtowa(min,max)', width='22')
        self.label_4.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_3 = ttk.Entry(self.frame_4)
        self.entry_3.configure(width='15')
        self.entry_3.pack(expand='true', fill='x', side='left')
        self.entry_1_2_3 = ttk.Entry(self.frame_4)
        self.entry_1_2_3.configure(width='15')
        self.entry_1_2_3.pack(expand='true', fill='x', padx='5', pady='5', side='left')
        self.frame_4.configure(height='200', width='200')
        self.frame_4.pack(expand='true', fill='x', side='top')
        self.frame_5 = ttk.Frame(self.frame_1)
        self.label_5 = ttk.Label(self.frame_5)
        self.label_5.configure(text='Ilość(min,max)', width='15')
        self.label_5.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_4 = ttk.Entry(self.frame_5)
        self.entry_4.pack(expand='true', fill='x', side='left')
        self.entry_4_5 = ttk.Entry(self.frame_5)
        self.entry_4_5.pack(expand='true', fill='x', padx='5', pady='5', side='left')
        self.frame_5.configure(height='200', width='200')
        self.frame_5.pack(expand='true', fill='x', side='top')
        self.frame_6 = ttk.Frame(self.frame_1)
        self.label_6 = ttk.Label(self.frame_6)
        self.label_6.configure(text='Cena netto(min,max)', width='20')
        self.label_6.pack(fill='x', padx='5', pady='5', side='left')
        self.entry_5 = ttk.Entry(self.frame_6)
        self.entry_5.pack(expand='true', fill='x', side='left')
        self.entry_6_7 = ttk.Entry(self.frame_6)
        self.entry_6_7.pack(expand='true', fill='x', padx='5', pady='5', side='left')
        self.frame_6.configure(height='200', width='200')
        self.frame_6.pack(expand='true', fill='x', side='top')
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='Dodaj')
        self.button_1.pack(expand='true', fill='x', ipady='10', padx='5', pady='5', side='bottom')
        self.button_1.bind('<Button>',self.get_settings)
        self.label_1_2 = ttk.Label(self.frame_1)
        self.label_1_2.configure(font='{Arial} 7 {}', text='*UWAGA! Wszystkie ustawienia dotyczą ilości cyfr lub znaków elementów wpisywanych do bazy')
        self.label_1_2.pack(side='left')
        self.frame_1.configure(height='200', padding='10', width='200')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1
        self.master.resizable(0,0)
        x = self.master.winfo_screenwidth() // 2 - 430 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 286 // 2 - 10
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Ustawienia początkowe')
        self.master.attributes("-topmost", True)

    def get_settings(self,event):
        values = [self.entry_1.get(),self.entry_1_2.get(),self.entry_2.get(),self.entry_2_2.get(),\
            self.entry_3.get(),self.entry_1_2_3.get(),self.entry_4.get(),self.entry_4_5.get(),self.entry_5.get(),\
                self.entry_6_7.get()]
        settings = self.check_entry_correctness(values)
        if settings is not None:
            import DB_Connection
            DB_Connection.open_connection()
            DB_Connection.create_settings_table(self.master,settings)
            import main
            root = tk.Tk()
            app = main.Main(root)
            self.master.destroy()
            app.run()
        
    def check_entry_correctness(self,arr):
        import Exceptions as E
        default_settings = [1,20,1,20,1,10,1,20,1,10]
        i = 0
        while i < 10:
            try:
                arr[i] = default_settings[i] if arr[i] == '' else int(arr[i])
                if arr[i] <= 0:
                    raise E.NegativeValueError
                if i%2 == 1 and arr[i-1] >= arr[i]:
                    raise E.MinGreaterThanMaxError
            except ValueError:
                messagebox.showerror(parent=self.master,title='Błąd',message='Pola przyjmują tylko liczby!')
                return None
            except (E.NegativeValueError,E.MinGreaterThanMaxError) as e:
                messagebox.showerror(parent=self.master,title='Błąd',message=e)
                return None
            i += 1
        return arr


    def run(self):
        self.mainwindow.mainloop()
