from Model.DbModel import DbModel
from Model.Logger import Logger
from Model.Note import *
import mysql.connector
import logging

node = Note(1, "Test1", "NJNHYGUYBBIIUHHIBIUBUI")
print(Note.getid(node), Note.getheader(node), Note.getbody(node))

node1 = Note(2, "Test2", "NJNHYGvvvvvvvvvvvvvvvvvvvI")
print(Note.getid(node1), Note.getheader(node1), Note.getbody(node1), Note.getdate_of_creation(node1))

logger = Logger("applogs")

db = DbModel("localhost", "root", "131214", logger)
db.init_connection()
db.create_notesdb("Notes")
db.create_notestable("Notes_table")



