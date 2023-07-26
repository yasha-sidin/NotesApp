from Model.Check_db_connection import Check_db_connection
from Model.Db_model import Db_model
from Model.Logger import Logger
from Model.Note import *
import mysql.connector
import logging
import tkinter as tk
import tkinter.font as tkFont
from ViewController.Data_frame import Data_frame
from ViewController.Login_frame import Login_frame
from ViewController.Note_frame import Note_frame

class ViewController:
    def __init__(self, database_name, table_name, logger_path):
        self._database_name = database_name
        self._table_name = table_name
        self._logger_path = logger_path

    def initialize(self):
        logger = Logger(self._logger_path)
        check_db_connection = Check_db_connection(logger)

        login_frame = Login_frame(check_db_connection)


    def __init_app(self, login, password, logger):

        db = Db_model("localhost", login, password, logger, "notes_data")
        db.init_db()
        db.create_table(self._table_name)

        window = tk.Tk()
        window.minsize(width=1100, height=784)

        note_frame = Note_frame(window, db, "test_notes")
        data_frame = Data_frame(window, db, "test_notes", note_frame)

        data_frame.initialize()
