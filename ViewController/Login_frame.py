import tkinter.font as tkFont
import tkinter as tk
from tkinter.messagebox import showinfo, showerror

from Model.Check_db_connection import Check_db_connection
from Model.Logger import Logger


class Login_frame():
    def __init__(self, check_db_connection):
        self._chech_db_conection = check_db_connection


    def initialize(self):
        login_window = tk.Tk()
        login_window.grab_set()
        login_window.title("Sign in MySQl")
        login_window.minsize(width=350, height=250)
        login_window.maxsize(width=350, height=250)

        main_frame = tk.Frame(master=login_window, width=100, height=350, bg="#EBC8C1")
        main_frame.pack(fill=tk.BOTH, expand=True)

        LABEL_FONT = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        ENTRY_FONT = tkFont.Font(family="Arial", size=10, slant="italic")
        BUTTON_FONT = tkFont.Font(family="Times New Roman", size=12, weight="bold", slant="italic")

        login_frame = tk.Frame(master=main_frame, width=100, height=350, bg="#EBC8C1")
        login_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        login_label = tk.Label(master=login_frame, text="Enter your login data from MySQL:", bg="#D5A8A0", width=26, height=2,
                                     relief="ridge", font=LABEL_FONT, justify=tk.LEFT)
        login_label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        string_var_login = tk.StringVar(login_window)
        login_entry = tk.Entry(master=login_frame, bg="#D5A8A0", font=ENTRY_FONT, relief="ridge",
                                     justify=tk.LEFT, textvariable=string_var_login,
                                     selectbackground="#FBEEE6", selectforeground="#E77A63")
        login_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=2, expand=True)

        string_var_password = tk.StringVar(login_window)
        password_entry = tk.Entry(master=login_frame, bg="#D5A8A0", font=ENTRY_FONT, relief="ridge",
                                     justify=tk.LEFT, textvariable=string_var_password,
                                     selectbackground="#FBEEE6", selectforeground="#E77A63")
        password_entry.pack(fill=tk.X, side=tk.TOP, padx=6, pady=15, expand=True)

        button_frame = tk.Frame(master=main_frame, width=100, height=300, bg="#EBC8C1")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        button_create = tk.Button(master=button_frame, text="Create note", font=BUTTON_FONT,
                                  background="#D5A8A0", activebackground="#F4DBD6")
                                  # command=lambda top_level=choose_header_and_text_window:
                                  # self.create_note(top_level,
                                  #                  string_var_for_entry_header.get()) if string_var_for_entry_header.get() != ""
                                  # else showerror(title='Error',
                                  #                message="Header's entry is empty. Please name your note or cancel"))

        button_create.pack(fill=tk.BOTH, side=tk.LEFT, padx=30, pady=30, expand=True)

        button_cancel = tk.Button(master=button_frame, text="Cancel", font=BUTTON_FONT,
                                  background="#D5A8A0", activebackground="#F4DBD6",
                                  command=login_window.destroy)
        button_cancel.pack(fill=tk.BOTH, side=tk.LEFT, padx=30, pady=30, expand=True)

        login_window.mainloop()

logger = Logger("./NotesApp/logs/login.log")
check_db_connection = Check_db_connection(logger)
window = Login_frame(check_db_connection)
window.initialize()
