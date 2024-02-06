class A:
    def show(self):
        print("Show From Claas A :")
class B(A):
    def show(self):
        super().show()
        print("Show From Claas B :")
class C(A):
    def show(self):
        super().show()
        print("Show From Claas C :")
class D(B,C):
    def show(self):
        super().show()
        print("Show From Claas D :")
d1=D()
d1.show()
