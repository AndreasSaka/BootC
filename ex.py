import inspect

class Sample:
    """this is a sample class"""
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def printing(self):
        print('This is',self.name, self.surname)

diana = Sample('Diana','Joobs')
diana.printing()
print(inspect.getdoc(Sample))
print(diana.__doc__)
