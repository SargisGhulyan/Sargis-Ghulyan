class Bird:
    def __init__(self, name, species, age, wing_span, color):
        self.name = name
        self.species = species
        self.age = age
        self.wing_span = wing_span  # Wing span in centimeters
        self.color = color  # New color attribute
        self.is_fed = False
 
    def feed(self):
        self.is_fed = True
        print(f"{self.name} the {self.species} has been fed.")
 
    def __str__(self):
        fed_status = "fed" if self.is_fed else "hungry"
        return (f"{self.name} ({self.species}, {self.age} years old, "
                f"{self.wing_span} cm wing span, color: {self.color}) is {fed_status}.")
 
 class Enclosure:
    def __init__(self, name, size):
        self.name = name
        self.size = size  # Size in square meters
        self.animals = []
        self.cleanliness = 100  # Starts clean (percentage)
 
    def add_animal(self, animal):
        if self.cleanliness > 50:
            self.animals.append(animal)
            print(f"{animal.name} has been added to {self.name}.")
        else:
            print(f"Cannot add {animal.name}. {self.name} needs cleaning first!")
 
    def clean_enclosure(self):
        self.cleanliness = 100
        print(f"The enclosure {self.name} has been cleaned.")
 
    def feed_animals(self):
        for animal in self.animals:
            animal.feed()
 
    def __str__(self):
        return (f"Enclosure {self.name}: {len(self.animals)} animal(s), "
                f"cleanliness {self.cleanliness}%.")
 
 class Zoo:
    def __init__(self, name):
        self.name = name
        self.enclosures = []
 
    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)
 
    def daily_report(self):
        print(f"Zoo: {self.name} - Daily Report")
        for enclosure in self.enclosures:
            print(enclosure)
            for animal in enclosure.animals:
                print(f"  - {animal}")
 
    def __str__(self):
        return f"Zoo {self.name}: {len(self.enclosures)} enclosures."
 
if __name__ == "__main__":
    zoo = Zoo("Wildlife Park")
    bird_enclosure = Enclosure("Bird Sanctuary", 200)
 
    # Adding color attribute to the Bird instances
    parrot = Bird("Polly", "Parrot", 3, 25, "Green")
    eagle = Bird("Eddie", "Eagle", 5, 180, "Brown")
 
    bird_enclosure.add_animal(parrot)
    bird_enclosure.add_animal(eagle)
 
    zoo.add_enclosure(bird_enclosure)


    print("Enclosures in the zoo:")
    for enclosure in zoo.enclosures:
        print(enclosure)

    zoo.daily_report()
