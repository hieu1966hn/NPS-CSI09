sea_cities = ['Hải Phòng', 'Đà Nẵng', 'Quy Nhơn', 'Tuy Hòa', 'Nha Trang', 'Phan Rang', 'Vũng Tàu']

def find_city_recursively(cities, target, index=0):
    # Trường hợp cơ bản: danh sách rỗng hoặc đã kiểm tra hết thành phố
    if index >= len(cities):
        return -1 # không tìm thấy
    
    # Kiểm tra thành phố tại vị trí hiện tại
    if cities[index] == target:
        return index
    
    # Đệ quy kiểm tra thành phố tiếp theo
    return find_city_recursively(cities, target, index + 1)
        
## Kiểm tra Quy Nhơn có đang nằm trong ds hay không
# print(find_city_recursively(sea_cities, 'Quy Nhơn'))

    
    
    

contest_result = [('Nam', 10), ('Hải', 13), ('Hoa', 13), ('Tuấn', 20), ('Trung', 20), ('Khải', 23), ('Ly', 30)]

def find_score_recursively(results, target_score, index=0):
    # Trường hợp cơ bản: danh sách rỗng hoặc đã kiểm tra hết các kết quả
    if index>= len(results):
        return None # không tìm thấy
    
    ## Kiểm tra điểm số tại vị trí hiện tại: index
    if results[index][1] == target_score: 
        return results[index][0]
    
    ## Đệ quy kiểm tra thí sinh tiếp theo
    return find_score_recursively(results, target_score, index + 1)

print(find_score_recursively(contest_result, 20))
    
    