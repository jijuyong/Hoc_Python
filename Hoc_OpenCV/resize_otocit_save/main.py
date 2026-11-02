import cv2

img = cv2.imread("image1.png",1)

# resize anh - cv2.resize(doi_tuong, (rong,dai)
img2 = cv2.resize(img,(400,200))
'''xuat anh bang x lan ban dau (anh_dau_vao,(kich thuoc dau ra),fx,fy)
 - kich thuoc dau ra (0,0) - Có nghĩa là bạn không chỉ định kích thước cụ thể cho ảnh đầu ra.
 - fx=0.1 - Có nghĩa là chiều rộng của ảnh mới bằng 10% chiều rộng ảnh ban đầu.
- fy=0.1 - Tương tự, chiều cao của ảnh mới bằng 10% chiều cao ảnh ban đầu.
'''
img3 = cv2.resize(img,(0,0),fx=0.1,fy=0.1)

'''xoay anh, cv2. rotate(anh dau vao, huong xoay)
- huong xoay:
  ~ cv2.ROTATE_90_CLOCKWISE - Xoay 90° theo chiều kim đồng hồ
  ~ cv2.ROTATE_90_COUNTERCLOCKWISE - Xoay 90° ngược chiều kim đồng hồ
  ~ cv2.ROTATE_180
'''
img4 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Anh zoro",img4)
k = cv2.waitKey(0)
print(k)

# luu thanh file moi neu bam "s"
if k == 115:
    cv2.imwrite("C:\\Users\avoca\\GitHub\\Hoc_Python\\Hoc_OpenCV\resize_otocit_save\\zoro_hot.png",img2)
    # ghi ten moi cho anh, hoac ghi link