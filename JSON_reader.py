from os import path
import os 
import json 
        
class DataJS:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = []                                      #Stores data of individual files 
        self.questions = []
        self.sql = []
    def get_data(self):
        self.file_name = os.path.join("example-data/",self.file_name)                                     #Places content into data
        if path.isfile(self.file_name) is False:
            raise Exception("File not found")
        f = open(self.file_name,"r")                        #opens file 
        der = json.load(f)                                  # places contents of the file in der 
        self.data = der                                     #places content into instance var 
        f.close()
        self.sort_data()
        return self.data
    def sort_data(self):
        for i in range(len(self.data)):
            for key in self.data[i].keys():                 #Goes through array of keys 
                if key == "question":
                    self.questions.append(self.data[i][key])
                elif key == "sql":
                    self.sql.append(self.data[i][key])
        return self.questions,self.sql

class Files:
    def __init__(self):
        self.files = []                                     #Stores all the instances of DataJS
    def add_to_list(self):
            for i in os.listdir("example-data"):            #goes through list of files in "example-data" folder
                if ".json" in i:
                    der = DataJS(i)
                    self.files.append(der)
        
if __name__ == "__main__":
    f = Files()
    f.add_to_list()
    hi = f.files[0]
    hi.get_data()
    #print(hi.questions)
    print(hi.sql)




