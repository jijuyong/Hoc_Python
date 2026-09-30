'''
1. Danh sách đi chợ (List)
Tạo một danh sách di_cho chứa: "bánh mì", "bơ", "táo".

Thêm "sữa" vào cuối danh sách.
Xóa "bơ" khỏi danh sách.
In ra số lượng món đồ trong danh sách (len()).
'''

danh_sach_di_cho = ["banh mi", "bo","tao"]
danh_sach_di_cho.append("sua")
danh_sach_di_cho.remove("bo")

print(f"so luong do can mua la: {len(danh_sach_di_cho)}")
for do in danh_sach_di_cho:
    print(do)

'''
2. Bình phương số (List Comprehension)
Sử dụng list comprehension để tạo một danh sách các bình phương 
của các số từ 0 đến 9. Kết quả sẽ là [0, 1, 4, 9, ...].
'''
danh_sach_binh_phuong = []
for i in range (10):
    danh_sach_binh_phuong.append(i*i)

print(danh_sach_binh_phuong)

'''
3. Danh bạ điện thoại (Dict)
Tạo một dictionary với khóa là tên và giá trị là số điện thoại.

In ra số điện thoại của "Nam".
Thêm một liên hệ mới "Lan".
In ra tất cả các tên trong danh bạ (các khóa).
'''

danh_ba = {
    "Nam": "0912345678",
    "An": "0987654321",
    "Bình": "0901122334"
}

print(f"so dien thoai cua nam la: {danh_ba['Nam']}")

danh_ba["Lan"] = "09432147126"

print(danh_ba.items())

'''
4. Các số duy nhất (Set)
Cho danh sách [1, 2, 2, 3, 1, 4, 5, 5]. 
Chuyển đổi nó thành một Set và in kết quả ra màn hình để loại bỏ các phần tử trùng lặp.
'''

cac_so = {1,2,2,3,1,4,5,5}
print(cac_so)
