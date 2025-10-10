# Exercise

# User
# Make a class called `User`. Create the following attributes:
# first_name and last_name, username, email, and location.
# Make a method called describe_user() that prints a summary of the user's information.
# Make another method called greet_user() that prints a personalized greeting to the user.


class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"""Name: {self.first_name} {self.last_name}
Username: {self.username}
Email: {self.email}
Location: {self.location}""")

    def greet_user(self):
        print(f"Welcome back {self.username}!")