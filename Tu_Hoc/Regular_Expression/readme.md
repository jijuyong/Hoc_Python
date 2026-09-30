# **Regular Expression**

Regex - chuoi ky tu dac biet dung de tim kiem mau(pattern) trong chuoi

thay vi tim chinh xac 'abc', regax cho phep tim theo quy tac -
vd - "tim tat ca cac so", "tim email", "tim std"

## **1. Import**

#import bat buoc trc khi dung regex
`import re`

khi nao can dung?
- tim/dem tat ca cac so(hoac ky tu nao do) trong chuoi dai
- tach van ban theo nhieu ky tu phan cach khac nhau (space/tab/newline)
- validate email, sdt, mk - ktra "co dung dag ko"
- tim thay theo mau - vd: thay tat ca cac so bang SO

### **5 ham chinh**
- `re.findall`
- `re.split`
- `re.sub`
- `re.subn`
- `re.search `

khi viet regex - luon thay chu 'r' trc chuoi pattern: e'\d+' 
dung de thong bao python dung xu ly, de day cho regex

## **2. Doc pattern**

| Pattern | viet tat                 | Đọc là                     | vd khớp |
|:--------|:-------------------------|:---------------------------|:--------
| `\d`    | digit (chu so)           | 1 chữ số                   | 5       |
| `\d+`   | digit lặp                | 1/nhiều chữ số = 1 con số  |42, 123|
| `\D`    | digit Hoa = nguoc lai    | ko phải chữ số             |a, !|
| `\s`    | space                    | 1 space                    | " "|
| `\s+`   | space lặp                | 1/nhiều space liên tiếp    | "    " |
| `\S`    | Space Hoa = nguoc lai    | ko phải space              |a, 3|
| `\w`    | word (ký tự từ)          | chữ cái, số, hoặc _        |a,3, _ |
| `\W`    | Word Hoa = nguoc lai   . | ko phải ký tự từ           |!, @, " " |
| `\A`    | A = đầu bảng             | Đầu chuỗi                  |(vi tri) |
| `\Z`    | Z = cuối bảng            | Cuối bảng                  |(vi tri) |
| `\b`    | boundary (ranh giới)     | ranh giới (đầu/ cuối 1 từ) | (vi tri) |


## **3. Quy Tac nho**
`Chu thuong (\d,\s,\w)` = "la cai nay " -> \d = la digit
`Chu Hoa (\D,\S,\W)` = "ko phai la cai nay" -> \D = ko phai digit

- \d,\s ,\w khop KY TU - tim ra 1 ky tu cu the (so, space, chu cai)
- \A, \Z, \b khop VI TRI - ko tim ky tu nao , chi ktra "dag o dau/cuoi/ranh gioi hay ko"
