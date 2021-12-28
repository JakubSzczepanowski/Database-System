import tkinter as tk
import tkinter.ttk as ttk


class PredictSupply:
    def __init__(self, master=None):
        self.master = master
        self.frame_1 = ttk.Frame(master)
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(font='{Arial} 24 {}', text='Przewidywane dostawy')
        self.label_1.pack(side='top')
        self.label_2 = ttk.Label(self.frame_1)
        self.label_2.configure(font='{Arial} 12 {}')
        self.label_2.pack(side='top')
        self.frame_1.configure(height='200', width='200')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1
        x = self.master.winfo_screenwidth() // 2 - 278 // 2 - 10
        y = self.master.winfo_screenheight() // 2 - 231 // 2 - 10
        self.master.resizable(0,0)
        self.master.geometry(f'+{x}+{y}')
        self.master.title('Przewidywanie dostaw')


    def run(self):
        self.mainwindow.mainloop()