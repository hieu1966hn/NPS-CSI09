## Thuật toán tìm kiếm Linear Search

number_list = [5, 9, 1, 12, 30, 35]

## Tìm vị trí khi biết giá trị
# def linear_search(data_list, value):
#     for i, el  in enumerate(data_list):
#         if el == value:
#             return i # dừng vòng lặp lại và trả về vị trí của phần tử thỏa mãn tìm kiếm.
        
# print(linear_search(number_list, 30)) ##

## Tìm giá trị khi biết vị trí
# def find_number(number_list, number):
#     index = linear_search(number_list, number) # sử dụng linear search
#     if index:
#         print('{} found at index {}'.format(number, index))
#     else:
#         print('{} not found'.format(number))
        

# print(find_number(number_list, 30))



## Giả sử danh sách đầu vào được sx theo thứ tự tăng dần
## Ta định nghĩa khoảng tìm kiếm là toàn bộ danh sách

# number_list.sort() ## [1, 5, 9, 12, 30, 35]
# print(number_list) 


## Viết hàm tính giai thừa của 1 số n:

    
def factorial(n):
    if n < 0:
        return "negative num bruh"
    elif n == 0 or n == 1:
        return 1
    else:
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp
    
    
def factorial2(num): # 3!
    if num == 0 or num == 1: # điều kiện cơ sở
        return 1
    return num * factorial2(num - 1) # 3*2*1
        
    

# print(factorial(5))
    
    
    
    