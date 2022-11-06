# Print result after every function to check
# Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths = 'C:/Users/vikalp/Documents/Python programming/data.json'


def read_data(filepaths):
    with open(filepaths) as json_file:
        data = json.load(json_file)
    # Read data from filepaths
    # for i in data['AVENGERS']:
    #     print(i)
    # for i in data['DC']:
    #     print(i)


data = read_data(filepaths)


def get_oldest(data):
    max = float('inf')
    c = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest = data["AVENGERS"][i]['age']

        if data["AVENGERS"][i]['age'] == max:   
            oldest[c] = data["AVENGERS"][i]
            c += 1

    for i in data["DC"]:
        if (data["DC"][i]['age'] > max):
            max = data["DC"][i]['age']
            oldest = data["DC"][i]

        if data["DC"][i]['age'] == max:
            oldest[c] = data["DC"][i]
            c += 1
    
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    return oldest
# returns info: Thor and Wonder Woman
def get_oldest_avenger(data):
    max = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest_avenger = data["AVENGERS"][i]
    # Return all info of the oldest avenger
    return oldest_avenger
# returns info: Thor


def get_total_points(data):
    total_points = {}
    for i in data["AVENGERS"]:
        key = data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key] += data["AVENGERS"][i]['points'][j]
    for i in data["DCU"]:
        key = data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key] += data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points

# returns info: Dict of superhero name and total points


def get_more_than_average(data):
    more_than_average = []
    avg_mcu = 0
    avg_dc = 0
    for i in data["AVENGERS"]:
        avg_mcu += data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu = avg_mcu/len(data["AVENGERS"])
    c = 0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['points']['stealth'] > avg_mcu):
            more_than_average[c] = data["AVENGERS"][i]
            c += 1
    for i in data["DC"]:
        avg_dc += data["DC"][i]['points']['strength']
    avg_dc = avg_dc/len(data["DC"])
    for i in data["DC"]:
        if (data["DC"][i]['points']['strength'] > avg_dc):
            more_than_average[c] = data["DC"][i]
            c += 1
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average

  # returns info: Steve Rogers and Superman


def get_names(data):
    names = []
    p = 0
    for i in data["AVENGERS"]:
        names.insert(p, data[i])
        p += 1
    for j in data["DC"]:
        names.insert(p, data[j])
        p+=1
    # Return a list of superhero names
    return names

# returns a list
