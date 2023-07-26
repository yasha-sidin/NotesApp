import tkinter as tk

from tkinter import ttk
import tkinter.font as tkFont
from tkinter.messagebox import showinfo, showerror
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter.messagebox import askyesno
import tkinter.messagebox as mbox

from Model.Note import Note



class Data_frame():
    def __init__(self, master, db_model, table_name, note_frame):
        self._note_frame = note_frame
        self._db_model = db_model
        self._table_name = table_name
        self._current_note = None
        self._master = master
        self._string_var_start_date = tk.StringVar(master)
        self._string_var_end_date = tk.StringVar(master)
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

        # Create DataFrame
        master_frame = tk.Frame(master=self._master, width=300, height=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        label = tk.Label(master=master_frame, text="Your notes", bg="#D5A8A0", width=26, height=2, relief="ridge", font=self._LABEL_FONT)
        label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        filter_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        filter_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        start_date = (datetime.now() - relativedelta(years=1)).strftime("%Y-%m-%d %H:%M:%S")
        start_date_entry = tk.Entry(master=filter_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge",
                                    justify=tk.LEFT, textvariable=self._string_var_start_date)
        start_date_entry.pack(fill=tk.X, side=tk.LEFT, padx=6, pady=6, expand=True, anchor=tk.N)
        start_date_entry.insert(0, start_date)

        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        end_date_entry = tk.Entry(master=filter_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge",
                                  justify=tk.LEFT, textvariable=self._string_var_end_date)
        end_date_entry.pack(fill=tk.X, side=tk.LEFT, padx=6, pady=6, expand=True, anchor=tk.N)
        end_date_entry.insert(0, end_date)

        list_box_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        list_box_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)
        self._listbox = tk.Listbox(master=list_box_frame, background="#F4DBD6", width=40, height=23, font=self._LISTBOX_FONT,
                             highlightbackground="white", selectbackground="#FBEEE6", selectforeground="#E77A63",
                             relief="ridge", activestyle="underline", justify="left")

        self.__fill_list_box()

        self._listbox.bind('<<ListboxSelect>>', self.confirm_select_note)

        self._listbox.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = ttk.Scrollbar(master=list_box_frame, orient=tk.VERTICAL, command=self._listbox.yview)
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        button_frame = tk.Frame(master=master_frame, bg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=20, pady=6, anchor=tk.N)

        button_new_note = tk.Button(master=button_frame, text="New note", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6", command=self.get_new_note)
        button_new_note.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button_delete = tk.Button(master=button_frame, text="Delete", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6", command=self.confirm_delete_note)
        button_delete.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

        button_filter = tk.Button(master=button_frame, text="Filter notes", font=self._BUTTON_FONT, background="#D5A8A0",
                           activebackground="#F4DBD6", command=self.__fill_list_box)
        button_filter.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=6, expand=True)

    def __check_saving(self):
        return ((self._current_note == None) or (self._note_frame.get_current_note() == None) or
                (self._current_note.getheader() == self._note_frame.get_current_header() and
                str(self._current_note.getbody()) == self._note_frame.get_current_text()))

    def __fill_list_box(self):
        if self._db_model.get_all_data(self._table_name):
            try:
                start_date = datetime.strptime(self._string_var_start_date.get(), "%Y-%m-%d %H:%M:%S")
                end_date = datetime.strptime(self._string_var_end_date.get(), "%Y-%m-%d %H:%M:%S")
                self.__to_listbox(start_date, end_date)
            except Exception as e:
                self._string_var_start_date.set((datetime.now() - relativedelta(years=1)).strftime("%Y-%m-%d %H:%M:%S"))
                self._string_var_end_date.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                start_date = datetime.strptime(self._string_var_start_date.get(), "%Y-%m-%d %H:%M:%S")
                end_date = datetime.strptime(self._string_var_end_date.get(), "%Y-%m-%d %H:%M:%S")
                self.__to_listbox(start_date, end_date)
        else:
            self._listbox.delete("0", tk.END)

    def __to_listbox(self, start_date, end_date):
        list_of_notes = self._db_model.get_all_data(self._table_name)
        filter_list = [note for note in list_of_notes if
        (start_date <= datetime.strptime(note.getdate_of_creation(), "%Y-%m-%d %H:%M:%S") <= end_date)]
        var = tk.Variable(value=list(map(lambda x: str(x.getid()) + "  " + str(x.getheader()), filter_list)))
        self._listbox.config(listvariable=var)

    def confirm_select_note(self, event):
        if (self._note_frame.check_initializing() == False and len(self._listbox.curselection()) != 0):
            self._note_frame.initialize()
            self._note_frame.set_new_button(self.save_note)

        if self.__check_saving():
            self.__choose_note()
        else:
            msg = f'If you continue without saving, you will lose all progress on the current note. Shall we continue?'
            self.confirm(msg, self.__choose_note)
    def __choose_note(self):
        try:
            selected_note = ",".join([self._listbox.get(i) for i in self._listbox.curselection()])
            id = int(selected_note.split("  ")[0])
            self._current_note = self._db_model.get_note_by_id(self._table_name, id)
            self._note_frame.set_note(self._current_note)
        except Exception as e:
            pass
    def get_new_note(self):
        if self.__check_saving():
            self.init_creating_window()
        else:
            msg = f'If you continue without saving, you will lose all progress on the current note. Shall we continue?'
            self.confirm(msg, self.init_creating_window)

    def create_note(self, top_level, header):
        if (self._note_frame.check_initializing() == False):
            self._note_frame.initialize()
            self._note_frame.set_new_button(self.save_note)

        note = Note(0, header, "")
        self._db_model.insert_into_table(self._table_name, note)
        self._current_note = self._db_model.get_note_by_id(self._table_name, self._db_model.get_last_id(self._table_name))
        self._note_frame.set_note(self._current_note)

        self._string_var_end_date.set((datetime.now() + relativedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))

        self.__fill_list_box()

        top_level.destroy()

    def save_note(self):
        if (self._current_note != None and self._note_frame.get_current_note() != None):
            if (self._note_frame.get_current_header() != ""):
                self._note_frame.get_current_note().setbody(self._note_frame.get_current_text())
                self._note_frame.get_current_note().setheader(self._note_frame.get_current_header())
                self._current_note.setbody(self._note_frame.get_current_text())
                self._current_note.setheader(self._note_frame.get_current_header())
                self._db_model.update_data(self._table_name, self._current_note)
                self.__fill_list_box()
            else:
                showerror(title='Error', message="Header's entry is empty. Please name your note or cancel changes")

    def confirm(self, msg, function):
        answer = askyesno(title='Confirmation',
                          message=msg)
        if answer:
            function()

    def init_creating_window(self):
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
        header_name_entry = tk.Entry(master=choose_frame, bg="#D5A8A0", font=self._ENTRY_FONT, relief="ridge",
                                     justify=tk.LEFT, textvariable=string_var_for_entry_header,
                                     selectbackground="#FBEEE6", selectforeground="#E77A63")

        header_name_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=2, expand=True)

        button_frame = tk.Frame(master=choose_header_and_text_window, width=100, height=300, bg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        button_create = tk.Button(master=button_frame, text="Create note", font=self._BUTTON_FONT,
                                  background="#D5A8A0", activebackground="#F4DBD6",
                                  command=lambda top_level=choose_header_and_text_window:
                                  self.create_note(top_level,
                                                   string_var_for_entry_header.get()) if string_var_for_entry_header.get() != ""
                                  else showerror(title='Error',
                                                 message="Header's entry is empty. Please name your note or cancel"))

        button_create.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=4, expand=True)

        button_cancel = tk.Button(master=button_frame, text="Cancel", font=self._BUTTON_FONT,
                                  background="#D5A8A0", activebackground="#F4DBD6",
                                  command=choose_header_and_text_window.destroy)
        button_cancel.pack(fill=tk.BOTH, side=tk.LEFT, padx=10, pady=4, expand=True)

        choose_header_and_text_window.mainloop()

    def confirm_delete_note(self):
        if (self._current_note != None):
            msg = f"Are you sure that you want to delete note with header \"{self._current_note.getheader()}\"?"
            self.confirm(msg, self.__delete_note)

    def __delete_note(self):
        self._db_model.delete_data(self._table_name, self._current_note)
        self.__fill_list_box()

        if (self._listbox.size() == 0):
            self._current_note = None
            self._note_frame.set_note(self._current_note)
            self._note_frame.disable()
        else:
            first_note = self._listbox.get(0)
            id = int(first_note.split("  ")[0])
            self._current_note = self._db_model.get_note_by_id(self._table_name, id)
            self._note_frame.set_note(self._current_note)

    note_frame = property
    db_model = property
    table_name = property
    current_note = property
    master = property
    string_var_start_date = property
    string_var_end_date = property
    listbox = property
    LABEL_FONT = property
    LISTBOX_FONT = property
    ENTRY_FONT = property
    BUTTON_FONT = property
