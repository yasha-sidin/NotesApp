from Model.Db_model import Db_model
from Model.Logger import Logger
from Model.Note import *
import mysql.connector
import logging
import tkinter as tk
import tkinter.font as tkFont
from ViewController.Data_frame import Data_frame
from ViewController.Note_frame import Note_frame

logger = Logger("applogs")

db = Db_model("localhost", "root", "131214", logger, "notes_data")
db.init_db()
# db.drop_table("test_notes")
db.create_table("test_notes")
# db.create_table("your_notes")
# # note1 = Note(0, "first", "Text some")
# # note2 = Note(0, "second", "Text some")
# # note3 = Note(0, "third", "Text some")
# # note4 = Note(0, "fourth", "Text some")
# # note5 = Note(0, "fifth", "Text some")
# # note6 = Note(0, "sixth", "Text some")
# # list_of_notes = [note1, note2, note3, note4, note5]
# # for note in list_of_notes:
# #     db.insert_into_table("your_notes", note)
#
# note = Note(1, "update", "new text")
# db.update_data("your_notes", note)
# note_del = Note(2, "hesss", "dddddd")
# db.delete_data("your_notes", note_del)
# result = db.get_limit_data("your_notes", 0, 3)
# print(result)

window = tk.Tk()
window.minsize(width=1100, height=784)

note_frame = Note_frame(window, db, "test_notes")
data_frame = Data_frame(window, db, "test_notes", note_frame)

data_frame.initialize()


window.mainloop()



