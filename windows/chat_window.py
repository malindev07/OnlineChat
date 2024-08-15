from mttkinter import mtTkinter as tk

from tkinter import ttk, NSEW, CENTER, DISABLED, EW, END, NORMAL
from tkinter.scrolledtext import ScrolledText

from actions.actions_on_user import auth_rest
from update_mag.update_msg_storage import start_threading, return_chat_msg_storage

from actions.send_message import send_message_in_chat


class ChatWindow(tk.Tk):
    
    def __init__(self, user = None, first_user_login = None, second_user_login = None, chat_id = None, parent_window = None):
        super().__init__()
        
        self.first_user_login = first_user_login
        self.second_user_login = second_user_login
        self.chat_id = chat_id
        self.user = user
        print(self.second_user_login)
        
        self.title('Онлайн чат')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.geometry('350x500')
        self.parent_window = parent_window
        
        for c in range(3): self.columnconfigure(index = c, weight = 1)
        for r in range(8): self.rowconfigure(index = r, weight = 1)
        
        self.chat_with_label = ttk.Label(self, text = f'Чат с {self.second_user_login}, чат id {self.chat_id}', justify = CENTER)
        self.chat_with_label.grid(row = 0, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.message_in_chat_text = ScrolledText(self, background = '#F5FFFA', width = 15, height = 2, state = DISABLED)
        self.message_in_chat_text.grid(row = 1, rowspan = 5, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4, sticky = NSEW)
        
        self.message_text_entry = tk.Text(self, width = 20, height = 3)
        self.message_text_entry.grid(row = 6, columnspan = 2, sticky = EW)
        
        self.send_msg_btn = ttk.Button(self, text = 'Отправить', command = self.send_message)
        self.send_msg_btn.grid(row = 6, column = 2, ipady = 15, sticky = EW)
        
        self.return_to_chats_window_btn = ttk.Button(self, text = 'Вернуться в меню', command = self.return_to_main)
        self.return_to_chats_window_btn.grid(row = 7, columnspan = 3, ipadx = 6, ipady = 6, padx = 4, pady = 4)
        
        self.show_messages()
        
        self.thread_manger = start_threading(chat_id = self.chat_id, update_func = self.check_new_messages)
        self.thread_manger.set_start()
        
        self.message_in_chat_text.yview_moveto('1')
    
    def send_message(self):
        message = self.message_text_entry.get(index1 = "1.0", index2 = END)
        
        data = {
            "chat_id": self.chat_id,
            "user_id": self.user["id"],
            "text": message
        }
        send_message_in_chat(data = data)
    
    def show_messages(self):
        res = return_chat_msg_storage(chat_id = self.chat_id)
        i = 0
        print(res)
        for msg in res:
            for k in msg:
                self.message_in_chat_text.configure(state = NORMAL)
                self.message_in_chat_text.insert(END, f'\n{k}: {msg[k]}')
                self.message_in_chat_text.configure(state = DISABLED)
                self.message_in_chat_text.yview_moveto('1')
    
    def check_new_messages(self):
        
        for k in self.thread_manger.last_msg:
            self.message_in_chat_text.configure(state = NORMAL)
            self.message_in_chat_text.insert(END, f'\n{k} : {self.thread_manger.last_msg[k]}')
            self.message_in_chat_text.configure(state = DISABLED)
            self.message_in_chat_text.yview_moveto('1')
    
    def return_to_main(self):
        self.destroy()
        self.parent_window.deiconify()
        self.parent_window.refresh_combobox()
