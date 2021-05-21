import tkinter as tk
from tkinter import ttk

class Frame(ttk.Frame):
    def __init__(self, *args, **kw):
        ttk.Frame.__init__(self, *args, **kw)
        self.tree = ttk.Treeview(self)
        self.tree.pack()

        for i in range(10):
            self.tree.insert("", tk.END, text="item %s" % i)

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        self.button = ttk.Button(self, text="test", command=self.print_selected)

        self.button.pack()
        self.selected = []

    def on_select(self, event):
        self.selected = event.widget.selection()

    def print_selected(self):
        for idx in self.selected:
            print(self.tree.item(idx)['text'])

if __name__ == "__main__":
    root = tk.Tk()
    frame = Frame(root)
    frame.pack()
    root.mainloop()