import tkinter as tk
import tkinter.font as tkFont
class Data_frame():
    LABEL_FONT = None
    LISTBOX_FONT = None
    BUTTON_FONT = None

    list_of_notes = []

    master = None

    def __init__(self, master, db_model, table_name):
        self._list_of_notes = db_model.get_all_data(table_name)
        self._master = master
        self._LABEL_FONT = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        self._LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        self._BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")
    def get_list_of_notes(self):
        return self._list_of_notes

    def initialize(self):

        master_frame = tk.Frame(master=self._master, width=300, height=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        label = tk.Label(master=master_frame, text="Your notes", bg="#D5A8A0", width=26, height=2, font=self._LABEL_FONT)
        label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        list_box_frame = tk.Frame(master=master_frame, bg="#D5A8A0")
        list_box_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)
        listbox = tk.Listbox(master=list_box_frame, background="#F4DBD6", width=40, height=25, font=self._LISTBOX_FONT,
                             highlightbackground="white",
                             selectbackground="#FBEEE6", selectforeground="#E77A63", activestyle="underline", justify="left")

        self.insert_list_box(listbox)

        listbox.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)


        scrollbar_vertical = tk.Scrollbar(master=list_box_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        button = tk.Button(master=master_frame, text="Choose note", font=self._BUTTON_FONT, background="#D5A8A0",
                           command=lambda listbox=listbox: self.get_note(listbox.get(tk.ANCHOR)))
        button.pack(fill=tk.BOTH, side=tk.TOP, padx=130, pady=6, expand=True)

    def insert_list_box(self, listbox):
        listbox.delete(0,'end')
        for note in self._list_of_notes:
            listbox.insert(tk.END, note.getheader() + "(" + str(note.getid()) + ")")

    def get_note(self, note_str):
        return int(note_str[-2])




    list_of_notes = property(get_list_of_notes)
    master = property