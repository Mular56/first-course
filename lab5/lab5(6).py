class Venicle():
    def method(self, x,y,c):
        self.x=x
        self.y=y
        self.c=c
        print(self.x, self.y, self.c)
class AirCraft(Venicle):
    def child_method1(self,x,y):
        self.x=x
        self.y=y
        print(self.x, self.y)
class Ship(Venicle):
    def child_method2(self,y,c):
        self.y=y
        self.c=c
        print(self.y, self.c)

a=AirCraft()
a.child_method1("40 метров", "150 пассажиров")
b=Ship()
b.child_method2("Париж", "100 пассажиров")