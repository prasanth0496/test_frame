from file_utilities.json_file_handling import JsonFileHandling


def iteration(path):
    map_iteration = JsonFileHandling()
    map_data = map_iteration.read_file(path)
    for key in map_data:
        print(map_data[key])
path = "C:\\Users\\Prasanth\\PycharmProjects\\Framework1\\file_utilities\\map.json"
iteration(path)