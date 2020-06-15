class Passenger:
    def __init__(self, name):
        self.name = name
        self.flight_numbers = []

    def has_flight(self, flight_number):
        return flight_number.upper() in self.flight_numbers

    def add_flight(self, flight_number):
        flight = flight_number.upper()
        if not self.has_flight(flight):
            self.flight_numbers.append(flight)
            
