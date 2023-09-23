"""
To recap, you are here to build an AI Data Assistant. Your co-pilot for the semi-structured data that many companies has.
 The copilot should make life of Human Data Assistant easier by getting insights from the data it has access to.
"""
# pip install transformers, nltk, pytorch
import sqlite3
from transformers import BertTokenizer
import nltk
from nltk.corpus import stopwords

# nltk.download("stopwords")

class DatabaseAI(object):
    def __init__(self, database_name:str):
        self._database_name = database_name

    def connect_fun(self, database_name:str):
        """Object that should “establish a connection” to a given SQLite file. 
            That function will be run once before all the questions related to the given database"""
        #Connect to SQLite
        conn = sqlite3.connect(self._database_name)
        cursor = conn.cursor()

        #Execute a query
        rows = cursor.execute(f"SELECT * FROM {database_name};").fetchall()


        #Close connection
        cursor.close()
        conn.close()

        return rows

    def query_fun(self, question:str, tables:list[str]):
        """This function will be run once for each question related to the given database."""

        #Tokenize the question - in order for it to be read by the ai
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")  #create the tokenizer
        stop_words = set(stopwords.words("english"))         #set of english stop words like commas, full stops and question marks
        tokens = tokenizer.tokenize(question)
        for token in tokens:
            if token in stop_words:
                tokens.remove(token)            #removing any stop words so that ai doesn't need to process them and can read more efficiently  


databases = {"covid_vaccinations": "example-data/example-covid-vaccinations.sqlite3", "orders": "example-data/example-simple.sqlite3", "murder_mystery": "example-data/sql-murder-mystery.sqlite3"}
preferred_database = input("Would you like to use the database of:\n'covid_vaccinations',\t'orders'")
while preferred_database not in databases:
        print("Not a valid Database")
        preferred_database = input("Would you like to use the database of:\n'covid_vaccinations',\t'orders', or\t'murder_mystery'\n\n")
db_path = databases[preferred_database]
the_ai = DatabaseAI(db_path)
rows = the_ai.connect_fun(preferred_database)
print(rows)

#tokenizing
question = input("Enter your question: ")
the_ai.query_fun(question, rows)
