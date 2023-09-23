from os import path
import os 
import json 
        
class DataJS:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = []
        
    def get_data(self): #Places content into data
        if path.isfile(self.file_name) is False:
            raise Exception("File not found")
        f = open(self.file_name,"r") #opens file 
        der = json.load(f)   # places contents of the file in der 
        self.data = der       #places content into instance var 
        f.close()
        return self.data
class Files:
    def __init__(self):
        self.files = []
    def add_to_list(self):
            for i in os.listdir("example-data"):
                if ".json" in i:
                    #i = DataJS(i)
                    self.files.append(i)
        
if __name__ == "__main__":
    f = Files()
    #print(os.listdir("example-data"))



