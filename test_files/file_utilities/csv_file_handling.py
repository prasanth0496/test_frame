
import os

import pandas


class CSVFileHandling:


    def __init__(self, path):
        self.path = path


    def create_file(self):
        with open(self.path, 'w') as file:
            file.write('')
            pass
            # json.dumps(file)
            # file.write(data)


    def delete_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)


    def read_file(self):
        pandas.read_csv(self.path)


    def write_file(self,content1):
        df = pandas.DataFrame(content1)
        df.to_csv(self.path)
        # with open(path,'w') as file:
        #     file.write()


    def append_file(self,content2):
        old_data = pandas.read_csv(self.path)
        new_data = pandas.DataFrame(content2)
        combined_data = pandas.concat((old_data, new_data), ignore_index=True)
        print(combined_data)


path = "data.csv"
file_handle = CSVFileHandling(path)
# file_handle.create_file()
# file_handle.delete_file()
file_handle.read_file()
content1 = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [30, 25, 28],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
content2 = {
    'Name': ['Eve', 'Tom'],
    'Age': [35, 27],
    'City': ['San Francisco', 'Seattle']
}
# file_handle.write_file(content1)
file_handle.append_file(content2)


