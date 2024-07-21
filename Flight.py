flight_list = []
import flight_file
flight_list = flight_file.load()
class Flight:
    def __init__(self, number, origin, destination, date, hour, airport, airplane, capacity):
        self.number = number
        self.origin = origin
        self.destination = destination
        self.date = date
        self.hour = hour
        self.airport = airport
        self.airplane = airplane
        self.capacity = capacity

    @classmethod
    def flight_creating(cls, flight):
        number, origin, destination, date, hour, airport, airplane, capacity  = flight.split(' - ')
        return cls(number, origin, destination, date, hour, airport, airplane, capacity)
    @property
    def flight_items(self):
        flight_items = []
        flight_items.append(self.number)
        flight_items.append(self.origin)
        flight_items.append(self.destination)
        flight_items.append(self.date)
        flight_items.append(self.hour)
        flight_items.append(self.airport)
        flight_items.append(self.airplane)
        flight_items.append(self.capacity)
        return flight_items
    def origin_changing(self, edit):
        self.origin = edit
        a = self.number
        self.number = str(edit[0]) + str(self.destination[0]) + str(self.number[2]) + str(self.number[3]) + str(self.number[4])
        import os
        os.rename('{}.txt'.format(a), '{}.txt'.format(self.number))
            #change the name of the flight file to new    RENAME THE FILE
    def destination_changing(self, edit):
        self.destination = edit
        a = self.number
        self.number = str(self.origin[0]) + str(edit[0]) + str(self.number[2]) + str(self.number[3]) + str(self.number[4])
        import os
        os.rename('{}.txt'.format(a), '{}.txt'.format(self.number))
            #change the name of the flight file to new     RENAME THE FILE
    def date_changing(self, edit):
        self.date = edit
    def hour_changing(self, edit):
        self.origin = edit
    def hour_changing(self, edit):
        self.hour = edit
    def airport_changing(self, edit):
        self.airport = edit
    def airplane_changing(self, edit):
        self.airplane = edit

class Ticket:
    def __init__(self, name, nationalcode, seatnumber, datetime, price):
        self.__name = name
        self.__nationalcode = nationalcode
        self.__seatnumber = seatnumber
        self.datetime = datetime
        self.price = price
           
    def ticket_items(self):
        ticket_items = []
        ticket_items.append(self.__name)
        ticket_items.append(self.__nationalcode)
        ticket_items.append(self.__seatnumber)
        ticket_items.append(self.datetime)
        ticket_items.append(self.price)
        return ticket_items
    def changename(self, new_name):
        self.__name = new_name
        return new_name
    def changenationalcode(self, new_nationalcode):
        self.__nationalcode = new_nationalcode
        return new_nationalcode
    def changeseatnumber(self, new_seatnumber):
        self.__seatnumber = new_seatnumber
        return new_seatnumber
seat_num = []
i = 65
while(i<115):
    char = chr(i)
    for j in range(1,21):
        dig = j
        a = str(char) + str(dig)
        seat_num.append(a)
    i += 1
def seat_number(seat_num, tickets_list):
    global i
    if tickets_list == []:
        seatnumber = seat_num[0]
        return seatnumber
    else:
        seatnumber =  seat_num[len(tickets_list)]
        return seatnumber
    
          
username = input("USERNAME: ")
password = input("PASSWORD: ")
emp_info = ('employee','1234')  #username and password for employee
mgr_info = ('manager','qwer')   #username and password for manager
if username == mgr_info[0] and password == mgr_info[1]:
    print('\n\n       ',end = '')
    from time import sleep
    hi = " Hello dear Manager .. Welcome ! "
    for i in hi:
        print(i, end = '')
        sleep(0.3)


