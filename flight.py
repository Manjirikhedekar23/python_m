# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details




class Flight():
    def __init__(self,in_name,in_arrival,in_dep,in_time,in_flightno,in_seatno):
        self.name=in_name
        self.arrival=in_arrival
        self.departure=in_dep
        self.time=in_time
        self.flightnumber=in_flightno
        self.seatnumber=in_seatno
        
    def display_instances(self):
        print(f"Name of passenger : {self.name}")
        print(f"Arrival : {self.arrival}")
        print(f"Departure : {self.departure}")
        print(f"Time : {self.time}")
        print(f"Flight number : {self.flightnumber}")
        print(f"Seat number : {self.seatnumber}")
        print(' ')
        
def main():
    passenger1=Flight("Manjiri","Sri Lanka","Yavatmal","4:30","45682","30E")
    passenger1.display_instances()
    print(' ')
    passenger2=Flight("Shrusti","Yavatmal","Pakistan","13:00","32325","6Y")
    passenger2.display_instances()
        
main()
    