import json
import os

class JsonFileHandling:

    def create_file(self,path):
        with open(path, 'x'):
            pass
            # json.dump(file)
            # file.write(data)


    def delete_file(self,path):
        if os.path.exists(path):
            os.remove(path)


    def read_file(self,path):
        with open (path,'r') as file:
            # file.read()
            return json.load(file)



    def write_file(self,path,content):
        with open(path,'w') as file:
            file.write(content)


    def append_file(self,path,content):
        with open(path,'a') as file:
            # file.read()
            file.write(content)
            # json.dump(content,file)



# file_handle = JsonFileHandling()
# path = "data.json"
# file_handle.create_file(path)
# file_handle.delete_file(path)
# file_handle.read_file(path)
# content = "prasanth"
# file_handle.write_file(path,content)
# file_handle.append_file(path,content)


