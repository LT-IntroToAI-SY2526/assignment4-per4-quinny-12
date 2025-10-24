# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A simple Dog class to learn OOP concepts

    Attributes:
        breed - the breed of the dog
        fur_color - the fur color of the dog
        name - the name of the dog
        age - the age of the dog
    """
 
    def __init__(self, breed = "dog", fur_color = "black", name = "no name", age = 1):
        """Initialize a new Dog with breed, fur_color, name and age"""
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def __str__(self):
        """String representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"

    def bark(self):
        return f"{self.name} says: Woof, Woof!!"
    
    def birthday(self):
        """celebrate the dog's birthday"""
        self.age += 1
        print(f"{self.name} is celebrating their {self.age} birthday")

    def dye_fur(self, new_color):
        """change the fur_color of the dog"""
        old_color = self.fur_color
        self.fur_color = new_color
        print(f"{self.name} changed their fur color from {old_color} to {self.fur_color}")

if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "logan", 9)
    aidan_dog = Dog("lab pitt mix", "grey", "cubbie", 9)
    q_imaginary_dog = Dog("border collie", "brown", "wrigley", 1)
    default_dog = Dog()
    matthew_dog = Dog(breed = "labrador", name = "bella", age = 1)

    print(berg_dog)
    print(aidan_dog)
    print(q_imaginary_dog)
    print(default_dog)

    print()

    print(aidan_dog.bark())
    matthew_dog.birthday()
    q_imaginary_dog.dye_fur("blue")
    print(q_imaginary_dog)