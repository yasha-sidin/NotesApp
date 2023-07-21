import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Note_frame():
    LABEL_FONT = None
    LISTBOX_FONT = None
    BUTTON_FONT = None
    HEADER_FONT = None

    note = None

    def __init__(self, master, db_model, table_name):
        self._note = None
        self._master = master
        self._LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self._LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")
        self._HEADER_FONT = tkFont.Font(family="Arial", size=30, weight="bold", slant="italic")

    def initialize(self):
        style = ttk.Style()
        style.theme_use('alt')

        style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#EBC8C1",
            darkcolor="#EBC8C1",
            lightcolor="#EBC8C1",
            troughcolor="#EBC8C1",
            bordercolor="#EBC8C1",
            arrowcolor="#B27355"
        )

        master_frame = tk.Frame(master=self._master, height=600, width=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        text_frame = tk.Frame(master=master_frame, bg="#EBC8C1")
        text_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        header_entry = tk.Entry(master=text_frame, bg="#D5A8A0", font=self._HEADER_FONT, relief="ridge", justify=tk.CENTER)
        header_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=6, expand=True, anchor=tk.N)

        text_field_frame = tk.Frame(master=text_frame, bg="#D5A8A0")
        text_field_frame.pack(fill=tk.BOTH, side=tk.TOP, padx=6, pady=6, expand=True)

        text_field = tk.Text(master=text_field_frame, relief="ridge", bg="#D5A8A0", background="#F4DBD6", height=26,
                             highlightbackground="white", selectbackground="#FBEEE6", selectforeground="#E77A63",
                             padx=15, pady=15, font=self._LISTBOX_FONT, width=65)
        text_field.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = ttk.Scrollbar(master=text_field_frame, orient=tk.VERTICAL, command=text_field.yview, cursor="arrow")
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        button_frame = tk.Frame(master=master_frame, bg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=140, pady=6, anchor=tk.N)

        button = tk.Button(master=button_frame, text="Save", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button = tk.Button(master=button_frame, text="Clear", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

