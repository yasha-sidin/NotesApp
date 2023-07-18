from Model.DbModel import DbModel
from Model.Logger import Logger
from Model.Note import *
import mysql.connector
import logging

logger = Logger("applogs")

db = DbModel("localhost", "root", "131214", logger)
db.create_db("notes_data")
note1 = Note(0, "My life", "Hello World!!! I am here.")
db.insert_into_table("notes_table", note1)




