from datetime import datetime

import mysql.connector
import private as private
import protected as protected

from Model.Logger import Logger

from Model.Note import Note


class DbModel():
    database_name = ""

    list_of_tables = []

    host = ""

    user = ""

    password = ""

    logger = Logger("")

    def __init__(self, host, user, password, logger):
        self._host = host
        self._user = user
        self._password = password
        self._logger = logger
        self._logger.initialize()
        self._database = ""
        self._list_of_tables = []

    def __init_connection_to_server(self):
        try:
            self._list_of_tables.clear()
            connection = mysql.connector.connect(host=self._host, user=self._user, password=self._password)
            sql_command = f"SELECT * FROM INFORMATION_SCHEMA.TABLES "
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                for row in cursor.fetchall():
                    table_name = str(row[2])
                    self._list_of_tables.append(table_name)
            self._logger.getlogger().info("Connection with db-server is successful")
            return connection
        except Exception as e:
            self._logger.getlogger().error(e)

    def __init_connection_to_db(self):
        try:
            self._list_of_tables.clear()
            connection = mysql.connector.connect(host=self._host, user=self._user, password=self._password, database=self._database_name)
            sql_command = f"SELECT * FROM INFORMATION_SCHEMA.TABLES "
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                for row in cursor.fetchall():
                    table_name = str(row[2])
                    self._list_of_tables.append(table_name)
            self._logger.getlogger().info("Connection with db-server is successful")
            return connection
        except Exception as e:
            self._logger.getlogger().error(e)


    def setlogger(self, logger):
        self._logger = logger

    def create_db(self, name_of_db):
        try:
            connection = self.__init_connection_to_server()
            sql_command = f"CREATE DATABASE IF NOT EXISTS {name_of_db}"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            connection.close()
            self._database = name_of_db
            self._logger.getlogger().info(f"Database named '{name_of_db}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def create_table(self, table_name):
        try:
            connection = self.__init_connection_to_db()
            if table_name in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' exist")
                return
            sql_command = f"USE {self._database};" \
                          f"CREATE TABLE IF NOT EXISTS {table_name}(" \
                          f"id INT AUTO_INCREMENT PRIMARY KEY," \
                          f"date_of_creation VARCHAR(30) NOT NULL," \
                          f"date_of_last_update VARCHAR(30)," \
                          f"header VARCHAR(100) NOT NULL," \
                          f"body TEXT" \
                          f");
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                connection.commit()
            self._list_of_tables.append(table_name)
            self._logger.getlogger().info(f"Table named '{table_name}' was created successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def drop_table(self, table_name):
        try:
            connection = self.__init_connection_to_db()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            sql_command = f"DROP TABLE {table_name}" \
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            connection.close()
            self._logger.getlogger().info(f"Table named '{table_name}' was dropped successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def insert_into_table(self, table_name, note):
        try:
            connection = self.__init_connection()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            sql_command = f"USE {self._database};" \
                          f"INSERT INTO {table_name} (date_of_creation, header, body)" \
                          f"VALUES" \
                          f"({note.getdate_of_creation()}, {note.getheader()}, {note.getbody()});"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            connection.commit()
            connection.close()
            self._logger.getlogger().info(f"Inserting into table '{table_name}' was successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def update_data(self, table_name, note):
        try:
            connection = self.__init_connection()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            date_of_update = str(datetime.datetime.now())
            sql_command = f"USE {self._database};" \
                          f"UPDATE {table_name}" \
                          f"SET header = {note.getheader()}, body = {note.getbody()}, date_of_last_update = {date_of_update}" \
                          f"WHERE id = {note.getid()};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            self._logger.getlogger().info(f"Note with id '{note.getid()}' was updated successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def delete_data(self, table_name, note):
        try:
            connection = self.__init_connection()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            sql_command = f"USE {self._database};" \
                          f"DELETE FROM {table_name}" \
                          f"WHERE id = {note.getid()};"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
            self._logger.getlogger().info(f"Note with id '{note.getid()}' was deleted successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_all_data(self, table_name):
        list_of_notes = []
        try:
            connection = self.__init_connection()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            sql_command = f"USE {self._database};" \
                          f"SELECT * FROM {table_name}"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                for row in result:
                    note = Note(row[0], row[3], row[4])
                    note.setdate_of_last_update(row[2])
                    list_of_notes.append(note)
            return list_of_notes
            self._logger.getlogger().info(f"Select was successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    def get_limit_data(self, table_name, limit):
        try:
            int(limit)
            list_of_notes = []
            connection = self.__init_connection()
            if table_name not in self._list_of_tables:
                self._logger.getlogger().info(f"This table '{table_name}' doesn't exist")
                return
            sql_command = f"SELECT * FROM {table_name} LIMIT {limit}"
            with connection.cursor() as cursor:
                cursor.execute(sql_command)
                result = cursor.fetchall()
                for row in result:
                    note = Note(row[0], row[3], row[4])
                    note.setdate_of_last_update(row[2])
                    list_of_notes.append(note)
            return list_of_notes
            self._logger.getlogger().info(f"Limit select was successful")
        except Exception as e:
            self._logger.getlogger().error(e)

    host = property
    user = property
    password = property
    logger = property(setlogger)
    database_name = property
    list_of_tables = property
