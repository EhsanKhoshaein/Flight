#if username == emp_info[0] and password == emp_info[1]:
#    print('\n              @ HELLO  MR. EMPLOYEE  ..  YOU  ARE  WELCOME! @')

    
class Ticket(Flight):
    def __init__(self, name, nationalcode, datetime, seatnumber, price, participationcode):
        self.__name = name
        self.__nationalcode = nationalcode
        self.__seatnumber = seatnumber
        self.datetime = datetime
        self.price = price
        if participation != '0':
            self.participationcode = participationcode
    @property       
    def ticket_items(self):
        ticket_items = []
        ticket_items.append(self.name)
        ticket_items.append(self.nationalcode)
        ticket_items.append(self.datetime)
        ticket_items.append(self.seatnumber)
        ticket_items.append(self.price)
        ticket_items.append(self.participationcode)
        return ticket_items
    def name_changing(self, edit):
        self.__name = edit
    def nationalcode_changing(self, edit):
        self.__nationalcode = edit
    def seatnumber_changing(self, edit):
        self.__seatnumber = edit
    def capacity_changing(self):
        self.capacity = int(self.capacity) - 1
        return self.capacity
    def __str__(self):
        return '''
        Passanger informations:
        \nFullname: {}
        \nNationalCode: {}
        \nDatetime : {}
        \nSeatNumber: {}
        \nTicketPrice: {}
        '''.format(self.name, self,nationalcode, self.datetime, self.seatnumber, self.price)
    def __repr__(self):
        return '''
        Ticket informations:
        \nParticipationCode: {}
        \nFullname: {}
        \nNationalCode: {}
        \nDatetime : {}
        \nSeatNumber: {}
        \nTicketPrice: {}
        
        '''.format(self.participationcodem ,self.name, self,nationalcode, self.datetime, self.seatnumber, self.price)
      
    @own_ticket.deleter
    def own_ticket(self):
        self.__name = None
        self.__nationalcode = None
        self.__seatnumber = None
        self.datetime = None
        self.price = None
        print('\n   Ticket is deleted!')
seat_num = []
i = 65
while(i<85):
    char = chr(i)
    for j in range(1,21):
        dig = j
        a = str(char) + str(dig)
        seat_num.append(a)
    i += 1
def seat_num(seat_num, tickets_list):
    global seatnumber
    if tickets_list == []:
        seatnumber = seat_num[0]
        return seatnumber
    else:
        seatnumber =  str(int(tickets_list[-1][3])+1)
        return seatnumber
    
    

while(True):
    print('''
    1. Search Flights
    2. Enter to a Flight
    3. Exit
    ''')
    emp_choice = ('1','2','3')
    choice = input('Enter your choice: ')
    if choice not in emp_choice:
        print('\n             WRONG INPUT !')
    elif choice == emp_choice[0]:
        if flight_list == []:
            print("\nThere is no Flight in Flight List ..!")
        else:
            search = [input("\nEnter the Origin: "),input("Enter the Destination: ")]
            import flights_search
            flights_search.searching(search, flight_list)

    elif choice == emp_choice[1]:
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
                    tickets = []
                    import tickets_flie
                    tickets_list = tickets_file.load(search)
                    print('''
            1. Create a new Ticket
            2. Show the Remaining Capacity
            3. Show all Tickets
            4. Enter to a Ticket
            5. Flight informations
            6. Go Back
            ''')
                    choice = ("\n Enter You Choice: ")
                    emp_choice = ('1','2','3','4','5')
                    choice = input("\nEnter your Choice: ")
                    if choice not in emp_choice:
                        print("\n             WRONG INPUT!")
                    
                        
                    elif choice == emp_choice[0]:                                               # Ticket Creating
                        name = input("\nEnter Passanger's Name and Family: ")
                        nationalcode = input("\nEnter Passanger's NationalCode: ")
                        import datetime
                        now = datetime.datetime.now()
                        date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
                        time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                        datetime = '{}'.format(date) + ';' + '{}'.format(time)
                        seatnumber = seat_num(tickets_list)    
                        participationcode = input("\n  If you have a ParticipationCode, Enter it:\n  If you don't have, so Enter just a \"-\" ")
                        if participationcode == '-':
                            participationcode = '0'
                        import airplane
                        m = airplane.info(airplane)
                        price = m[1]
                        t = Ticket(name, nationalcode, datetime, seatnumber, price, participationcode)
                        ticket = t.ticket_items
                        tikcets_list.append(ticket)
                        tickets_file = open(f'{name}.txt','w')
                        tickets_file.close
                        import tickets_file
                        tickets_file.save(ticket, search)
                    elif choice == emp_choice[1]:
                        for ticket in tickets_list:
                            remaining_capacity = f.changing_capacity()
                        print('\n The remaining Capacity of this Flight is {}'.format(remaining_capacity))
                    elif choice == emp_choice[2]:
                        if tickets_list == []:
                            print("\nThere is no Ticket in Ticket List ..!")
                        else:
                            print('\n+=======================================================================================================================================================================+')
                            print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|".format('FULLNAME','NATIONALCODE','DATE - TIME','SEATNUMBER','PRICE'))
                            print('+=======================================================================================================================================================================+')
                            for ticket in ticket_list:
                                for item in flight:
                                    print("|",end='')
                                    print("{0: ^20s}".format(item),end='')
                                    print("|",end='\n')
                                print('+--------------------------------------+')
                    elif choice == emp_choice[3]:
                        pass
                    elif choice == emp_choice[4]:
                        print('\n+=======================================================================================================================================================================+')
                        print("|{0: ^20}|{1: ^20}|{2: ^20}|{3: ^20}|{4: ^20}|{5: ^20}|{6: ^20}|{7: ^20}|".format('FLIGHT NUM','ORIGIN','DESTINATION','DATE','HOUR','AIRPORT','AIRPLANE','CAPACITY'))
                        print('+=======================================================================================================================================================================+')
                        for item in flight:
                            print("|",end='')
                            print("{0: ^20s}".format(item),end='')
                            print("|",end='\n')
                        print('+-------------------------------------------------------------------------------------------------------------------------------------+')
                    elif choice == emp_choice[5]:
                        pass
    
#path = 'C:\\Users\\Username\\Path\\To\\File'

#with open(path, 'w') as f:
    #f.write(data)
#import os
#f = open(r'C:\Users\Directory\sample.txt')
