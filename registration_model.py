# import tkinter as tk
# from tkinter import ttk
#
#
# # window_reg = tk.Tk()
# # window_reg.title("Онлайн чат")
# # window_reg.geometry("250x200+1150+500")
# # window_reg.resizable(False, False)
# #
# # reg_label_frame = ttk.LabelFrame(text = 'Регистрация', width = 200)
# #
# # ttk.Label(reg_label_frame, text = 'Логин').grid(row = 0, column = 0)
# # ttk.Label(reg_label_frame, text = 'Пароль').grid(row = 1, column = 0)
# #
# # ttk.Entry(reg_label_frame).grid(row = 0, column = 1, padx = 5, pady = 5)
# # ttk.Entry(reg_label_frame).grid(row = 1, column = 1, padx = 5, pady = 5)
# # reg_label_frame.pack(padx = 5, pady = 15, ipadx = 5, ipady = 5)
# #
# # btn_reg = ttk.Button(text = 'Создать аккаунт', width = 30)
# #
# # btn_reg.pack(padx = 5, pady = 15, ipadx = 5, ipady = 5)
# #
# # window_reg.mainloop()
#
#
# class RegWindow(tk):
#     def __init__(self):
#         # configure the root window
#         self.title('Онлайн чат')
#         self.geometry('250x200+1150+500')
#         self.resizable(False, False)
#
#         # label
#         self.label = ttk.Label(self, text = f'Добро пожаловать в Онлайн чат', padding = [5, 5],
#                                font = ("Arial", 11),
#                                wraplength = 180, justify = CENTER)
#         self.label.pack(padx = 5, pady = 15)
#
#         # grid buttons
#         self.frame = ttk.Frame(width = 200)
#
#         self.auth_btn = ttk.Button(self.frame, text = 'Авторизация', padding = [5, 5], command = self.auth_click())
#         self.reg_btn = ttk.Button(self.frame, text = 'Регистрация', padding = [5, 5], command = self.reg_click)
#
#         self.reg_btn.grid(row = 0, column = 0, padx = 5)
#         self.auth_btn.grid(row = 0, column = 1, padx = 5)
#
#         self.frame.pack()
