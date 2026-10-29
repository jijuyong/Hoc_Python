class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vektor(
            self.x + other.x,
            self.y + other.y
        )

    def __eq__(self, value):
        if not isinstance(value,Vektor):
            return NotImplemented
        return self.x== value.x and self.y == value.y


class Seznam:
    def __init__(self,data):
        self.data=data
    def __getitem__(self, index):#truy cap phan tu bang chi so
        return self.data[index]

class Pozdrav: 
    def __call__(self):
        print("xin chao!")


v1 = Vektor(2, 3)
v2 = Vektor(4, 5)
#khi viet
v3 = v1+v2  
#python se goi phuong thuc add va chuyen v1 va v2 vao lam tham so other
print(v3)
#ham eq - so sanh hai doi tuong
print('*'*10,"Ham __eq__",'*'*10)
print(f"v1 == v2: {v1==v2}")

#__getitem__ – Truy cập phần tử bằng chỉ số
print('*'*10,"Ham __getitem__",'*'*10)
s = Seznam([10,20,30])
print(s[0])
print(s[2])

#ham __call__ - cho pheo goi doi tuong nhu ham
print('*'*10,"Ham __call__",'*'*10)
p = Pozdrav()
p()

