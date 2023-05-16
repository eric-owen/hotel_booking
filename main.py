import pandas

df = pandas.read_csv("hotels.csv")
class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass
    def available(self):
        pass

class ReservationTicket:
    def __init__(self, cust_name, hotel_obj):
        pass
    def generate(self):
        pass

print(df)
id = input("enter the id of hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("senter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    ;print(reservation_ticket.generate())
else:
    print("hotel is not available")