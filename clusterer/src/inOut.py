import os
import json
import src.config as conf

def getData(depth = None, path = None):
    raw_data = {}

    if depth is not None:
        if depth == "d1":
            path = conf.path_bereinigtesCrawlErgebnis_Startseiten
        elif depth == "d16":
            path = conf.path_bereinigtesCrawlErgebnis_16
        elif depth == "d1_eva":
            path = conf.path_bereinigtesCrawlErgebnis_Startseiten_Evaluation
        elif depth == "d16_eva":
            path = conf.path_bereinigtesCrawlErgebnis_16_Evaluation

    with open(path, "r") as json_file:
        raw_data = json.load(json_file)
    
    return raw_data

def dict2file(dictionary, destination_path, file_name):
    file_name_with_path = destination_path + "\\" + file_name

    dict_json = json.dumps(dictionary)

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    if os.path.isfile(file_name_with_path):
        os.remove(file_name_with_path)
        
    with open(file_name_with_path,"w") as file:
        file.write(dict_json)

def file2dict(pfad):
    with open(pfad) as file:
        data = json.load(file)
        return data

def file2list(pfad):
    file = open(pfad, "r")
    stopwords = file.readlines()
    return [w.rstrip() for w in stopwords]

def list2file(liste, pfad):
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
        
    with open(pfad,"w") as file:
        for item in liste:
            file.write(item)
            file.write('\n')