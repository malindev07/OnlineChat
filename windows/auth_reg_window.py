from mttkinter import mtTkinter as tk

from tkinter import ttk, NSEW

from tkinter.messagebox import showinfo

from actions.actions_on_user import auth_rest, reg_rest
from windows.all_chats_window import ChatsWindow


class AuthWindow(tk.Tk):
    def __init__(self, parent_window = None):
        super().__init__()
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        self.parent_window = parent_window
        self.parent_window.withdraw()
        
        self.reg_label = ttk.Label(self, text = 'Авторизация', justify = 'center')
        # Поля ввода логина и пароля
        self.entry_login = ttk.Entry(self)
        self.entry_pass = ttk.Entry(self)
        self.btn = ttk.Button(self, text = 'Войти', command = self.auth_in_sys)
        
        self.reg_label.grid(row = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        ttk.Label(self, text = 'Логин').grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                             sticky = NSEW)
        ttk.Label(self, text = 'Пароль').grid(row = 2, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                              sticky = NSEW)
        self.entry_login.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.entry_pass.grid(row = 2, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.btn.grid(row = 3, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.reg_window = ttk.Button(self, text = 'Регистрация', command = self.open_reg_window)
        self.reg_window.grid(row = 4, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
    
    def open_reg_window(self):
        self.destroy()
        _ = RegWindow(parent_window = self.parent_window)
    
    def open_chats(self):
        self.destroy()
        _ = ChatsWindow(parent_window = self.parent_window)
    
    def auth_in_sys(self):
        login = self.entry_login.get()
        password = self.entry_pass.get()
        data = {'login': login, 'password': password}
        res = auth_rest(data)
        
        if res != 404:
            self.info_is_auth(data['login'])
            _ = ChatsWindow(data = res, parent_window = self.parent_window, log_pas = data)
            self.destroy()
        
        else:
            showinfo(title = 'Авторизация', message = f'Неверный логин или пароль')
    
    def info_is_auth(self, data_login):
        showinfo(title = 'Авторизация', message = f'Добро пожаловать, {data_login}!')


class RegWindow(tk.Tk):
    def __init__(self, parent_window = None):
        super().__init__()
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        self.parent_window = parent_window
        self.parent_window.withdraw()
        
        self.reg_label = ttk.Label(self, text = 'Регистрация', justify = 'center')
        # Поля ввода логина и пароля
        self.entry_login = ttk.Entry(self)
        self.entry_pass = ttk.Entry(self)
        self.btn = ttk.Button(self, text = 'Создать аккаунт', command = self.reg_in_sys)
        
        self.reg_label.grid(row = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        ttk.Label(self, text = 'Логин').grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                             sticky = NSEW)
        ttk.Label(self, text = 'Пароль').grid(row = 2, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                              sticky = NSEW)
        self.entry_login.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.entry_pass.grid(row = 2, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.btn.grid(row = 3, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
    
    def reg_in_sys(self):
        login = self.entry_login.get()
        password = self.entry_pass.get()
        data = {'login': login, 'password': password}
        
        res = reg_rest(data)
        if res == 404:
            showinfo(title = 'Регистрация', message = f'Пользователь с логином {login} уже зарегестрирован!')
            
            _ = AuthWindow(parent_window = self.parent_window)
            self.destroy()
            # auth_window.open()
        
        elif res == 400:
            showinfo(title = 'Регистрация', message = f'Недопустимый логин')
        
        else:
            self.button_clicked(data['login'])
            _ = ChatsWindow(data = res, parent_window = self.parent_window, log_pas = data)
            self.destroy()
    
    def button_clicked(self, data_login):
        showinfo(title = 'Регистрация', message = f'Добро пожаловать, {data_login}!')
