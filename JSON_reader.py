from os import path
import json 
class dataJS:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = []
    def help(self):
        if path.isfile(self.file_name) is False:
            raise Exception("File not found")
        f = open(self.file_name,"r") #opens file 
        der = json.load(f)   # places contents of the file in der 
        self.data = der       #places content into instance var 
        
        f.close()

test1 = dataJS("example-data\example-covid-vaccinations.json")
test1.help()
print(test1.data)
