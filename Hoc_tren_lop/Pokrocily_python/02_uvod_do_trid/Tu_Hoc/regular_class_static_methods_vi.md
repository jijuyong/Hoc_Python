# Phân biệt Regular Method, Class Method và Static Method trong Python

Python có 3 loại method thường gặp:

- **Regular method (instance method)**: nhận `self`, đại diện cho object hiện tại.
- **Class method**: dùng `@classmethod`, nhận `cls`, đại diện cho class hiện tại.
- **Static method**: dùng `@staticmethod`, không tự nhận `self` hoặc `cls`.

## 1. So sánh nhanh

| Loại method | Tham số tự động | Dùng để |
|---|---|---|
| Regular method | `self` — object hiện tại | Đọc hoặc thay đổi dữ liệu riêng của object |
| Class method | `cls` — class hiện tại | Thao tác với class hoặc dữ liệu cấp class; thường dùng làm phương thức khởi tạo thay thế |
| Static method | Không có | Hàm tiện ích liên quan đến class nhưng không cần truy cập trực tiếp object hay class |

## 2. Ví dụ với class `Sieu_nhan`

```python
class Sieu_nhan:
    suc_manh = 50

    def __init__(self, id, vu_khi):
        self.id = id
        self.vu_khi = vu_khi

    # Regular method
    def thong_tin(self):
        return f"Hero {self.id}, vu khi: {self.vu_khi}"

    # Class method
    @classmethod
    def update_power(cls, smach):
        cls.suc_manh = smach

    # Static method
    @staticmethod
    def kiem_tra_id(id):
        return id > 0
```

Cách gọi:

```python
hero1 = Sieu_nhan(556, "Kiem")

print(hero1.thong_tin())
Sieu_nhan.update_power(100)
print(Sieu_nhan.suc_manh)
print(Sieu_nhan.kiem_tra_id(556))
```

Kết quả:

```text
Hero 556, vu khi: Kiem
100
True
```

## 3. Regular method: `self` đại diện cho object

```python
def thong_tin(self):
    return self.id
```

Khi gọi `hero1.thong_tin()`, Python tự truyền object `hero1` vào `self`. Nếu gọi `hero2.thong_tin()`, `self` sẽ là `hero2`.

## 4. Class method: `cls` đại diện cho class

```python
@classmethod
def update_power(cls, smach):
    cls.suc_manh = smach
```

Khi gọi:

```python
hero1.update_power(100)
```

Python tự truyền class tương ứng vào `cls`, chứ không truyền object `hero1` như `self`. Với class `Sieu_nhan`, lời gọi này tương đương:

```python
Sieu_nhan.update_power(100)
```

Do đó, `Sieu_nhan.suc_manh` được đổi thành `100`. Các object không có thuộc tính `suc_manh` riêng sẽ đọc giá trị mới từ class.

### Class method làm phương thức khởi tạo thay thế

```python
@classmethod
def from_string(cls, s):
    id_hero, vu_khi = s.split("-", 1)
    return cls(int(id_hero.strip()), vu_khi.strip())
```

Gọi như sau:

```python
hero3 = Sieu_nhan.from_string("558 - am khi")
print(hero3.__dict__)
```

Kết quả:

```python
{'id': 558, 'vu_khi': 'am khi'}
```

Dùng `cls(...)` giúp tạo object từ class hiện tại. Nếu class con kế thừa `Sieu_nhan`, phương thức cũng có thể tạo object thuộc class con đó.

## 5. Static method: không tự nhận `self` hoặc `cls`

```python
@staticmethod
def kiem_tra_id(id):
    return id > 0
```

Khi gọi `Sieu_nhan.kiem_tra_id(556)`, Python chỉ truyền `556` vào tham số `id`; nó không tự thêm `self` hoặc `cls`.

Static method vẫn có thể truy cập class nếu bạn truyền class vào như một đối số hoặc tham chiếu tên class trực tiếp, nhưng Python không tự truyền class như với `@classmethod`.

## 6. Khi nào nên dùng loại nào?

- Muốn đọc hoặc sửa dữ liệu riêng của object: dùng **regular method**.
- Muốn đọc hoặc sửa dữ liệu cấp class: dùng **`@classmethod`**.
- Muốn tạo object từ chuỗi hoặc dữ liệu khác: thường dùng **`@classmethod`**.
- Muốn viết hàm tiện ích liên quan đến class nhưng không cần `self` hay `cls`: dùng **`@staticmethod`**.

## 7. Mẹo ghi nhớ

- `self` = object hiện tại.
- `cls` = class hiện tại.
- `@staticmethod` = hàm không tự nhận `self` hay `cls`.

### Câu hỏi tự kiểm tra

Với method:

```python
@staticmethod
def cong(a, b):
    return a + b
```

Khi gọi `Sieu_nhan.cong(3, 5)`, Python chỉ truyền `3` và `5` vào `a` và `b`. Kết quả là `8`.
