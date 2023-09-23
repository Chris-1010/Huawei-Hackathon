from os import path
import os 
import json 
        
class DataJS:
    def __init__(self,file_name):
        self._file_name = file_name
        self._data = []                                      #Stores data of individual files 
        self._questions = []                                 #Stores example questions 
        self._sql = []                                       #Store example query 

    def get_data(self):
        self._file_name = os.path.join("example-data/", self._file_name)                                    #Places content into data
        if path.isfile(self._file_name) is False:
            raise Exception("File not found")
        f = open(self._file_name,"r")                        #opens file 
        der = json.load(f)                                  #places contents of the file in der 
        self._data = der                                     #places content into instance var 
        f.close()
        self.sort_data()
        return self._data
    
    def sort_data(self):                                    #Method goes through data set of instance and catorgrizes data (Qs & SQL)
        for i in range(len(self._data)):
            for key in self._data[i].keys():                 #Goes through array of keys 
                if key == "question":
                    self._questions.append(self._data[i][key])
                elif key == "sql":
                    self._sql.append(self._data[i][key])
        return self._questions,self._sql

class Files:
    def __init__(self):
        self.files = []                                     #Stores all the instances of DataJS
        all_files = self.add_to_list()                                  #Adds files to list
        return all_files
    def add_to_list(self):
            for i in os.listdir("example-data"):            #goes through list of files in "example-data" folder
                if ".json" in i:
                    der = DataJS(i)
                    self.files.append(der)
        
if __name__ == "__main__":
    f = Files()                                             #Initializes Files
    content = {}
    for file_i in range(len(f)):
        f[file_i]
        content = f.files[file_i]
    content.get_data()                                           #Loads the JSON file content into the instance 
    print(content._questions)
    print("\n\n")
    print(content._sql)




