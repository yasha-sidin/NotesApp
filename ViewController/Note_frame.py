import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from Model.Note import Note

class Note_frame():
    def __init__(self, master, db_model, table_name):
        self._master_frame = tk.Frame()
        self._is_initialize = False
        self._current_note = None
        self._button_frame = tk.Frame()
        self._master = master
        self._textfield = tk.Text()
        self._header_entry = tk.Entry()
        self._string_var_header = tk.StringVar(master)
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

        self._master_frame = tk.Frame(master=self._master, height=600, width=600, bg="#EBC8C1")
        self._master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        text_frame = tk.Frame(master=self._master_frame, bg="#EBC8C1")
        text_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        self._header_entry = tk.Entry(master=text_frame, bg="#D5A8A0", font=self._HEADER_FONT, relief="ridge", justify=tk.CENTER,
                                      textvariable=self._string_var_header, selectbackground="#FBEEE6", selectforeground="#E77A63")
        self._header_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=6, expand=True, anchor=tk.N)

        text_field_frame = tk.Frame(master=text_frame, bg="#D5A8A0")
        text_field_frame.pack(fill=tk.BOTH, side=tk.TOP, padx=6, pady=6, expand=True)

        self._textfield = tk.Text(master=text_field_frame, relief="ridge", bg="#D5A8A0", background="#F4DBD6", height=26,
                             highlightbackground="white", selectbackground="#FBEEE6", selectforeground="#E77A63",
                             padx=15, pady=15, font=self._LISTBOX_FONT, width=65, undo=True)
        self._textfield.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = ttk.Scrollbar(master=text_field_frame, orient=tk.VERTICAL, command=self._textfield.yview, cursor="arrow")
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        self._button_frame = tk.Frame(master=self._master_frame, bg="#EBC8C1")
        self._button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=140, pady=6, anchor=tk.N)

        # button_save = tk.Button(master=self._button_frame, text="Save", font=self._BUTTON_FONT, background="#D5A8A0",
        #                    activebackground="#F4DBD6")
        # button_save.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button_clear = tk.Button(master=self._button_frame, text="Clear", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6", command=self.clear_text)
        button_clear.pack(fill=tk.BOTH, side=tk.RIGHT, padx=10, pady=6, expand=True)

        self._is_initialize = True

    def get_current_note(self):
        return self._current_note

    def set_note(self, note):
        if note == None:
            self._current_note = None
        else:
            self._current_note = note

            self._header_entry.delete(0, tk.END)
            self._header_entry.insert(0, self._current_note.getheader())

            self._textfield.delete("1.0", tk.END)
            self._textfield.insert(tk.END, self._current_note.getbody())

    def get_current_text(self):
        return self._textfield.get("1.0", "end-1c")

    def get_current_header(self):
        return self._string_var_header.get()

    def set_new_button(self, function):
        button = tk.Button(master=self._button_frame, text="Save", font=self._BUTTON_FONT, background="#D5A8A0",
                            activebackground="#F4DBD6", command=function)
        button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=10, pady=6, expand=True)

    def get_button_frame(self):
        return self._button_frame

    def check_initializing(self):
        return self._is_initialize

    def clear_text(self):
        self._textfield.delete("1.0", tk.END)

    def disable(self):
        self._is_initialize = False
        self._master_frame.destroy()

    master_frame = property
    is_initialize = property
    current_note = property
    button_frame = property
    master = property
    textfield = property
    header_entry = property
    string_var_header = property
    LABEL_FONT = property
    LISTBOX_FONT = property
    BUTTON_FONT = property
    HEADER_FONT = property
