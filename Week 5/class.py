

# Base class: Superhero
class Superhero:
    def __init__(self, name, alias, power, city):
        self.name = name
        self.alias = alias
        self.power = power
        self.city = city
        self._health = 100  # Encapsulated attribute (protected)
    
    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}. I protect {self.city}!")

    def use_power(self):
        print(f"{self.alias} uses {self.power}!")

    def take_damage(self, amount):
        self._health -= amount
        print(f"{self.alias} took {amount} damage! Health is now {self._health}.")

    def get_health(self):
        return self._health

    def heal(self, amount):
        self._health += amount
        print(f"{self.alias} heals for {amount}. Health is now {self._health}.")

# Derived class: Spiderman (inherits from Superhero)
class Spiderman(Superhero):
    def __init__(self, name="Peter Parker", city="New York"):
        super().__init__(name, "Spiderman", "web-slinging and agility", city)

    # Polymorphism: override use_power
    def use_power(self):
        print(f"{self.alias} swings through the city using webs and dodges enemies with agility!")

    # New method specific to Spiderman
    def shoot_web(self):
        print(f"{self.alias} shoots a web at the enemy!")

# Create Spiderman object
spidey = Spiderman()

# Use methods
spidey.introduce()
spidey.use_power()
spidey.take_damage(30)
spidey.heal(20)
spidey.shoot_web()
