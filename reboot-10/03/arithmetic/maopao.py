#!/usr/bin/env  python
#coding:utf8
data = [8,5,9,3]
n = len(data)

for i in range(n-1):     
    for j in range(n-i-1):       # 效率比较高的方式，内部循环每次减少一次，因为后面的值都固定了
    #for j in range(n-1):         # 比较死板的方式，内外循环都全部循环一遍
        if data[j]  > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
         
print data 
# i = 0,外循环第一圈，最大值出来
# [5,8,9,3]  [5,8,9,3] [5,8,3,9]    # 效率高的方式,j = 0,1,2
# [5,8,9,3]  [5,8,9,3] [5,8,3,9]    # 效率低的方式,j = 0,1,2

# i = 1,外循环第二圈，第二大值出来
# [5,8,3,9]  [5,3,8,9]              # 效率比较高的方式，最后一个值已经是最大了，不需要再比了,j = 0,1     
# [5,8,3,9]  [5,3,8,9] [5,3,8,9]    # 效率低的方式，多比了一次 j = 0,1,2

# i = 2,外循环第三圈，第三大值出来
# [3,5,8,9]                         # 效率高的方式， 最后的两个值已经是最大了，只需要比一次即可,j = 0
# [3,5,8,9]  [3,5,8,9] [3,5,8,9]    # 效率低的方式，又全部比一遍 j = 0,1,2

#!/usr/bin/env python
#coding:utf-8
array = [8,5,9,3]
for i in range(len(array))[::-1]:  # 原理一样，range(4)为:0,1,2,3，翻转之后为3,2,1,0
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array

# 外循环第一圈i = 3,内循环对比3圈j分别为0,1,2,最大值出现
# [5,8,9,3] [5,8,9,3] [5,8,3,9] 

# 外循环第二圈i = 2,内循环对比2圈j分别为0,1,最二大值出现
# [5,8,3,9] [5,3,8,9]  

# 外循环第三圈i = 1,内循环对比1圈j为0,最三大值出现
# [3,5,8,9]  

# 外循环第四圈i = 0,内循环对比1圈j为0,最四大值出现
# [3,5,8,9]  
