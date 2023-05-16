import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        pass
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, cust_name, hotel_obj):
        self.cust_name = cust_name
        self.hotel = hotel_obj
    def generate(self):
        content = f"""
        Booking data:
        Name: {self.cust_name}
        hotel: {self.hotel.name}
        """
        return content

print(df)
hotel_ID = input("enter the id of hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("enter your name: ")
    reservation_ticket = ReservationTicket(cust_name=name, hotel_obj=hotel)
    print(reservation_ticket.generate())
else:
    print("hotel is not available")