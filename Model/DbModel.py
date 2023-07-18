import mysql.connector
import logging
from Model.Logger import Logger

from Model.Note import Note

class DbModel():

    database = ""

    host = ""

    user = ""

    password = ""

    logger = Logger("")

    connection = None

    list = []

    def __init__(self, host, user, password, logger):
        self._host = host
        self._user = user
        self._password = password
        self._logger = logger
        self._connection = None
        self._logger.initialize()
        self._database = ""
    def init_connection(self):
        try:
            self._connection = mysql.connector.connect(host=self._host, user=self._user, password=self._password)
            self._logger.getlogger().info("Connection with db-server successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def setlogger(self, logger):
        self._logger = logger
    def create_notesdb(self, name):
        try:
            sql_command = f"CREATE DATABASE IF NOT EXISTS {name}"
            with self._connection.cursor() as cursor:
                cursor.execute(sql_command)
            self._database = name
            self._logger.getlogger().info(f"Database named '{name}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def create_notestable(self, name):
        try:
            sql_command = f"USE {self._database};" \
                          f"CREATE TABLE IF NOT EXISTS {name}(" \
                          f"date_of_creation VARCHAR(30)," \
                          f"id SERIAL," \
                          f"header VARCHAR(100)," \
                          f"body TEXT" \
                          f");"
            with self._connection.cursor() as cursor:
                cursor.execute(sql_command)
            self._logger.getlogger().info(f"Table named '{name}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)
    def updatetable(self, **kwargs):
        return

    def deletedata(self, **kwargs):
        return

    def getdata(self, **kwargs):
        return

    host = property
    user = property
    password = property
    node = property
    logger = property(setlogger)
    database = property
