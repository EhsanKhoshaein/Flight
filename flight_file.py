def load():
    flight_char_list = []
    flight_list = []
    flight_file = open('flights.txt','r')
    flight_char = flight_file.readlines()
    for flight in flight_char:
        new_flight_char = flight.split('\n')
        for item in new_flight_char:
            if item != '':
                flight_char_list.append(item)
    for item in flight_char_list:
            new_item = item.split(' - ')
            flight_list.append(new_item)
    flight_file.close()
    return flight_list

def save(flight):
    flight_char = ''
    i = 0
    while(i <= len(flight)):
        if i == len(flight)-1:
            flight_char = flight_char + flight[i]
            break
        flight_char = flight_char + flight[i] + ' - '
        i += 1
    flight_file = open('flights.txt','a')
    flight_file.writelines(flight_char + '\n')
    flight_file.close()
    #return flight_file

def rewrite(flight_list):
    flight_file = open('flights.txt','w')
    flight_file.close()
    for flight in flight_list:
        flight_char = ''
        i = 0
        while(i <= len(flight)):
            if i == len(flight)-1:
                flight_char = flight_char + flight[i]
                break
            flight_char = flight_char + flight[i] + ' - '
            i += 1
        flight_file = open('flights.txt','a')
        flight_file.writelines(flight_char + '\n')
        flight_file.close()
    return flight_file
