import mysql
import mysql.connector

class Check_db_connection():
    def __init__(self, logger):
        self._logger = logger
        self._is_connect = False

    def check_db_connection(self, login, password):
        try:
            connection = mysql.connector.connect(host="localhost", user=login, password=password)
            self._is_connect = True
            self._logger.getlogger().info("GOOD choice of connecting to database")
        except Exception as e:
            self._logger.getlogger().warning("BAD choice of connecting to database")

    def get_result(self):
        return self._is_connect

    logger = property
    is_connect = property
