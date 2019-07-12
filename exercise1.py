trains_list = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

#Exercise 1
direction_111 = trains_list[7]['direction'] # south

#Exercise 2
frequency_80B = trains_list[5]['frequency_in_minutes'] # 30

#Exercise 3
direction_610 = trains_list[2]['direction'] # north

#Exercise 6
def get_trains_from_heading(direction): #Returns a list of all trains heading in a certain direction.
    new_trains_list = []

    for train in trains_list: #Iterates through each train in the list.
        if (train['direction'] == direction):
            new_trains_list.append(train) #Appends train to new list.

    return new_trains_list

#Exercise 4
print(get_trains_from_heading('north')) #Prints 3 trains heading north.
print()

#Exercise 5
print(get_trains_from_heading('east')) #Prints 1 train heading east.
print()

#Exercise 7
trains_list[0]['first_departure_time'] = 6 #Adds 'first_departure_time:6' to first train.

#Exercise 8
def sort_trains_by_frequency(trains): #Returns a list of frequencies with and their specific trains.
    trains_by_frequency = {}

    for train in trains: #Iterates through each train in trains
        name = train['train'] #Train name.
        freq = train['frequency_in_minutes'] #Train frequency.

        if freq in trains_by_frequency: #If the frequency already exists in the list.
            trains_by_frequency[freq].append(name)
        else: #Else, this is a new frency and is added to the list.
            trains_by_frequency[freq] = [name]

    return trains_by_frequency

print(sort_trains_by_frequency(trains_list))