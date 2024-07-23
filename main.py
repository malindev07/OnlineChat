import tkinter as tk

from tkinter import ttk, X, NSEW, N, W
from tkinter.constants import NW, S
from tkinter.messagebox import showinfo

from authorization_model import reg_rest, auth_rest


class ChatsWindow(tk.Tk):
    
    def __init__(self, login = None, chats_id = None):
        super().__init__()
        
        if chats_id is None:
            chats_id = []
        
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.geometry('300x200')
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        login_label = ttk.Label(self, text = f'Вы вошли как {login}', font = ("Arial", 16, 'bold'))
        login_label.grid(row = 0, sticky = NW, pady = 10, columnspan = 4)
        
        chats_label = ttk.Label(self, text = 'Ваши чаты', justify = 'center', font = ("Arial", 14))
        chats_label.grid(row = 1, column = 2, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = N)
        
        go_in_chat_btn = ttk.Button(self, text = 'Войти в чат')
        go_in_chat_btn.grid(row = 2, column = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                            sticky = NSEW)
        
        combobox = ttk.Combobox(values = chats_id, font = ("Arial", 12), width = 13)
        combobox.grid(row = 2, column = 2, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        create_new_chat_btn = ttk.Button(self, text = 'Создать новый чат')
        create_new_chat_btn.grid(row = 1, column = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                 sticky = NSEW)
    
    def open(self):
        self.mainloop()


class AuthWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        reg_label = ttk.Label(self, text = 'Авторизация', justify = 'center')
        # Поля ввода логина и пароля
        self.entry_login = ttk.Entry(self)
        self.entry_pass = ttk.Entry(self)
        btn = ttk.Button(self, text = 'Войти', command = self.auth_in_sys)
        
        reg_label.grid(row = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        ttk.Label(self, text = 'Логин').grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                             sticky = NSEW)
        ttk.Label(self, text = 'Пароль').grid(row = 2, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                              sticky = NSEW)
        self.entry_login.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.entry_pass.grid(row = 2, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        btn.grid(row = 3, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
    
    def open(self):
        self.mainloop()
    
    def open_chats(self):
        self.destroy()
        chats_window = ChatsWindow()
        chats_window.open()
    
    def auth_in_sys(self):
        login = self.entry_login.get()
        password = self.entry_pass.get()
        data = {'login': login, 'password': password}
        res = auth_rest(data)
        
        if res != 404:
            self.info_is_auth(data['login'])
            self.destroy()
            
            chats_window = ChatsWindow(login = data['login'], chats_id = res['chats_id'])
            chats_window.open()
        else:
            showinfo(title = 'Авторизация', message = f'Неверный логин или пароль')
    
    def info_is_auth(self, data_login):
        showinfo(title = 'Авторизация', message = f'Добро пожаловать, {data_login}!')


class RegWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        reg_label = ttk.Label(self, text = 'Регистрация', justify = 'center')
        # Поля ввода логина и пароля
        self.entry_login = ttk.Entry(self)
        self.entry_pass = ttk.Entry(self)
        btn = ttk.Button(self, text = 'Создать аккаунт', command = self.reg_in_sys)
        
        reg_label.grid(row = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        ttk.Label(self, text = 'Логин').grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                             sticky = NSEW)
        ttk.Label(self, text = 'Пароль').grid(row = 2, column = 0, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                              sticky = NSEW)
        self.entry_login.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        self.entry_pass.grid(row = 2, column = 1, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        btn.grid(row = 3, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
    
    def open(self):
        self.mainloop()
    
    def reg_in_sys(self):
        login = self.entry_login.get()
        password = self.entry_pass.get()
        data = {'login': login, 'password': password}
        
        if reg_rest(data) != 404:
            self.button_clicked(data['login'])
            self.destroy()
            chats_window = ChatsWindow(login = data['login'])
            chats_window.open()
        else:
            showinfo(title = 'Регистрация', message = f'Пользователь с логином {login} уже зарегестрирован!')
            self.destroy()
            auth_window = AuthWindow()
            auth_window.open()
    
    def button_clicked(self, data_login):
        showinfo(title = 'Регистрация', message = f'Добро пожаловать, {data_login}!')


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
        self.destroy()
        reg_window = RegWindow()
        reg_window.open()
    
    def auth_open(self):
        self.destroy()
        auth_window = AuthWindow()
        auth_window.open()


if __name__ == "__main__":
    app = App()
    app.mainloop()
