# What is OOP
     Oriented Programming


a way of formatting code in the form of objects to keep things visually simple.

we can keep certain variables and commands in a seperate document in blocks called Classes which can be accessed and called on from another document using

OOP relies on 4 things
#    Encapsulation  
         all properties and methods in the object are kept private and seperate from other objects.

         fundamental attributes of our car can’t be changed or modified by other objects.
#    Abstraction 
        Code calling the method dosn't need to know HOW it works. Just needs to know that it works.
#    Inheritance  
        we can reuse attributes for other objects
#    Polymorphism. 
    a way to use an object exactly like its parent but keeping its own methods as they are.



``` python
    import Class from Document.py
```


``` python

    class Car():
        def __init__(self, make,model,year,colour,hp):
            self.make = make
            self.model = model
            self.year = year
            self.colour = colour
            self.hp = hp

car_1 = Car("Ford", "Mustang", 1969, "Grey", 500)
car_2 = Car("Hyundai","i20N",2022,"Blue",125)
car_3 = Car("Chrysler", "PT Cruiser", 2004, "Black", 100)

print(car_1.make)

```