from tkinter import N

from mttkinter import mtTkinter as tk
from tkinter import ttk
from windows.auth_reg_window import AuthWindow, RegWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # configure the root window
        
        self.title('Онлайн чат')
        self.geometry('250x200')
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        self.resizable(False, False)
        
        for c in range(2): self.columnconfigure(index = c, weight = 1)
        for r in range(2): self.rowconfigure(index = r, weight = 1)
        
        hi_label = ttk.Label(self, text = 'Добро пожаловать в Онлайн чат', anchor = N)
        reg_btn = ttk.Button(self, text = 'Регистрация', command = self.reg_open)
        auth_btn = ttk.Button(self, text = 'Авторизация', command = self.auth_open)
        
        hi_label.grid(row = 0, columnspan = 2, ipadx = 70, ipady = 6, padx = 5, pady = 5)
        reg_btn.grid(row = 1, column = 0, ipadx = 70, ipady = 6, padx = 5)
        auth_btn.grid(row = 1, column = 1, ipadx = 70, ipady = 6, padx = 5)
    
    def reg_open(self):
        # self.withdraw()
        _ = RegWindow(parent_window = self)
    
    def auth_open(self):
        # self.withdraw()
        _ = AuthWindow(parent_window = self)
