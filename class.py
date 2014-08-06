class Person:
    def __init__(self, name, initial_health):
        self.name = name;
        self.health = initial_health
        self.inventory = []
    
    def __str__(self):
        s = 'Name:' + self.name + 'Initial_health:' + str(self.health)
        return s
    def increate(self, number):
        self.health += number

p = Person("John", 100)
print p
        
