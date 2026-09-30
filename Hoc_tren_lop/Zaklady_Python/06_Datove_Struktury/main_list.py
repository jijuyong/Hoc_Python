# -------1. Danh sách (List)-----------

# Danh sách rỗng
danh_sach_cua_toi = []

# Danh sách có dữ liệu (có thể chứa nhiều kiểu dữ liệu khác nhau)
trai_cay = ["táo", "lê", "chuối", 10, True]
rau_cu = ["brocolice","potato","tomato","salad"]

# Truy cập bằng chỉ số (bắt đầu từ 0)
print("trai cay[0]: ",trai_cay[0])# tao
print("trai cay[-1]: ",trai_cay[-1]) # true

print("--------------------------------")
print("khi dung appaned(): ")
trai_cay.append("dua hau")
print(trai_cay)

print("--------------------------------")
print("khi dung insert(): ")
trai_cay.insert(3,"thanh long")
print(trai_cay)

print("--------------------------------")
print("khi dung remove(): ")
trai_cay.remove("chuối")
print(trai_cay)

print("--------------------------------")
print("khi dung pop(): ")
trai_cay.pop()
print("da xoa",trai_cay.pop(2))
print(trai_cay)

print("--------------------------------")
print("khi dung del: ")
print("da xoa",trai_cay[0])
del trai_cay[0]
print(trai_cay)

print("--------------------------------")
dang_sach_so = [8,12,1,0,78,12,3,5,699]
print("khi dung sort(): ")
dang_sach_so.sort()
print(trai_cay)
print(max(dang_sach_so))

print("--------------------------------")
print("khi dung extend(): ")
trai_cay.extend(rau_cu)
print(trai_cay)

#---------------toan tu +,*,in/not in --------------
print("--------------------------------")
print("toan tu +")
print([1,2,3]+["a","b"])
print("toan tu *")
print([1,2,3]*3)
print("in/ not in")
print("a" in ["a","b","c"])
print("z" not in ["a","b","c"])



#-------------Slicing list-------------
print("--------------------------------")
s = ["p","y","t","h","o","n"]
print(s[2:4])# in ra tu 2->4
print(s[3:])# in ra tu 3->het
print(s[:3])# in ra tu dau->3
print(s[0:5:2])# in ra tu 0->5 buoc nhay la 2 : 0 2 4
print(s[::-1])# dao nguoc


# -------3. Tập hợp (Set)-----------
print("--------------------------------")
cac_so = {1, 2, 3, 3, 3, 4}
print(cac_so)  # In ra: {1, 2, 3, 4} -> các phần tử trùng đã bị xóa
