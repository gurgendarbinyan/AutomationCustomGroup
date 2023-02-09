#class people():
 #   name = "John"
  #  age = 33
#    heigh = 180.5

  #  def sing(self):
 #       print("lya lya")

#person1 = people()
#print(type(person1))
#print(type(person1).name)
#class int():
#   pass
model = "BMW"
year = 1997
millage = 10000
class Car():
    def __init__(self, model, year, millage):
        self.model = model
        self.year = year
        self. millage = millage
    def info(self):
        print("",self.model,'\n',self.year,'\n', self.millage)

car = Car(model, year, millage)
car.info()




