import tkinter as tk

from tkinter import ttk
import tkinter.font as tkFont
from tkinter.messagebox import showinfo, showerror
from datetime import datetime
from dateutil.relativedelta import relativedelta

from Model.Note import Note


class Data_frame():
    LABEL_FONT = None
    LISTBOX_FONT = None
    BUTTON_FONT = None

    table_name = None

    listbox = None

    db_model = None

    master = None

    current_note = None

    def __init__(self, master, db_model, table_name, note_frame):
        self._note_frame = note_frame
        self._db_model = db_model
        self._table_name = table_name
        self._current_note = None
        self._master = master
        self._listbox = tk.Listbox()
        self._LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self._LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._ENTRY_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")

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

        master_frame = tk.Frame(master=self._master, width=300, height=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        label = tk.Label(master=master_frame, text="Your notes", bg="#D5A8A0", width=26, height=2, relief="ridge", font=self._LABEL_FONT)
        label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        filter_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        filter_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        start_date = (datetime.now() - relativedelta(years=1)).strftime("%Y-%m-%d %H:%M:%S")
        start_date_entry = tk.Entry(master=filter_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge", justify=tk.LEFT)
        start_date_entry.pack(fill=tk.X, side=tk.LEFT, padx=6, pady=6, expand=True, anchor=tk.N)
        start_date_entry.insert(0, start_date)

        end_date_entry = tk.Entry(master=filter_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge", justify=tk.LEFT)
        end_date_entry.pack(fill=tk.X, side=tk.LEFT, padx=6, pady=6, expand=True, anchor=tk.N)

        list_box_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        list_box_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)
        self._listbox = tk.Listbox(master=list_box_frame, background="#F4DBD6", width=40, height=23, font=self._LISTBOX_FONT,
                             highlightbackground="white", selectbackground="#FBEEE6", selectforeground="#E77A63",
                             relief="ridge", activestyle="underline", justify="left")

        self.fill_list_box()

        # self._listbox.bind('<<ListboxSelect>>', self.items_selected)

        self._listbox.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = ttk.Scrollbar(master=list_box_frame, orient=tk.VERTICAL, command=self._listbox.yview)
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        button_frame = tk.Frame(master=master_frame, bg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=20, pady=6, anchor=tk.N)

        button = tk.Button(master=button_frame, text="New note", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6", command=self.get_new_note)
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button = tk.Button(master=button_frame, text="Delete", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button = tk.Button(master=button_frame, text="Filter notes", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6")
        button.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        self._note_frame.initialize()

    def fill_list_box(self):
        if self._db_model.get_all_data(self._table_name):
            var = tk.Variable(value=list(map(lambda x: x.getheader(), self._db_model.get_all_data(self._table_name))))
            self._listbox.config(listvariable=var)

    def get_note(self, note_str):
        try:
            print(tk.Listbox.index(note_str))
            return int(note_str[-2])
        except Exception as e:
            pass

    def select_note(self, event):
        # get all selected indices
        selected_indices = self._listbox.curselection()
        # get selected items
        selected_langs = ",".join([self._listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'
        showinfo(title='Information', message=msg)

    def __check_saving(self):
        # return ((self._current_note == None) or (self._note_frame.get_current_note() == None) or
        #         (self._current_note.getheader() == self._note_frame.get_current_note().getheader() and
        #         self._current_note.getbody() == self._note_frame.get_current_note().getbody()))

        return ((self._current_note == None) or (self._note_frame.get_current_note() == None) or
                (self._current_note.getheader() == self._note_frame.get_current_header() and
                str(self._current_note.getbody()) == self._note_frame.get_current_text()))

    def get_new_note(self):
        if self.__check_saving():
            choose_header_and_text_window = tk.Toplevel(self._master, background="#EBC8C1")
            choose_header_and_text_window.grab_set()
            choose_header_and_text_window.title("Names your new note")
            choose_header_and_text_window.minsize(width=300, height=200)
            choose_header_and_text_window.maxsize(width=300, height=200)

            choose_frame = tk.Frame(master=choose_header_and_text_window, width=100, height=300, bg="#EBC8C1")
            choose_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

            header_name_label = tk.Label(master=choose_frame, text="Header of note:", bg="#D5A8A0", width=26, height=2,
                                         relief="ridge", font=self._LABEL_FONT, justify=tk.LEFT)
            header_name_label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

            string_var_for_entry_header = tk.StringVar(choose_header_and_text_window)
            header_name_entry = tk.Entry(master=choose_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge", justify=tk.LEFT,
                                         textvariable=string_var_for_entry_header)

            header_name_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=2, expand=True)

            button_frame = tk.Frame(master=choose_header_and_text_window, width=100, height=300, bg="#EBC8C1")
            button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

            button_create = tk.Button(master=button_frame, text="Create note", font=self._BUTTON_FONT,
                                      background="#D5A8A0", activebackground="#F4DBD6",
                                      command= lambda top_level=choose_header_and_text_window:
                                      self.create_note(top_level, string_var_for_entry_header.get()) if string_var_for_entry_header.get() != ""
                                      else showerror(title='Error', message="Header's entry is empty. Please name your note or cancel"))

            button_create.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=4, expand=True)

            button_cancel = tk.Button(master=button_frame, text="Cancel", font=self._BUTTON_FONT,
                                      background="#D5A8A0", activebackground="#F4DBD6", command=choose_header_and_text_window.destroy)
            button_cancel.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=4, expand=True)

            choose_header_and_text_window.mainloop()



        else:
            msg = f'If you continue without saving, you will lose all progress on the current note. Shall we continue?'
            showinfo(title='Information', message=msg)

    def create_note(self, top_level, header):
        note = Note(0, header, "")
        self._current_note = note
        self._note_frame.set_note(self._current_note)
        self._db_model.insert_into_table(self._table_name, self._current_note)
        self.fill_list_box()
        top_level.destroy()

