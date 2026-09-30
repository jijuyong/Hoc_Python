'''
De bai
- phan tich su khac nhau giua List va Tuple
'''

#1. Tao
my_list = [1,2,3]
my_tuple = (1,2,3)

#2. sua phan tu
my_list[0] = 99 #✅
my_tuple[0] = 99 #❌

#3. them phan tu
my_list.append(12)#✅
my_tuple.append(12) #❌

#4. Lam key cho Dict
d = {(1,2): "tuple"}#✅
d2 = {[1,2]:"list"} #❌

