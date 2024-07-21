class Flight:
    def __init__(self, origin, destination, date, hour, airplane, airport):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.hour = hour
        self.airplane = airplane
        self.airport = airport

    def flight_info(self):
        return '''
                Origin: {}
                Destination: {}
                Date: {}
                Hour: {}
                Airplane: {}
                Airport: {}
                '''.format(self.origin, self.destination, self.date, self.hour, self.airplane, self.airport)
        
    @classmethod
    def flight_creating(cls, flight):
        origin, destination, date, hour, airplane, airport   = flight.split(' - ')
        return cls(origin, destination, date, hour, airplane, airport)
f = (
            input('\nenter the origin: ') + ' - '+
            input('enter the destination: ') + ' - ' +
            input('enter the flight mounth : ') + '/' + input('  and the day: ') + ' - ' +
            input('enter the flight hour : ') + ':' + input('  and the minute: ') + ' - ' +
            input('enter the airplane code (K202): ') + ' - ' +
            input('enter the airport name: ') + ' , ' +  input('  and the loggage band code : ')
            )

flight1 = Flight.flight_creating(f)

#mesali digar az flight sazi: flight2 = Flight.flight_creating(f)    
        
class Manager(Flight):
    def __init__(self, flights = 0):
        if flights == 0:
            self.flights = []
        else:
            self.flights = flights
    def add_flight(self, flight):
        if flight not in self.flights:
            self.flights.append(flight)
            
    def remove_flight(self, flight):
        if flight in self.flights:
            self.flights.remove(flight)
    def flights_charter(self):
        for flight in self.flights:
            print('----->', flight.flight_info())
mgr = Manager([flight1])
#mgr = Manager.add_flight(flight1)
mgr.remove_flight([flight1])
mgr.flights_charter()




'''
# isinstance --> to see if an object is from class or sub or not
print(isinstance(mgr_1, Manager))  #--> True
print(isinstance(mgr_1, Employee)) #--> True
print(isinstance(mgr_1, Developer))#--> False
# sublcass --> to see if a class is subclass or not
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
'''
