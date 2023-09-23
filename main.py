"""
To recap, you are here to build an AI Data Assistant. Your co-pilot for the semi-structured data that many companies has.
 The copilot should make life of Human Data Assistant easier by getting insights from the data it has access to.
"""

import sqlite3
class DatabaseAI(object):
    def __init__(self, database_name:str):
        self._database_name = database_name

    def connect_fun(self):
        """Object that should “establish a connection” to a given SQLite file. 
            That function will be run once before all the questions related to the given database"""
        #Connect to SQLite
        conn = sqlite3.connect(self._database_name)
        cursor = conn.cursor()

        #Execute a query
        cursor.execute("""SELECT * FROM covid_vaccinations""")
        rows = cursor.fetchall()


        #Close connection
        cursor.close()
        conn.close()

    def query_fun(question:str, tables:list[str], database_connection: object):
        """This function will be run once for each question related to the given database."""

user = DatabaseAI("app.db")