import tkinter as tk
import tkinter.font as tkFont

class Note_frame():
    LABEL_FONT = None
    LISTBOX_FONT = None
    BUTTON_FONT = None

    note = None

    data_frame = None
    def __init__(self, master, db_model, data_frame, table_name):
        self._note = None
        self._data_frame = data_frame
        self._master = master
        self._LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self._LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")

    def initialize(self):
        master_frame = tk.Frame(master=self._master, height=600, width=600, bg="#D5A8A0")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        text_frame = tk.Text(master=master_frame, bg="#D5A8A0")
        text_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        header_entry = tk.Entry(master=text_frame, bg="#D5A8A0")
        header_entry.pack(fill=tk.BOTH, side=tk.TOP, padx=6, pady=6, expand=True)

        text_field_frame = tk.Frame(master=text_frame, bg="#D5A8A0")
        text_field_frame.pack(fill=tk.BOTH, side=tk.TOP, padx=6, pady=6, expand=True)

        text_field = tk.Text(master=text_field_frame, bg="#D5A8A0")
        text_field.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = tk.Scrollbar(master=text_field_frame, orient=tk.VERTICAL, command=text_frame.yview)
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)
