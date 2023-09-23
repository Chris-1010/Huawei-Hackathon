from os import path
import os 
import json 
        
class DataJS:
    def __init__(self,file_name):
        self._file_name = file_name
        self._data = {"sql":[],"questions":[]}               #Stores data of individual files 
        self.get_data()

    def get_data(self):
        self._file_name = os.path.join("example-data/", self._file_name)                                    #Places content into data
        if path.isfile(self._file_name) is False:
            raise Exception("File not found")
        f = open(self._file_name,"r")                        #opens file 
        self._der = json.load(f)                                   #places contents of the file in der 
        f.close()
        self.sort_data()
        return self._der
    
    def sort_data(self):                                    #Method goes through data set of instance and catorgrizes data (Qs & SQL)
        for i in range(len(self._der)):
            for key in self._der[i].keys():                 #Goes through array of keys 
                if key == "question":
                    self._data["questions"].append(self._der[i][key])
                elif key == "sql":
                    self._data["sql"].append(self._der[i][key])
        return self._data

class Files:
    def __init__(self):
        self.files = {}                                     #Stores all the instances of DataJS
        all_files = self.add_to_list()                                  #Adds files to list
        return all_files
    def add_to_list(self):
            for i in os.listdir("example-data"):            #goes through list of files in "example-data" folder
                if ".json" in i:
                    der = DataJS(i)
                    self.files[i] = der
        
if __name__ == "__main__":
    f = Files()                                               #Initializes Files
    print(f.files["example-covid-vaccinations.json"]._data)
        
   # print(f.files["example-covid-vaccinations.json"]._data)

    
