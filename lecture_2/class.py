# class Point():
#     #magic method
#     def __init__(self, inputX, inputY):
#         self.x = inputX
#         self.y = inputY

# p = Point(8, 9)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['Mohammed', 'ali', 'Hannen', "SubZero"]

for person in people:
    if flight.add_passenger(person):
        print(f'Added {person} to flight successfuly')
    else:
        print(f'No available seats for {person}')
