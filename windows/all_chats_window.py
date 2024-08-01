from mttkinter import mtTkinter as tk

from tkinter import ttk, NSEW, N
from tkinter.constants import NW, CENTER
from tkinter.messagebox import showinfo

from actions.actions_on_user import auth_rest
from actions.create_or_connect_chat import create_chat, connect_to_chat

from windows.chat_window import ChatWindow


class ChatsWindow(tk.Tk):
    parent_window = None
    
    def __init__(self, data = None, parent_window = None, log_pas = None):
        super().__init__()
        self.data = data
        
        self.log_pas = log_pas
        self.parent_window = parent_window
        
        if self.data is not None:
            self.login = data['login']
            self.chats_id = data['chats_id']
        
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.geometry('300x200')
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        self.login_label = ttk.Label(self, text = f'Вы вошли как {self.login}', font = ("Arial", 16, 'bold'))
        self.login_label.grid(row = 0, sticky = NW, pady = 10, columnspan = 4)
        
        self.chats_label = ttk.Label(self, text = 'Ваши чаты', justify = 'center', font = ("Arial", 14))
        self.chats_label.grid(row = 1, column = 2, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = N)
        
        self.go_in_chat_btn = ttk.Button(self, text = 'Войти в чат', command = self.open_chat)
        self.go_in_chat_btn.grid(row = 2, column = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                 sticky = NSEW)
        
        self.combobox = ttk.Combobox(self, values = self.chats_id, font = ("Arial", 12), width = 13)
        self.combobox.grid(row = 2, column = 2, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.create_new_chat_btn = ttk.Button(self, text = 'Создать новый чат',
                                              command = self.create_new_chat)
        self.create_new_chat_btn.grid(row = 1, column = 0, columnspan = 2, ipadx = 6, ipady = 6, padx = 4, pady = 4,
                                      sticky = NSEW)
        
        self.exit_btn = ttk.Button(self, text = 'Выйти', command = self.return_to_reg_auth_window)
        self.exit_btn.grid(row = 3, columnspan = 4, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
    
    def open_chat(self):
        chat_id = self.combobox.get()
        second_user_login = ''
        
        res = connect_to_chat(chat_id)
        
        for item in res[chat_id]['users']:
            for login in item:
                if login == self.data['login']:
                    
                    continue
                else:
                    second_user_login = login
        
        self.withdraw()
        
        _ = ChatWindow(first_user_login = self.data['login'], second_user_login = second_user_login, chat_id = chat_id,
                       parent_window = self)
    
    def create_new_chat(self):
        _ = CreateChat(data = self.data, parent_window = self)
        self.withdraw()
    
    def return_to_reg_auth_window(self):
        
        self.parent_window.deiconify()
        self.destroy()
    
    def refresh_combobox(self):
        print(self.log_pas)
        res = auth_rest(self.log_pas)
        print(res)
        self.chats_id = res['chats_id']
        self.combobox.configure(values = self.chats_id)


class CreateChat(tk.Tk):
    
    def __init__(self, data = None, parent_window = None):
        super().__init__()
        
        self.data = data
        self.parent_window = parent_window
        self.parent_window.withdraw()
        
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.geometry('200x200')
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        for c in range(3): self.columnconfigure(index = c, weight = 1)
        for r in range(5): self.rowconfigure(index = r, weight = 1)
        
        self.search_login_lbl = ttk.Label(self, text = 'Введите логин пользователя', justify = CENTER)
        self.search_login_entry = ttk.Entry(self)
        self.create_chat_btn = ttk.Button(self, text = 'Создать чат', command = self.open_created_chat)
        
        self.search_login_lbl.grid(row = 0, columnspan = 3)
        self.search_login_entry.grid(row = 1, columnspan = 3, ipadx = 6, padx = 5,
                                     sticky = NSEW)
        self.create_chat_btn.grid(row = 2, columnspan = 3, ipadx = 6, ipady = 6, padx = 5, pady = 4,
                                  sticky = NSEW)
    
    def open_created_chat(self):
        second_user_login = self.search_login_entry.get()
        first_suer = {'login': self.data['login']}
        second_user = {'login': second_user_login}
        self.parent_window.withdraw()
        
        res = create_chat([first_suer, second_user])
        
        if first_suer == second_user:
            showinfo(title = 'Чат', message = f'Нельзя создать чат с самим собой')
        
        elif res is None:
            showinfo(title = 'Чат', message = f'Пользовтаель не найден')
        
        elif isinstance(res, int):
            self.destroy()
            showinfo(title = 'Чат', message = f'Чат уже создан id чата {res}')
            _ = ChatWindow(first_user_login = self.data['login'], second_user_login = second_user_login,
                           chat_id = res, parent_window = self.parent_window)
        
        else:
            self.destroy()
            _ = ChatWindow(first_user_login = self.data['login'], second_user_login = second_user_login,
                           chat_id = res['id'], parent_window = self.parent_window)

# app = CreateChat()
# app.mainloop()
