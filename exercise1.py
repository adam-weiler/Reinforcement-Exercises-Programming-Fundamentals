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
def get_trains_from_heading(direction):
    new_trains_list = []

    for train in trains_list: #Iterates through each train in the list.
        if (train['direction'] == direction):
            new_trains_list.append(train) #Appends train to new list.

    return new_trains_list

#Exercise 4
print(get_trains_from_heading('north')) #Prints 3 trains heading north.
print(\n)

#Exercise 5
print(get_trains_from_heading('east')) #Prints 1 train heading east.
print(\n)