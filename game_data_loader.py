import json, pickle

def load_file(file_path):
    extention = file_path.split(".")[-1]
     
    if extention == "pkl":
        with open(file_path, 'rb') as file:
            data = pickle.load(file)

    elif extention == "json":
        with open(file_path, 'r') as file:
            data = json.load(file)
    return data

def save_to_file(file_path, content):
    extention = file_path.split(".")[-1]

    if extention == "pkl":
        with open(file_path, 'wb') as file:
            pickle.dump(content, file)

    elif extention == "json":
        with open(file_path, 'w') as file:
            json.dump(content, file, indent = 4)