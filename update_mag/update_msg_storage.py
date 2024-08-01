import time
from threading import Thread

import requests


def return_chat_msg_storage(chat_id: str) -> list:
    response_get = requests.get(f'http://127.0.0.1:8000//chats/show_chat_msg_storage', params = {'chat_id': chat_id})
    
    data = response_get.json()
    
    return data


class IntervalCheckMsgThread(Thread):
    sleep: int | float
    chat_id: str
    len_msg_storage: int
    last_msg: dict = {}
    _is_run: bool = False
    
    def __init__(self, sleep: int | float = 0, chat_id: str = '', update_msg = None):
        Thread.__init__(self)
        self.daemon = True
        self.sleep = sleep
        self.chat_id = chat_id
        self.len_msg_storage = len(return_chat_msg_storage(self.chat_id))
        self.update_msg_func = update_msg
    
    def run(self):
        while True:
            if self.is_run():
                
                msg_storage = return_chat_msg_storage(self.chat_id)
                current_len_msg_storage = len(msg_storage)
                
                if current_len_msg_storage > self.len_msg_storage:
                    self.len_msg_storage = current_len_msg_storage
                    self.last_msg = msg_storage[-1]
                    
                    self.start_write_msg(self.update_msg_func)
            
            time.sleep(self.sleep)
    
    def is_run(self) -> bool:
        return self._is_run
    
    def set_stop(self):
        self._is_run = False
    
    def set_start(self):
        self._is_run = True
    
    def start_write_msg(self, func = None):
        func()
    
    # def start_main_window(self):
    #     app = App()
    #     app.mainloop()


def start_threading(chat_id: str, time_sleep: int = 0.5, update_func = None):
    return_thread_manager = IntervalCheckMsgThread(chat_id = chat_id, sleep = time_sleep, update_msg = update_func)
    return_thread_manager.start()
    return return_thread_manager
