import cv2
#from cv2 import cv2


'''cv2.imread(link_anh, flag) - cu phap de doc anh
neu anh ko cung muc thu voi file thi "thu_muc_no_danh_o/image.jpg"

- flag
    ~ cv2.IMREAD_COLOR : doc anh mau (1) BGR
    ~ cv2.IMREAD_GRAYSCALE : doc anh xam (0)
    ~ cv2.IMREAD_UNCHANGED : doc anh goc (-1) BGRA
'''
# doc anh
image1 = cv2.imread("image1.png", 1)

#lenh hien thi anh - cv2.imshow(ten_cua_cua_so, anh)
cv2.imshow("Anh zoro", image1)
cv2.waitKey(0)  # Đợi nhấn phím bất kỳ để đóng cửa sổ hiển thị
cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ hiển thị