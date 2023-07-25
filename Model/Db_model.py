from datetime import datetime

import mysql.connector
import private as private
import protected as protected

from Model.Logger import Logger

from Model.Note import Note


class Db_model():
    database_name = ""

    list_of_databases = []

    list_of_tables = []

    host = ""

    user = ""

    password = ""

    logger = Logger("")

    def __init__(self, host, user, password, logger, database_name):
        self._host = host
        self._user = user
        self._password = password
        self._logger = logger
        self._logger.initialize()
        self._database_name = database_name
        self._list_of_tables = []
        self._list_of_databases = []

    def __init_connection_to_server(self):
        try:
            self._list_of_tables.clear()
            connection = mysql.connector.connect(host=self._host, user=self._user, password=self._password)
            sql_command = f"SELECT * FROM INFORMATION_SCHEMA.TABLES;"
            sql_command2 = f"SHOW DATABASES;"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                for row in cursor.fetchall():
                    table_name = str(row[2])
                    self._list_of_tables.append(table_name)
                cursor.execute(sql_command2)
                for row in cursor.fetchall():
                    db_name = str(row[0])
                    self._list_of_databases.append(db_name)
            self._logger.getlogger().info("Connection with db-server is successful")
            return connection
        except Exception as e:
            self._logger.getlogger().error(e)

    def __init_connection_to_db(self):
        try:
            connection = mysql.connector.connect(host=self._host, user=self._user, password=self._password, database=self._database_name)
            self._logger.getlogger().info("Connection with db-server is successful")
            return connection
        except Exception as e:
            self._logger.getlogger().error(e)


    def setlogger(self, logger):
        self._logger = logger

    def init_db(self):
        try:
            connection = self.__init_connection_to_server()
            if self._database_name in self._list_of_databases:
                self._logger.getlogger().info(f"This database '{self._database_name}' exist")
                return
            sql_command = f"CREATE DATABASE IF NOT EXISTS {self._database_name};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            connection.close()
            self._logger.getlogger().info(f"Database named '{self._database_name}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def create_table(self, table_name):
        try:
            connection = self.__init_connection_to_server()
            connection = self.__init_connection_to_db()
            if table_name in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' exist")
                return
            sql_command = f"CREATE TABLE IF NOT EXISTS {table_name}(" \
                          f"id INT AUTO_INCREMENT PRIMARY KEY," \
                          f"date_of_creation VARCHAR(30) NOT NULL," \
                          f"date_of_last_update VARCHAR(30)," \
                          f"header VARCHAR(100) NOT NULL," \
                          f"body TEXT" \
                          f");"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._list_of_tables.append(table_name)
            self._logger.getlogger().info(f"Table named '{table_name}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def drop_table(self, table_name):
        try:
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"DROP TABLE IF EXISTS {table_name};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._logger.getlogger().info(f"Table named '{table_name}' was dropped successful")
            self._list_of_tables.remove(table_name)
        except Exception as e:
            self._logger.getlogger().error(e)

    def insert_into_table(self, table_name, note):
        try:
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"INSERT INTO {table_name} (date_of_creation, header, body)" \
                          f"VALUES" \
                          f"('{note.getdate_of_creation()}', '{note.getheader()}', '{note.getbody()}');"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._logger.getlogger().info(f"Inserting into table '{table_name}' was successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def update_data(self, table_name, note):
        try:
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            date_of_update = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql_command = f"UPDATE {table_name} SET " \
                          f"header = '{note.getheader()}'," \
                          f"body = '{note.getbody()}'," \
                          f"date_of_last_update = '{date_of_update}'" \
                          f"WHERE id = {note.getid()};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._logger.getlogger().info(f"Note with id '{note.getid()}' was updated successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def delete_data(self, table_name, note):
        try:
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"DELETE FROM {table_name} " \
                          f"WHERE id = {note.getid()};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._logger.getlogger().info(f"Note with id '{note.getid()}' was deleted successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_all_data(self, table_name):
        list_of_notes = []
        try:
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"SELECT * FROM {table_name};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                for row in result:
                    note = Note(row[0], row[3], row[4])
                    note.setdate_of_last_update(row[2])
                    list_of_notes.append(note)
                connection.commit()
            self._logger.getlogger().info(f"Select was successful")
            return list_of_notes
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_limit_data(self, table_name, limit_start, limit_end):
        try:
            limit_start = int(limit_start)
            limit_end = int(limit_end)
            list_of_notes = []
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"SELECT * FROM {table_name} LIMIT {limit_start},{limit_end};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                for row in result:
                    note = Note(row[0], row[3], row[4])
                    note.setdate_of_last_update(row[2])
                    list_of_notes.append(note)
                connection.commit()
            self._logger.getlogger().info(f"Limit select was successful")
            return list_of_notes
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_note_by_id(self, table_name, id):
        try:
            note = None
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"SELECT * FROM {table_name} WHERE id = {id};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                note = Note(result[0][0], result[0][3], result[0][4])
                note.setdate_of_last_update(result[0][2])
                connection.commit()
            self._logger.getlogger().info(f"Note with id '{result[0][0]}' was selected successful")
            return note
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_last_id(self, table_name):
        try:
            id = 0
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            connection = self.__init_connection_to_db()
            sql_command = f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1;"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                id = result[0][0]
                connection.commit()
            self._logger.getlogger().info(f"Last id was selected successful")
            return id
        except Exception as e:
            self._logger.getlogger().error(e)

    host = property
    user = property
    password = property
    logger = property(setlogger)
    database_name = property
    list_of_tables = property
    list_of_databases = property

