import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo


class Data_frame():
    LABEL_FONT = None
    LISTBOX_FONT = None
    BUTTON_FONT = None

    table_name = None

    listbox = None

    db_model = None

    master = None

    def __init__(self, master, db_model, table_name, note_frame):
        self._note_frame = note_frame
        self._db_model = db_model
        self._table_name = table_name
        self._master = master
        self._listbox = tk.Listbox()
        self._LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self._LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")

    def initialize(self):

        master_frame = tk.Frame(master=self._master, width=300, height=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        label = tk.Label(master=master_frame, text="Your notes", bg="#D5A8A0", width=26, height=2, font=self._LABEL_FONT)
        label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        list_box_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        list_box_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)
        self._listbox = tk.Listbox(master=list_box_frame, background="#F4DBD6", width=40, height=25, font=self._LISTBOX_FONT,
                             highlightbackground="white",
                             selectbackground="#FBEEE6", selectforeground="#E77A63", activestyle="underline", justify="left")

        self.fill_list_box()

        self._listbox.bind('<<ListboxSelect>>', self.items_selected)

        self._listbox.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)


        scrollbar_vertical = tk.Scrollbar(master=list_box_frame, orient=tk.VERTICAL, command=self._listbox.yview)
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        button_frame = tk.Frame(master=master_frame, dg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        button = tk.Button(master=button_frame, text="New note", font=self._BUTTON_FONT, background="#D5A8A0")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button = tk.Button(master=button_frame, text="Choose note", font=self._BUTTON_FONT, background="#D5A8A0")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

    def fill_list_box(self):
        var = tk.Variable(value=list(map(lambda x: x.getheader(), self._db_model.get_all_data(self._table_name))))
        self._listbox.config(listvariable=var)

    def get_note(self, note_str):
        try:
            print(tk.Listbox.index(note_str))
            return int(note_str[-2])
        except Exception as e:
            pass

    def items_selected(self, event):
        # get all selected indices
        selected_indices = self._listbox.curselection()
        # get selected items
        selected_langs = ",".join([self._listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'
        showinfo(title='Information', message=msg)

    master = property