class Modi:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("This Is A Modi Family")
        print("*"*40)

class Chinu(Modi):
    def getB(self, Cname):
        self.Cname=Cname

    def putB(self):
        print(self.Cname,"Is a Son Of Chinu Bhai")
        print("*" * 40)

class Dashrath(Modi):
    def getC(self, Dname):
        self.Dname = Dname

    def putC(self):
        print(self.Dname,"Is a Son Of Dashrath Bhai")
        print("*" * 40)

class Raju(Chinu):
    def getD(self, Rname1,Rname2):
        self.Rname1 = Rname1
        self.Rname2 = Rname2

    def putD(self):
        print(self.Rname1,"Is a Son Of Raju Bhai")
        print(self.Rname2, "Is a Son Of Raju Bhai")
        print("*" * 40)
class Kanu(Chinu):
    def getE(self, Kname):
        self.Kname = Kname

    def putE(self):
        print(self.Kname,"Is a Son Of Kanu Bhai")
        print("*" * 40)
class Mahendra(Dashrath):
    def getF(self, Mname):
        self.Mname = Mname

    def putF(self):
        print(self.Mname,"Is a Son Of Mahendra Bhai")
        print("*" * 40)

c1=Chinu()
d1=Dashrath()
r1=Raju()
k1=Kanu()
m1=Mahendra()

c1.putA()
Cc=input("Enter Father Name Son Of Chinubhai :  ")
c1.getB(Cc)
c1.putB()
m1.getC("MahendraBhai")
m1.putC()
r1.getD("Jalak","Sunny")
r1.putD()
k1.getE("Suraj")
k1.putE()
m1.getF("Bhaumik")
m1.putF()








