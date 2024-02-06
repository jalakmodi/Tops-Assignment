#********************Making Class For Car*****************************
class Vehicle:
    def getA(self):
        pass
    def putA(self):
        print("\n Below Company Vehicle Available ")
        print("*"*60)
class maruti(Vehicle):
    def getB(self,mcname):
        self.mcname=mcname
    def putB(self):
        print(self.mcname,"Car Belongs To Maruti Company.")

class hyundai(Vehicle):
    def getC(self,hcname):
        self.hcname=hcname
    def putC(self):
        print(self.hcname,"Car Belongs To Hyundai Company.")

class bench(hyundai,maruti):
    def getD(self, bcname):
        self.bcname = bcname

    def putD(self):
        print(self.bcname, "Car Belongs To Bench Company.")
        print("*" * 60)


m=bench()
m.putA()
m.getB("Brezza")
m.putB()
m.getC("Creta")
m.putC()
m.getD("M G Hector")
m.putD()

