## Thuật toán tìm kiếm Linear Search

number_list = [5, 9, 1, 12, 30, 35]

## Tìm vị trí khi biết giá trị
def linear_search(data_list, value):
    for i, el  in enumerate(data_list):
        if el == value:
            return i # dừng vòng lặp lại và trả về vị trí của phần tử thỏa mãn tìm kiếm.
        
# print(linear_search(number_list, 30)) ##

## Tìm giá trị khi biết vị trí
def find_number(number_list, number):
    index = linear_search(number_list, number) # sử dụng linear search
    if index:
        print('{} found at index {}'.format(number, index))
    else:
        print('{} not found'.format(number))
        
    

print(find_number(number_list, 30))
    
    
    