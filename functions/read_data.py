import json
def read_data(file_name):
    with open(file_name) as file:
        data = json.load(file)
        data_time = data['data_time']
        other_data = data['ohter_data']
        return data_time, other_data