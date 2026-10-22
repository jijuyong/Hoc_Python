from typing import Optional

'''1. Hàm có định nghĩa kiểu
Viết hàm tinh_chu_vi, hàm này:

Nhận một tham số canh (kiểu int hoặc float).
Trả về float.
Tính chu vi hình vuông (cạnh * 4).
'''
def tinh_chu_vi (canh:int|float)->float:
    return canh*4

print("UKOL01")
print("chu vi hinh vuong a =4,5 la: ",tinh_chu_vi(4.5))
print("chu vi hinh vuong a = 3 la: ",tinh_chu_vi(3))

'''
2. Bộ sưu tập (Collections)
Tạo một biến sinh_vien, biến này sẽ là một từ điển (dictionary) 
với khóa là tên (str) và giá trị là tuổi (int). Sử dụng chú thích kiểu chính xác.
'''

sinh_vien: dict[str:int]= {
    "An":20,
    "Binh":54
}

'''
3. Optional
Viết hàm tim_nguoi_dung(id: int), hàm này trả về tên người dùng (str) 
hoặc None nếu người dùng không tồn tại (trả về None cho bất kỳ ID nào > 10).
Đừng quên kiểu trả về là str | None (hoặc Optional[str]).
'''

def tim_nguoi_dung(id:int)->str|None:
    if id>10: 
        return None
    else: return f"Nguoi dung {id}"

print(tim_nguoi_dung(5))
print(tim_nguoi_dung(10))
print(tim_nguoi_dung(11))




