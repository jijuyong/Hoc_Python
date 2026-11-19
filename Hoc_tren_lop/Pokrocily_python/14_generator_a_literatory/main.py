'''1.1. Iterable – Đối tượng có thể lặp'''
#Iterable có nghĩa là một đối tượng mà bạn có thể sử dụng vòng lặp for để duyệt qua các phần tử.
print("**********ITERABLE************")
number = [1,2,3,4,5]
for number in number:
    print(number)


#Bạn có thể kiểm tra một đối tượng có phải Iterable không:
from collections.abc import Iterable
numbers = [1, 2, 3]
print(isinstance(numbers, Iterable))

'''1.2. Iterator – Bộ lặp'''
print("**********ITERATOR************")
#Iterator là đối tượng có khả năng cung cấp từng phần tử một.
numbers1= [10,20,30]
#hàm iter() - Chuyển một Iterable thành Iterator.
iterator = iter(numbers1)# numbers1.__iter__()
#ham next() - Lấy phần tử tiếp theo từ Iterator.
print(next(iterator))
print(next(iterator))#iterator.__next__()
print(next(iterator))
#print(next(iterator)) - se bi loi vi chi co 3 phan tu

'''1.3. Generator – Bộ sinh dữ liệu'''
print("**********GENERATOR************")
#Một điều quan trọng: Generator cũng là Iterator và Iterable.
#Generator là một loại Iterator đặc biệt, cho phép tạo dữ liệu từng phần tử một khi cần
def bo_dem():
    yield 1
    yield 2
    yield 3

g = bo_dem()

print(next(g))
print(next(g))
print(next(g))

# trong vong for
while True:
    try:
        numbers1 = next(iterator)
        print(numbers1)

    except StopIteration:
        break

    '''yield = Tạm dừng + Ghi nhớ trạng thái + Tiếp tục
Mỗi lần gọi next(), Generator tiếp tục chạy từ vị trí đã dừng trước đó.'''


"""5. Generator Expression – Biểu thức Generator"""
print("**********Generator Expression************")
numbers4 = (x*2 for x in range(5))
print(next(numbers4))
print(next(numbers4))
print(next(numbers4))
#hoac
for number in numbers4:
    print(number)

'''6.2. Tạo chuỗi vô hạn'''
def so_chan():
    number =0

    while True:
        yield number
        number+=2
        