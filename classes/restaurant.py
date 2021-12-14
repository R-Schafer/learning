# try it yourself

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        description = f"{self.restaurant_name} {self.cuisine_type}"
        return description.title()

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def customers_served(self):
        print(f"We served {self.number_served} customers.")

    def update_customers(self, customers):
        self.number_served = customers

    def increment_customers(self, served):
        self.number_served += served

# my_restaurant = Restaurant("FOODZ", "comfort food")
# print(f"{my_restaurant.restaurant_name}")
# print(f"{my_restaurant.cuisine_type}")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant() 

# your_rest = Restaurant("Poo Thai", "Thai Food")
# your_rest.describe_restaurant()

# other_rest = Restaurant("Burger King", "Burgers")
# other_rest.describe_restaurant()
# other_rest.update_customers(250)
# other_rest.customers_served()
# other_rest.increment_customers(100)
# other_rest.customers_served()

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def name_flavors(self):
        print(f"Are flavors are: {', '.join(self.flavors)}")

my_ice_cream = IceCreamStand("Andy's", "cold treats")
print(my_ice_cream.describe_restaurant())
my_ice_cream.name_flavors()


    