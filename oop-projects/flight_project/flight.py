class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def is_full(self):
        return len(self.passengers) == self.capacity

    def board_passenger(self, passenger):
        if (not self.is_full()) and passenger.has_flight(self.flight_number):
            self.passengers.append(passenger)

    def list_passengers(self):
        return self.passengers
