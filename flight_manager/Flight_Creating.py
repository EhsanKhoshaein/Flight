class Flight:
    def __init__(self, number, origin, destination, date, hour, airplane, airport):
        self.number = number
        self.origin = origin
        self.destination = destination
        self.date = date
        self.hour = hour
        self.airplane = airplane
        self.airport = airport
        
    @classmethod
    def object_creating(cls, flight):
        number, origin, destination, date, hour, airplane, airport   = flight.split(' - ')
        return cls(number, origin, destination, date, hour, airplane, airport)
'''flight1 = (
            input('\nenter the origin: ') + ' - '+
            input('enter the destination: ') + ' - ' +
            input('enter the flight date (08/31): ') + ' - ' +
            input('enter the flight hour (12:35): ') + ' - ' +
            input('enter the airplane code (K202): ') + ' - ' +
            input('enter the airport and loggage band code (Imam,B12): ')
            )
f = Flight.object_creating(flight1)'''

