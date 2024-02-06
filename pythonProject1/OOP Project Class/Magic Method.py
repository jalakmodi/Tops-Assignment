class Point:
    def __init__(self,x,y):
        print("init Called")
        print("*"*20)
        self.x=x
        self.y=y

    def __str__(self):
        print("Str called")
        print("*" * 20)
        return "({}, {})".format(self.x,self.y)

    def __add__(self, obj):
        print("add called")
        print("*" * 20)
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)



p1=Point(10,20)
print(p1)
print("*" * 20)
p2=Point(30,50)
print(p2)
print("*" * 40)
print(" Addition Of Object : ",p1+p2)


