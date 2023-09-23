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
        rows = cursor.execute("""SELECT * FROM covid_vaccinations LIMIT 1;""").fetchall()


        #Close connection
        cursor.close()
        conn.close()

        return rows

    def query_fun(question:str, tables:list[str], database_connection: object):
        """This function will be run once for each question related to the given database."""
        return


databases = {"covid_vaccinations": "example-data/example-covid-vaccinations.sqlite3", "simple_users": "example-data/example-simple.sqlite3", "murder_mystery": "example-data/sql-murder-mystery.sqlite3"}
database = databases[input("Would you like to use the database of:\n'covid_vaccinations',\t'',\t'simple_users'")] # sub in whatever database you'd like instead of "simple_users"
the_ai = DatabaseAI(database)
print(the_ai.connect_fun())

# from datasets import load_dataset
# dataset = load_dataset("fka/awesome-chatgpt-prompts")