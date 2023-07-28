import tkinter.font as tkFont
import tkinter as tk
from tkinter.messagebox import showerror



class Login_frame():
    def __init__(self, check_db_connection, icon_path):
        self._check_db_connection = check_db_connection
        self.login_window = None
        self._string_var_login = None
        self._string_var_password = None
        self._login = None
        self._password = None
        self._icon_path = icon_path

    def initialize(self, login_function):
        self._login_window = tk.Tk()
        self._login_window.iconbitmap(self._icon_path)
        self._login_window.grab_set()
        self._login_window.title("Sign in MySQL")
        self._login_window.minsize(width=350, height=217)
        self._login_window.maxsize(width=350, height=217)

        main_frame = tk.Frame(master=self._login_window, width=100, height=350, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)

        MAIN_LABEL_FONT = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        LABEL_FONT = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
        ENTRY_FONT = tkFont.Font(family="Arial", size=10, slant="italic")
        BUTTON_FONT = tkFont.Font(family="Times New Roman", size=12, weight="bold", slant="italic")

        sign_in_frame = tk.Frame(master=main_frame, width=100, height=350, bg="white")
        sign_in_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        sign_in_label = tk.Label(master=sign_in_frame, text="Enter your login data from MySQL:", bg="#F7F2EF", width=26, height=2,
                                     relief="ridge", font=MAIN_LABEL_FONT, justify=tk.LEFT)
        sign_in_label.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        # login part
        login_frame = tk.Frame(master=sign_in_frame, width=100, height=350, bg="white")
        login_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        login_label = tk.Label(master=login_frame, text="Login:", bg="#F7F2EF", relief="ridge", font=LABEL_FONT, justify=tk.LEFT)
        login_label.pack(side=tk.LEFT)

        self._string_var_login = tk.StringVar(self._login_window)
        login_entry = tk.Entry(master=login_frame, bg="white", font=ENTRY_FONT, relief="ridge",
                                     justify=tk.LEFT, textvariable=self._string_var_login,
                                     selectbackground="#E1D0C8", selectforeground="black", width=28)
        login_entry.pack(side=tk.LEFT)

        # password part
        password_frame = tk.Frame(master=sign_in_frame, width=100, height=350, bg="white")
        password_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        password_label = tk.Label(master=password_frame, text="Password:", bg="#F7F2EF", relief="ridge", font=LABEL_FONT,
                               justify=tk.LEFT)
        password_label.pack(side=tk.LEFT)
        self._string_var_password = tk.StringVar(self._login_window)
        password_entry = tk.Entry(master=password_frame, bg="white", font=ENTRY_FONT, relief="ridge",
                                     justify=tk.LEFT, textvariable=self._string_var_password,
                                     selectbackground="#E1D0C8", selectforeground="black", width=25, show="*")
        password_entry.pack(side=tk.LEFT)

        #buttons part
        button_frame = tk.Frame(master=main_frame, bg="white")
        button_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=90, pady=15, anchor=tk.CENTER)

        button_login = tk.Button(master=button_frame, text="Login", font=BUTTON_FONT,
                                  background="#F7F2EF", activebackground="white",
                                  command=lambda function=login_function: self.__check_connection_action(function))

        button_login.pack(side=tk.LEFT, padx=10)

        button_cancel = tk.Button(master=button_frame, text="Cancel", font=BUTTON_FONT,
                                  background="#F7F2EF", activebackground="white",
                                  command=self._login_window.destroy)
        button_cancel.pack(side=tk.LEFT, padx=10)

        self._login_window.mainloop()

    def __check_connection_action(self, login_function):
        self._check_db_connection.check_db_connection(self._string_var_login.get(), self._string_var_password.get())
        if self._check_db_connection.get_result():
            self._login = self._string_var_login.get()
            self._password = self._string_var_password.get()
            self._login_window.destroy()
            login_function()
        else:
            showerror(title='Error', message="Wrong login or password. Please try again or cancel.")

    def get_login(self):
        return self._login

    def get_password(self):
        return self._password

check_db_connection = property
login_window = property
string_var_login = property
string_var_password = property
login = property
password = property
icon_path = property
