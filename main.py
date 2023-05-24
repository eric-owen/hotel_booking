import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        print(card_data)
        if card_data in df_cards:
            return True
        else:
            return False


print(df)
hotel_ID = input("enter the id of hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    credit_card = CreditCard(number="1234123412341234")
    if credit_card.validate(expiration="01/29", cvc="123", holder="John Smith"):
        hotel.book()
        name = input("enter your name: ")
        reservation_ticket = ReservationTicket(cust_name=name, hotel_obj=hotel)
        print(reservation_ticket.generate())
    else:
        print("something went wrong with payment")
else:
    print("hotel is not available")
