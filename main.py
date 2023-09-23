"""
To recap, you are here to build an AI Data Assistant. Your co-pilot for the semi-structured data that many companies has.
 The copilot should make life of Human Data Assistant easier by getting insights from the data it has access to.
"""
import sqlite3
from transformers import BertTokenizer
from nltk.corpus import stopwords

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

        return rows

    def query_fun(self, question:str, tables:list[str]):
        """This function will be run once for each question related to the given database."""
        #Tokenize the question - in order for it to be read by the ai
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")  #create the tokenizer
        stop_words = set(stopwords.words("english"))         #set of english stop words like commas, full stops and question marks
        tokens = tokenizer.tokenize(question)
        for token in tokens:
            if token in stopwords:
                tokens.remove(token)            #removing any stop words so that ai doesn't need to process them and can read more efficiently  

    
        


user = DatabaseAI("app.db")
rows = user.connect_fun()

question = input("Enter your question: ")
user.query_fun(question, rows)