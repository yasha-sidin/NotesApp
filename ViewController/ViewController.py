from Model.Check_db_connection import Check_db_connection
from Model.Db_model import Db_model
from Model.Logger import Logger
import tkinter as tk
from ViewController.Data_frame import Data_frame
from ViewController.Login_frame import Login_frame
from ViewController.Note_frame import Note_frame

class ViewController:
    def __init__(self, database_name, table_name, logger_path, icon_path, title):
        self._database_name = database_name
        self._table_name = table_name
        self._logger_path = logger_path
        self._icon_path = icon_path
        self.title = title

    def initialize(self):
        logger = Logger(self._logger_path)
        check_db_connection = Check_db_connection(logger)

        login_frame = Login_frame(check_db_connection, self._icon_path)
        login_frame.initialize(lambda: self.__init_app(login_frame.get_login(), login_frame.get_password(), logger))

    def __init_app(self, login, password, logger):

        db = Db_model("localhost", login, password, logger, self._database_name)
        db.init_db()
        db.create_table(self._table_name)

        window = tk.Tk()
        window.title(self.title)
        window.iconbitmap(self._icon_path)
        window.minsize(width=1100, height=784)

        note_frame = Note_frame(window, db, self._table_name)
        data_frame = Data_frame(window, db, self._table_name, note_frame)

        data_frame.initialize()

        window.mainloop()

database_name = property
table_name = property
logger_path = property
icon_path = property
title = property