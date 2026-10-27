class A:
    def pozdrav(self):
        print("Ahoj z A")

class B(A):
    def pozdrav(self):
        print("Ahoj z B")
        super().pozdrav()

class C(A):
    def pozdrav(self):
        print("Ahoj z C")
        super().pozdrav()

class D(B,C):
    def pozdrav(self):
        print("Ahoj z D")
        super().pozdrav()

D().pozdrav()