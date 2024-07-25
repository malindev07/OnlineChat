import tkinter as tk

from tkinter import ttk, NSEW, CENTER, DISABLED, EW, END, INSERT, NORMAL
from tkinter.scrolledtext import ScrolledText

from actions.create_or_connect_chat import connect_to_chat
from windows.send_message import send_message_in_chat


class ChatWindow(tk.Tk):
    
    def __init__(self, first_user_login = None, second_user_login = None, chat_id = None):
        super().__init__()
        
        self.first_user_login = first_user_login
        self.second_user_login = second_user_login
        self.chat_id = chat_id
        
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.geometry('350x500')
        
        for c in range(3): self.columnconfigure(index = c, weight = 1)
        for r in range(8): self.rowconfigure(index = r, weight = 1)
        
        chat_with_label = ttk.Label(self, text = f'Чат с {self.second_user_login}', justify = CENTER)
        chat_with_label.grid(row = 0, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.message_in_chat_text = ScrolledText(self, background = '#F5FFFA', width = 15, height = 2, state = DISABLED)
        self.message_in_chat_text.grid(row = 1, rowspan = 5, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.message_text_entry = tk.Text(width = 20, height = 3)
        self.message_text_entry.grid(row = 6, columnspan = 2, sticky = EW)
        
        send_msg_btn = ttk.Button(self, text = 'Отправить', command = self.send_message)
        send_msg_btn.grid(row = 6, column = 2, ipady = 15, sticky = EW)
        
        return_to_chats_window_btn = ttk.Button(self, text = 'Вернуться в меню')
        return_to_chats_window_btn.grid(row = 7, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4)
        
        self.show_messages()
        self.len_storage_msg = 0
    
    def send_message(self):
        message = self.message_text_entry.get(index1 = "1.0", index2 = END)
        data = {"msg_text": message, "user_login": self.first_user_login, "chat_id": self.chat_id}
        
        send_message_in_chat(data = data)
        
        self.message_in_chat_text.configure(state = NORMAL)
        self.message_in_chat_text.insert(INSERT, f'{self.first_user_login}: {message}\n')
        self.message_in_chat_text.configure(state = DISABLED)
    
    def show_messages(self):
        res = connect_to_chat(id = self.chat_id)
        
        for value in res[self.chat_id]['messages']:
            self.message_in_chat_text.configure(state = NORMAL)
            self.message_in_chat_text.insert(INSERT, f'{value['user_login']}: {value['text']}\n')
            self.message_in_chat_text.configure(state = DISABLED)
            return len(res[self.chat_id]['messages'])
    
    def check_new_messages(self):
        is_true: bool = True
        
        while is_true:
            pass
