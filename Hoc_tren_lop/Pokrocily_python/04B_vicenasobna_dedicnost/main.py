class Bo:
    def an(self):
        print("Bo dang an")

class Me:
    def ngu(self):
        print("me dang ngu")

class Con(Bo,Me):# ke thua cua bo va me
    pass

be = Con()
be.an()
be.ngu()

'''ket hua kieu diamant
            A
        //      \\
        B        C
        \\     //
            D
'''

'''
print('*'*10,"Vi du diamant",'*'*10)
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")
        A.hello(self)

class C(A):
    def hello(self):
        print("C")
        A.hello(self)

class D(B, C):
    def hello(self):
        print("D")
        B.hello(self)
        C.hello(self)

D().hello() # nhu the nay A se dc goi 2 lan
'''

#MRO - method resolution order 
# tim ham trong D neu ko co thi -> class B -> class C ->class A

class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")
        super().hello()

class C(A):
    def hello(self):
        print("C")
        super().hello()

class D(B, C):
    def hello(self):
        print("D")
        super().hello()

D().hello()#in D roi goi super, luc goi xong -> classB neu class B co super thi -> classC
# neu class C van van super thi  -> class A , neu class A ko co super thi chuoi kthuc o day