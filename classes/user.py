class User:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.full_name = first + " " + last
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.full_name}")

    def greet_user(self):
        print(f"Greetings, {self.full_name}")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print(f"There have been {self.login_attempts} attempts to login.")

    def reset_login_attempts(self):
        self.reset_login_attempts = 0
        print(f"Resetting - there have been {self.reset_login_attempts} attempts to login.")
        
user_1 = User("Rainey", "Schafer")
user_2 = User("Charlie", "Johnson")

# user_1.greet_user()
# user_2.describe_user()
# user_1.increment_login_attempts(5)
# user_1.reset_login_attempts()
    
class Admin(User):

    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"The Admin can do the following: {', '.join(self.privileges)}")

    
admin1 = Admin("Boss", "Man")
admin1.describe_user()
admin1.show_privileges()