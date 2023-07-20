import tkinter as tk
import tkinter.font as tkFont

# window = tk.Tk()

# label = tk.Label(
#     text="Привет, Tkinter!",
#     foreground="white",  # Устанавливает белый текст
#     background="black",  # Устанавливает черный фон
#     width = 100,
#     height = 40
# )
#
# button = tk.Button(
#     text="Нажми на меня!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
# label.pack()
# window.mainloop()

# text_box = tk.Text()
# text_box.pack()
#
# window.mainloop()



window = tk.Tk()

LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
LISTBOX_FONT = tkFont.Font(family="Times New Roman", size=14, slant="italic")
BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")

master_frame = tk.Frame(master=window, width=300, height=600, bg="#EBC8C1")
master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label = tk.Label(master=master_frame, text="Your notes", bg="#D5A8A0", width=26, height=2, font=LABEL_FONT)
label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

list_box_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
list_box_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)
listbox = tk.Listbox(master=list_box_frame, background="#F4DBD6", height=25, font=LISTBOX_FONT,
                     highlightbackground="white",
                     selectbackground="#FBEEE6", selectforeground="#E77A63")
listbox.insert(tk.END, *(f"Element {i}" for i in range(100)))

listbox.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

scrollbar_vertical = tk.Scrollbar(master=list_box_frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

# horizontal_vertical = tk.Scrollbar(master=list_box_frame, orient=tk.HORIZONTAL, command=listbox.xview)
# horizontal_vertical.pack(fill=tk.BOTH, side=tk.BOTTOM)

button = tk.Button(master=master_frame, text="Choose note", font=BUTTON_FONT, background="#D5A8A0")
button.pack(fill=tk.BOTH, side=tk.TOP, padx=130, pady=6, expand=True)

frame3 = tk.Frame(master=window, height=600, width=600, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()