################################################################################################################################################################################################
    
    while(True):
        print('\n+=======================================================================================================================================================================+')
        print('''
    1. Create a Flight
    2. Search a Flight
    3. Enter to a Flight
    4. Show all Flights in Flight List
    5. Exit
    ''')
        mgr_choice = ('1','2','3','4','5')
        choice = input('Enter your choice: ')
        if choice not in mgr_choice:
            print('\n             WRONG INPUT !')
        elif choice == mgr_choice[0]:      
            if flight_list == []:
                number = 100
            else:
                num1, num2, num3 = flight_list[-1][0][2], flight_list[-1][0][3], flight_list[-1][0][4]
                number = int(num1+num2+num3)+1
            origin = input("\nenter the origin: ")
            destination = input("enter the destination: ")
            flight_number = '{}{}{}'.format(origin[0],destination[0],number)
            flight_char = (
            '{}'.format(flight_number) + ' - ' +
            '{}'.format(origin) + ' - '+
            '{}'.format(destination) + ' - ' +
            input('enter the flight mounth : ') + '/' + input('  and the day: ') + ' - ' +
            input('enter the flight hour : ') + ':' + input('  and the minute: ') + ' - ' +
            input('enter the airport name: ') + ',' +  input('  and the loggage band code : ')
            )
            airplane0 = input('enter the airplane code (B737): ')
            import airplane
            m = airplane.info(airplane0)
            capacity = str(m[0])
            flight1 = flight_char + ' - ' + airplane0 + ' - ' + capacity
            sure = input("  Are you sure? (y/n): ")
            if sure == 'y':
                f = Flight.flight_creating(flight1)
                #f.capacity_changing()
                flight = f.flight_items
                flight_list.append(flight)    
                flight_file = open(f'{flight_number}.txt','w')
                flight_file.close
                import flight_file
                flight_file.save(flight)
                print("\n  New Flight from {} to {} is created :D !".format(origin, destination))
                
            else:
                print("\n Allright .. Back to Menu ..!")
                continue
            
        elif choice == mgr_choice[1]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                search = [input("\nEnter the Origin: "),input("Enter the Destination: ")]
                import flights_search
                flights_search.searching(search, flight_list)       
                
        elif choice == mgr_choice[2]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                search = input("\n Enter a Flight Number: ")
                import flight_enter
                l = flight_enter.mgr_entering(search, flight_list)
                flag = int(l[0])
                f_char = str(l[1])
                index = int(l[2])
                if flag == 0:
                    print('\n oops .. There is no Flight with this flight number')
                else:
                    f = Flight.flight_creating(f_char)
                    while(True):
                        print('\n+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                        print('''
        1. Show informations of Flight
        2. Edit Flight
        3. Delete Flight
        4. Total Transaction of Flight
        5. Go Back
        ''')
                        mgr_search_choice = ('1','2','3','4','5')
                        choice = input("\nEnter your Choice: ")
                        if choice not in mgr_search_choice:
                            print("\n             WRONG INPUT!")
                        elif choice == mgr_search_choice[0]:
                            print('\n+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                            print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUMBER','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','ENTIRE CAPACITY'))
                            print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                            flight = f.flight_items 
                            for item in flight:
                                print("|",end='')
                                print("{0: ^20s}".format(item),end='')
                                if item == flight[-1]:
                                    print("|")
                                    print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                        elif choice == mgr_search_choice[1]:
                            edit_choice = ['1','2','3','4','5','6','7']
                            while(True):
                                print('\n+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                                print('''
                    \nWhich one do you want to edit?
                    1. origin
                    2. destination
                    3. date
                    4. hour
                    5. airport
                    6. airplane
                    7. Go back''')
                                choice = input('\nEnter your choice: ')
                                if choice not in edit_choice:
                                    print("\n             WRONG INPUT!")
                                elif choice == '1':
                                    edit = input("\nenter the new origin: ")
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        f.origin_changing(edit)
                                        print("\nnew origin replaced successfully ..!")
                                elif choice == '2':
                                    edit = input("\nenter the new destination: ")
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        f.destination_changing(edit)
                                        print("\nnew destination replaced successfully ..!")
                                elif choice == '3':
                                    edit = input('\nenter the new flight mounth : ') + '/' + input('  and the day: ')
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        f.date_changing(edit)
                                        print("\nnew date replace successfully ..!")
                                elif choice == '4':
                                    edit = input('\nenter the new flight hour : ') + ':' + input('  and the minute: ')
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        f.hour_changing(edit)
                                        print("\nnew hour replaced successfully ..!")
                                elif choice == '5':
                                    edit = input('\nenter the new airport name: ') + ' , ' +  input('  and the loggage band code : ')
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        f.airport_changing(edit)
                                        print("\nnew airport is entered successfully ..!")
                                elif choice == '6':
                                    edit1 = input('\nenter the new airplane code (B737): ')
                                    y = input("     Are you sure(y/n)? :")
                                    if y == 'y':
                                        import airplane
                                        edit2 = str(airplane.info(edit1)[0])
                                        f.airplane_changing(edit1)
                                        f.capacity_changing(edit2)
                                elif choice == '7':
                                    break
                                del flight_list[index] 
                                flight = f.flight_items
                                flight_list.append(flight)
                                import flight_file
                                flight_file.rewrite(flight_list)
                        elif choice == mgr_search_choice[2]:
                            y = input('\n Are you sure (y/n)?\n    NOTE: all the flight informations with passangers informations will be deleted ..! : ')
                            if y == 'y':
                                y = input('\n      Are you really sure (y/n)?\n    NOTE: There is no way Back !!!!!! : ')
                                if y == 'y':
                                    flag = 0
                                    index = 0
                                    for flight in flight_list:
                                        if flight[0] == search:
                                            flag = 1
                                        else:
                                            index += 1
                                    if flag == 1:
                                        del flight_list[index]
                                    import flight_file
                                    flight_file.rewrite(flight_list)
                                    import os
                                    os.remove('{}.txt'.format(search))
                                    print("\n Flight with entered flight number is deleted ..!")
                                    break
                                else:
                                    print("\n   Alright .. Go back ..")
                            else:
                                print("\n   Alright .. Go back ..")
       
                        elif choice == mgr_search_choice[3]:
                            pass
                            #x: len(tickets in this flight)
                            #total = 700 * x
                            #print('Boss! You earned {0:,d}$ from this Flight ..!'.format(total))
                        elif choice == mgr_search_choice[4]:
                            break
                    
        elif choice == mgr_choice[3]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                print('\n+=======================================================================================================================================================================+')
                print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUM','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','ENTIRE CAPACITY'))
                print('+=======================================================================================================================================================================+')
                for flight in flight_list:
                    for item in flight:
                        print("|",end='')
                        print("{0: ^20s}".format(item),end='')
                    print("|",end='\n')
                    print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')

        elif choice == mgr_choice[4]:
            print('\n\n       ',end = '')
            from time import sleep
            bye = " See You Soon .. Bye ! "
            for i in bye:
                print(i, end = '')
                sleep(0.5)
###########################################################################################
                                                                                            #######################################################################################################
    
if username == emp_info[0] and password == emp_info[1]: 
   ''' print('\n\n       ',end = '')
    from time import sleep
    hi = " Hello dear Employee .. Welcome ! "
    for i in hi:
        print(i, end = '')
        sleep(0.3)'''
   while(True):
        print("\n=========================================================================================================================================================================")
        print('''
        1. Show all Flights
        2. Search Flights
        3. Enter to a Flight
        4. Exit
        ''')
        emp_choice = ('1','2','3','4')
        choice = input('Enter your choice: ')
        if choice not in emp_choice:
            print('\n             WRONG INPUT !')
        elif choice == emp_choice[0]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                print('\n+=======================================================================================================================================================================+')
                print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUM','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','ENTIRE CAPACITY'))
                print('+=======================================================================================================================================================================+')
                for flight in flight_list:
                    for item in flight:
                        print("|",end='')
                        print("{0: ^20s}".format(item),end='')
                    print("|",end='\n')
                    print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
        elif choice == emp_choice[1]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                search = [input("\nEnter the Origin: "),input("Enter the Destination: ")]
                import flights_search
                flights_search.searching(search, flight_list)

        elif choice == emp_choice[2]:
            if flight_list == []:
                print("\nThere is no Flight in Flight List ..!")
            else:
                search = input("\n Enter a Flight Number: ")
                import flight_enter
                l = flight_enter.emp_entering(search, flight_list)
                flag = l[0]
                flight = l[1]
                airplane = flight[6]
                if flag == 0:
                    print('\n oops .. There is no Flight with this flight number')
                else:
                    while(True):
                        tickets_list = []
                        import tickets_file
                        tickets_list = tickets_file.load(search)
                        if tickets_list == []:
                            capacity = flight[7]
                        else:
                            capacity = int(flight[7]) - len(tickets_list)
                        print('\n+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                        print('''
                1. Create a new Ticket
                2. Show the Remaining Capacity
                3. Show all Tickets
                4. Enter to a Ticket
                5. Flight informations
                6. Go Back
                ''')
                        choice = ("\n Enter You Choice: ")
                        emp_choice = ('1','2','3','4','5','6')
                        choice = input("\nEnter your Choice: ")
                        if choice not in emp_choice:
                            print("\n             WRONG INPUT!")
                        elif choice == emp_choice[0]:                                               # Ticket Creating
                            name = input("\nEnter Passanger's  Name and Family: ")
                            nationalcode = input("\nEnter Passanger's NationalCode: ")
                            seatnumber = seat_number(seat_num, tickets_list) 
                            import datetime
                            now = datetime.datetime.now()
                            date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
                            time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                            datetime = '{}'.format(date) + ';' + '{}'.format(time)
                            participationcode = input("\nIf you have a ParticipationCode, Enter it:\n  If you don't have, so Enter just a \"-\" :  ")
                            import airplane
                            price = str(airplane.info(airplane)[1])
                            t = Ticket(name, nationalcode, seatnumber, datetime, price)
                            ticket = t.ticket_items()
                            tickets_list.append(ticket)
                            tickets_file = open(f'{name}.txt','w')
                            import passanger_file
                            passanger_file.save(flight, ticket, name)
                            tickets_file.close
                            import tickets_file
                            tickets_file.save(ticket, search)
                            #new_capacity = rem_capacity(capacity)
                            '''if participationcode != '-':
                                with open('r','{}.txt'.format(participationcode)) as participation_file:
                                    particip_list = participation_file.readlines()
                                    participation_file.close
                                each_particip_list = []
                                ticket.append(participationcode)
                                each_particip_list.append(ticket)
                                with open('w','{}.txt'.format(participationcode)) as each_participation_file:
                                    each_participation_file.write(each_particip_list + '\n')
                                    each_participation_file.close'''
                            print("\n New Ticket created successfully and added to Tickets List :D ")
                        elif choice == emp_choice[1]:
                            if tickets_list == []:
                                print('\n   No Tickets are reserved yet  .. !!!')
                            else:
                                print('\n      The remaining Capacity of this Flight is "{}"'.format(capacity))
                        elif choice == emp_choice[2]:
                            if tickets_list == []:
                                print("\n    There is no Ticket in Ticket List ..!")
                            else:
                                print('\n+========================================================================================================+')
                                print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|".format('FULLNAME','NATIONALCODE','SEATNUMBER','DATE - TIME','PRICE'))
                                print('+========================================================================================================+')
                                for ticket in tickets_list:
                                    for item in ticket:
                                        print("|",end='')
                                        print("{0: ^20s}".format(item),end='')
                                    print("|",end='\n')
                                    print('+--------------------------------------------------------------------------------------------------------+')
                        elif choice == emp_choice[3]:
                            if tickets_list == []:
                                print('\n oop .. There is no Ticket in Ticekt List ..!')
                            else:
                                username = input("\n     USERNAME: ")
                                password = input("\n PASSWORD: ")
                                if username != mgr_info[0] and password != mgr_info[1]:
                                    print('\n Sorry .. You Can not Enter .. Just Manager Can Enter to this Part!')
                                else:
                                    search1 = input("\nEnter Passanger's Name and Family or NationalCode: ")
                                    mark = 0
                                    for i in range(48, 58):
                                        if ord(search1[0]) == i:
                                            mark = 1
                                    if mark == 0:
                                        ind = 0
                                        fl = 0
                                        for tic in tickets_list:
                                            if tic[0] == search1:
                                                fl = 1
                                                ticket1 = tic
                                                search_name = ticket1[0]
                                                break
                                            else:
                                                ind += 1
                                        flag = fl
                                        index = ind
                                    else:
                                        ind = 0
                                        fl = 0
                                        for tic in tickets_list:
                                            if tic[1] == search1:
                                                fl = 1
                                                ticket1 = tic
                                                search_name = ticket1[0]
                                                break
                                            else:
                                                ind += 1
                                        flag = fl
                                        index = ind
                                        
                                    if flag == 0:
                                        print("\n There is no Ticket with entered name in Tickets List ..!")
                                    else:
                                        name, nationalcode, seatnumber, datetime, price = ticket1[0], ticket1[1], ticket1[2], ticket1[3], ticket1[4]
                                        t = Ticket(name, nationalcode, seatnumber, datetime, price)
                                        ticket = t.ticket_items()
                                        while(True):
                                            print('''
                        1. Show Ticket
                        2. Edit Ticket
                        3. Delete Ticket
                        4. Go Back
                        ''')
                                            choice = input("\n Enter your choice: ")
                                            emp_choice = ('1','2','3','4')
                                            if choice not in emp_choice:
                                                print("\n                   @WRONG INPUT!@")
                                            elif choice == emp_choice[0]:
                                                import ticket_show
                                                ticket_show.showing(ticket, flight)
                                            elif choice == emp_choice[1]:
                                                while(True):
                                                    print('''
                                1. Name
                                2. NationalCode
                                3. SeatNumber
                                4. Go Back
                                ''')
                                                    choice = input("\n Which Item do you want to Edit?: ")
                                                    emp_choice = ('1','2','3','4')
                                                    if choice not in emp_choice:
                                                        print("\n              @WRONG INPUT!@ .. Go Back!")
                                                    elif choice == emp_choice[0]:
                                                        new_name = input("\n Enter new Name and Family: ")
                                                        y = input("\n     Are you sure (y/n)? ")
                                                        if y == 'y':
                                                            name1 = t.changename(new_name)
                                                            t = Ticket(name1, ticket[1], ticket[2], ticket[3], ticket[4])
                                                            import os
                                                            os.rename('{}.txt'.format(search_name), '{}.txt'.format(new_name))
                                                            print("\n New Name is Replaced successfully ..!")
                                                    elif choice == emp_choice[1]:
                                                        new_nationalcode = input("\n Enter new NationalCode: ")
                                                        y = input("\n     Are you sure (y/n)? ")
                                                        if y == 'y':
                                                            natonalcode1 = t.changenationalcode(new_nationalcode)
                                                            t = Ticket(ticket[0], nationalcode1, ticket[2], ticket[3], ticket[4])
                                                            print("\n New NationalCode is Replaced successfully ..!")
                                                    elif choice == emp_choice[2]:
                                                        new_seatnumber = input("\n Enter new Seat Number: ")
                                                        y = input("\n     Are you sure (y/n)? ")
                                                        if y == 'y':
                                                            for item in tikcets_list:
                                                                if item[3] == new_seatnumber:
                                                                    item[3] = seatnumber
                                                                    seatnumber1 = t.changeseatnumber(new_seatnumber)
                                                                    t = Ticket(ticket[0], ticket[1], seatnumber1, ticket[3], ticket[4])
                                                            else:
                                                                seatnumber1 = t.changeseatnumber(new_seatnumber)
                                                                t = Ticket(ticket[0], ticket[1], seatnumber1, ticket[3], ticket[4])
                                                            print("\n New NationalCode is Replaced successfully ..!")
                                                        
                                                        del tickets_list[index]
                                                        ticket = t.ticket_items()
                                                        search = ticket[0]
                                                        tickets_list.append(ticket)
                                                        import tickets_file
                                                        tickets_file.rewrite(search, tickets_list)
                                                    elif choice == emp_choice[3]:
                                                        break
                                            elif choice == emp_choice[2]:
                                                y = input('\n Are you sure (y/n)?\n    NOTE: all the Tickets will be deleted ..! : ')
                                                if y == 'y':
                                                    y = input('\n      Are you really sure (y/n)?\n    NOTE: There is no way Back !!!!!! : ')
                                                    if y == 'y':
                                                        del tickets_list[index]
                                                        import tickets_file
                                                        tickets_file.rewrite(search, tickets_list)
                                                        import os
                                                        os.remove('{}.txt'.format(search_name))
                                                        print("\n Flight with entered flight number is deleted ..!")
                                                        break
                                                    else:
                                                        print("\n   Allright .. Go back ..")
                                                else:
                                                    print("\n   Allright .. Go back ..")
                                            elif choice == emp_choice[3]:
                                                break
                                        
                        elif choice == emp_choice[4]:
                            print('\n+=======================================================================================================================================================================+')
                            print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUM','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','CAPACITY'))
                            print('+=======================================================================================================================================================================+')
                            for item in flight:
                                print("|",end='')
                                print("{0: ^20s}".format(item),end='')
                                if item == flight[-2]:
                                    print("|",end='')
                                    break
                            print("{0: ^20s}|".format(str(capacity)))
                            print('+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
                        elif choice == emp_choice[5]:
                            break
        elif choice == emp_choice[3]:
            from time import sleep
            bye = " See You Soon "
            for i in bye:
                print(i, end = '')
                sleep(0.5) 
            break
