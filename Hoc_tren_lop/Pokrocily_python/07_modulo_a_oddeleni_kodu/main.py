import math_utils#modulo
# import cach 2 - import rieng ham thi phai ghi ntn, neu muon dung nheiu hon thi ghi them
from math_utils import cong,nhan

#cach 3
import math_utils as m

print("*" * 10, "Import thu vien math_utils", "*" * 10)

print(f"Ket qua phep cong: {math_utils.cong(3, 5)}")
print(f"Ket qua phep nhan: {math_utils.nhan(3, 5)}")

# ba cach import thuong gap
print("************3 cach import ***************")
'''cach 1  - import toan bo modulo
Bạn phải viết math_utils.cong() vì hàm thuộc module math_utils.
'''
print("---cach 1  - import toan bo modulo---")
print(f"math_utils.cong: {math_utils.cong(3,5)}")


'''cach 2 - Import riêng hàm
Bạn có thể gọi thẳng cong() mà không cần viết math_utils..
'''
print("---cach 2 - Import riêng hàm---")
print(f"phep cong:{cong(4,3)}")
print(f"phep cong:{nhan(4,3)}")


'''cach 3 - Đặt tên viết tắt (alias)
Ở đây, m là tên viết tắt của math_utils.
'''
print("---cach 3 - Đặt tên viết tắt (alias)---")
print(f"phep cong:{m.cong(4,3)}")
print(f"phep cong:{m.nhan(4,3)}")

#3. if __name__ == "main": la cai ji
#vi du


