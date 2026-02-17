class Flight:
    def __init__ (self, flight_number, source, destination):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.class_types = {}
        self.food_menu = {}
        self.luggage_rates = {}
        self.passengers =[]

    def add_class_type(self, class_name, price, seats):
        self.class_types [class_name] = {"price": price, "seats": seats}

    def add_food_item(self, item, price):
        self.food_menu [item] = price

    def delete_food_item(self, item):
        if item in self.food_menu:
            del self.food_menu[item]
            print (f" (item) deleted from the food menu.")
        else:
            print (f"(item) not found in the food menu.")

    def revise_food_item(self, item, price):
        if item in self.food_menu:
            self.food_menu [item] = price
            print (f"{item} price updated to ${price}.")
        else:
            print (f"{item} not found in the food menu.")

    def show_food_menu (self):
        print("Food Menu:")
        for item, price in self.food_menu.items():
            print (f"{item}: ${price}")

    def add_luggage_charge(self, luggage_type, price):
        self.luggage_rates[luggage_type] = price

    def show_luggage_rates (self):
        print("Luggage Rates:")
        for luggage_type, price in self.luggage_rates.items():
            print (f"{luggage_type}: ${price}")

    def show_available_seats (self):
        print("Available Class Types:")
        for class_name, details in self.class_types.items():
            print (f"{class_name}: {details['seats']} seats - ${details['price']} per seat")

    def book_seat(self, passenger, class_name, num_seats):
        if class_name in self.class_types and num_seats <= self.class_types[class_name]["seats"]:
            self.class_types [class_name] ["seats"] = num_seats
            passenger.selected_class =class_name
            passenger.selected_seats = num_seats
            return self.class_types[class_name] ["price"] * num_seats
        else:
            return 0

    def add_passenger (self, passenger):
        self.passengers.append(passenger)

class Passenger:
    def __init__(self, name):
        self.name = name
        self.selected_class = None
        self.selected_seats = 0
        self.luggage_type = None
        self.food_order = []

    def calculate_seat_cost(self, flight):
        if self.selected_class in flight.class_types:
            if isinstance(self.selected_seats, int) and self.selected_seats > 0:
                class_price = flight.class_types [self.selected_class] ["price"]
                total_cost = class_price * self.selected_seats
                return total_cost
            else:
                return "Error: Number of seats must be a positive integer."
        else:
            return "Error: Selected class is not valid for this flight."

    def calculate_luggage_cost(self, flight):
        return flight.luggage_rates.get(self.luggage_type, 0)

    def calculate_food_cost (self, flight):
        return sum(flight.food_menu[item] for item in self.food_order)

    def calculate_total_price(self, flight):
        seat_cost = self.calculate_seat_cost(flight)
        luggage_cost = self.calculate_luggage_cost(flight)
        food_cost = self.calculate_food_cost(flight)
        return seat_cost + luggage_cost + food_cost

    if __name__ == "__main__":
        flight = Flight("AA101", "New York", "Los Angeles")

        while True:
            print("\nFlight Reservation System Menu:")
            print("1. Add Class Type")
            print("2. Add Food Item")
            print("3. Delete Food Item")
            print("4. Revise Food Item Price")
            print("5. Show Food Menu")
            print("6. Add Luggage Charge")
            print("7. Show Luggage Rates")
            print("8. Show Available Seats")
            print("9. Book a Seat")
            print("10. Add Passenger")
            print("11. Exit")

            choice = input("Enter your choice: ")
    
            if choice == "1":
                class_name = input("Enter class name: ")
                price = float(input("Enter price per seat: "))
                seats = int(input("Enter number of seats: "))
                flight.add_class_type(class_name, price, seats)
                print (f"{class_name} class added.")
            elif choice == "2":
                food_item = input("Enter food item: ")
                price = float(input("Enter the price: "))
                flight.add_food_item(food_item, price)
                print (f"{food_item} added to the food menu.")
            elif choice == "3":
                food_item = input("Enter food item to delete: ")
                flight.delete_food_item(food_item)
            elif choice == "4":
                food_item = input("Enter food item to revise : ")
                price = float(input("Enter the new price : "))
                flight.revise_food_item(food_item, price)
            elif choice == "5":
                flight.show_food_menu()
            elif choice == "6":
                luggage_type = input("Enter luggage type: ")
                price = float(input("Enter the price : "))
                flight.add_luggage_charge(luggage_type, price)
                print(f"Luggage charge for {luggage_type} added.")
            elif choice == "7":
                flight.show_luggage_rates()
            elif choice == "8":
                flight.show_available_seats()
            elif choice =="9":
                passenger_name = input("Enter passenger name: ")
                class_name = input("Enter class name: ")
                num_seats = int(input("Enter the number of seats to book: "))
                passenger = Passenger(passenger_name)
                cost = flight.book_seat(passenger, class_name, num_seats)
                if cost > 0:
                    print(f"Successfully booked {num_seats} seat(s) in {class_name}. Total cost: ${cost}")
                    luggage_type = input("Enter luggage type: ")
                    food_order = input("Enter food items (comma-separated): ").split(',')
                    passenger.luggage_type = luggage_type
                    passenger.food_order = [item.strip() for item in food_order]
                else:
                    print("Seat booking failed.")
            elif choice == "10":
                passenger_name = input("Enter passenger name: ")
                passenger = Passenger(passenger_name)
                flight.add_passenger(passenger)
                print(f"Passenger {passenger_name} added.")
            
            elif choice == "11":
                break
            else:
                print("Invalid choice. Please try again.")  


