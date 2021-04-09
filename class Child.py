# class Child:
#     #constructor
#     def __init__(self,name):
#         __self.name = name


#     #get name
#     def getName(self):
#         return self.name

#     #to check if this returns whatever
    
# class Student(Child):
#     pass



class Vehicle:
    _brand = 'Ford'

    def honk(self):
        print("Tut tut")

class Car(Vehicle):
    __modelName = 'Mustang'

myvehicle = vehilce()
mycar = Car()
print(myvehicle._brand)