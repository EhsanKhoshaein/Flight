def searching(search, flight_list):
    flag = 0
    finded_flights_list = []
    for flight in flight_list:
        if flight[1] == search[0]:
            if flight[2] == search[1]:
                finded_flights_list.append(flight)
                flag = 1
    if flag == 1:
        if len(finded_flights_list) == 1:
            print('\n  a Flight from {} to {} is existed:\n'.format(search[0],search[1]))
        else:
                print('\n  {} Flights from {} to {} are existed:\n'.format(len(finded_flights_list), search[0],search[1]))
        print('\n+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
        print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUMBER','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','CAPACITY'))
        print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
        for flight in finded_flights_list:
            for item in flight:
                print("|",end='')
                print("{0: ^20s}".format(item),end='')
            print("|",end='\n')
        print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
    else:
        print("\n  sorry .. Flight with these informations doesn't exist in flights list ..!")
