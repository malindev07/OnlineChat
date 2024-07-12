from tkinter import *

root = Tk()
root.title("Online Chat")
root.geometry("350x350")

hello_label = Label(text = 'Добро пожаловать в приложение "Онлайн чат"')
hello_label.pack(side =TOP ,pady=60)

auth_btn = Button(text = "Регистрация")  # создаем кнопку из пакета tkinter
auth_btn.pack(side = LEFT, ipadx = 15, ipady = 15)  # размещаем кнопку в окне

reg_btn = Button(text = "Регистрация")
reg_btn.pack(side = RIGHT, ipadx = 15, ipady = 15)

root.mainloop()

# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# for c in range(2): root.columnconfigure(index = c, weight = 1)
# for r in range(2): root.rowconfigure(index = r, weight = 1)
#
# btn1 = ttk.Button(text = "button 1")
# # columnspan=2 - растягиваем на два столбца
# btn1.grid(row = 0, column = 0, columnspan = 2, ipadx = 70, ipady = 6, padx = 5, pady = 5)
#
# btn3 = ttk.Button(text = "button 3")
# btn3.grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)
#
# btn4 = ttk.Button(text = "button 4")
# btn4.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)
#
# root.mainloop()