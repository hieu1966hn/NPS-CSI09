import time
import math

## Ví dụ: Tính tổng số nguyên từ 1 đến n (n>1)

# Method 1
def cal_sum_n_v1(num):
    result = 0
    for i in range(num + 1):
        result += i
    return result

cal_sum_n_v1(5)

# Method 2
def cal_sum_n_v2(num):
    return (num+1) * num // 2

cal_sum_n_v2(5)


### Tính thời gian thực hiện của hai thuật toán trên?
def cal_time(func):
    start_time = time.time()
    result = func()
    real_time = time.time() - start_time
    return real_time, result
    
BIG_NUMS = {
    'ONE MILLION': 1000000,
    'TEN MILLION': 10000000,
    'ONE HUNDRED MILLION': 100000000,   
}

for name, num in BIG_NUMS.items():
    print('Execution time for {} numbers:'.format(name))
    time1, res1 = cal_time(lambda: cal_sum_n_v1(num))
    time2, res2 = cal_time(lambda: cal_sum_n_v2(num))
    print(time1-time2)
    
    print("- 0(n) algorithm: {} secs | result = {}".format(time1, res1))
    print("- 0(n) algorithm: {} secs | result = {}".format(time2, res2))
    print()
    
    
    
### Ví dụ minh họa về:lambda
# lamvda với một tham số
# square = lambda x: x**2
# print(square(5)) ## 25

# lamvda với nhiều tham số
# add = lambda a,b: a + b
# print(add(1, 2)) ## 3

# lambda với map, filter
# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x**2, numbers)
# print(list(squared)) ## output: [1, 4, 9, 16]



### 1.2 Độ phức tạp về không gian 0(1)