import os

import pandas


class JsonFileHandlingPandas:


        def create_file(self, file):
            # df = pandas.DataFrame(self.data)
            # json_string = df.to_json(orient="records")
            with open(file, 'x') :
                pass
                # f.write(json_string)


        def delete_file(self,file):
            if os.path.exists(file):
                os.remove(file)


        def read_file(self,file):
            return pandas.read_json(file)


        def write_file(self,file,data):
            df = pandas.DataFrame(data)
            json_string = df.to_json(orient="records")
            with open(file, 'x') as f:
                f.write(json_string)


        def append_file(self,file,content):
            old_data = pandas.read_json(file)
            new_data = pandas.DataFrame(content)
            # c=old_file.append(df)
            # df.to_json(file, mode='a',header=False, index=False)
            combined_data = pandas.concat((old_data,new_data),ignore_index=True)
            print(combined_data)


file_handle = JsonFileHandlingPandas()
file = 'output.json'
# file_handle.create_file(file)
# file_handle.delete_file(file)
# content = {"username": ['a','b','c','d']}
# file_handle.write_file(file,data)
file_handle.read_file(file)
# file_handle.append_file(file,content)




