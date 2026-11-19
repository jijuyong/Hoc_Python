from collections.abc import Iterable

'''Bài 1: Đếm ngược (Countdown)
Đề bài:
Viết Generator countdown(n), trả về các số từ n về 0 bằng yield.
Sử dụng trong vòng lặp for.'''

def count_down(n):
    while n>=0:
        yield n
        n-=1


for i in count_down(10):
    print (i)

'''Bài 2: Dãy số chẵn vô hạn
Đề bài:
Viết Generator so_chan_lien_tiep(), trả về dãy:
0, 2, 4, 6, 8, 10, 12...
Lấy 5 số đầu tiên bằng next()'''

def so_chan_lien_tiep():
    n =0
    while True:
        yield n
        n+=2

g = so_chan_lien_tiep()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


