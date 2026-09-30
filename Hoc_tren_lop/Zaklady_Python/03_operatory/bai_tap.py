'''
1. Các phép toán
Yêu cầu người dùng nhập vào hai số nguyên. In ra kết quả của:

Phép cộng
Phép nhân
Phép lũy thừa (số thứ nhất mũ 2)
Phần dư sau phép chia (modulo)
'''

a = int(input("nhap vao so a: "))
b = int(input("nhap vao so b: "))

print(a,"+",b,"=",a+b)
print(a,"*",b,"=",a*b)
print(a,"^2","=",a**2)
print(a,"%","=",a%b)

'''
2. Thám tử
Yêu cầu người dùng nhập vào câu yêu thích của họ.
Sử dụng toán tử in để kiểm tra xem câu đó có chứa từ "Python" hay không. In ra True hoặc False.
'''

cau_yeu_thich = input("nhap vao cau yeu thich cua ban: ")
kiem_tra = "Python" in cau_yeu_thich
print(f"chu python co trong cau yeu thich khong: {kiem_tra}")

'''
3. Tính chia hết
Nhập một số. Kiểm tra (True/False) xem số đó có đồng thời chia hết cho 5 VÀ 10 hay không.
'''
so = int(input("nhap vao so: "))
print(so%5==0 and so%10==0)

'''
nhap vao tu ban phim S(tong 2 so) va D(hieu 2 so). In ra 2 so do
cong thuc: neu a+b=S va a-b = D thi:
a = (S+D)/2
b = (S-D)/2
'''
S = int(input("nhap vao tong 2 so: "))
D = int(input("nhap vao hieu 2 so: "))
a = (S+D)/2
b = (S-D)/2

