Buổi 4: Thuật toán tìm kiếm
- Các dạng bài toán tìm kiếm
- Các thuật toán tìm kiếm: Linear Search, Binary Search, Tìm kiếm Subset
- Phương pháp đệ quy


Giới thiệu bài toán tìm kiếm
- Tìm kiếm là một bài toán phổ biến trong lập trình 
+ Nhập chữ để tìm bạn bè trên facebook, tìm đoạn chát trên facebook, tìm phần mềm trong thanh search của windows, tìm kiếm trên google, youtube, ...
+ Cho danh sách của KH, tìm mặt hàng phổ biến nhất, các KH trung thành.

=> BÀI HỌC: bao gồm những bài toán tìm kiếm thông thường nhất và thuật toán để giải quyết những bài toán đó.


- Tại sao phải học cách viết thuật toán khi Python và các thư viện (Numpy, ...) đã hỗ trợ?
+ Mục đích học thuật toán không phải để hoàn thành các việc như: Tìm kiếm, sắp xếp, .. => Những việc đó đều có thư viện hỗ trợ.
+ Học thuật toán để phát triển tư duy lập trình và tư duy thuật toán: cách phân tích vấn đề từ dạng văn bản hay lời nói thành input, output và các bước để xử lý input thành output.
+ Học thuật toán để chọn cách lưu trữ và xử lý dữ liệu phù hợp để giải quyết các vấn đề lớn hơn (VD: Google không chỉ dùng một thuật toán tìm kiếm đơn giản mà là tổ hợp của nhiều thuật toán khác nhau)


Khi xử lý một bài toán tìm kiếm, ta quan tâm đến gì? 
+ Đặc trưng của thành phần cần tìm kiếm
+ Đặc trưng của dữ liệu chứa thành phần đó


Tìm kiếm tuần tự: (Linear Search)
Đề bài: Tìm kiếm vị trí của một phần tử dựa vào giá trị của nó trên một danh sách cho trước.

Ứng dụng: Tìm mã số khách hàng dựa vào họ tên, cộng điểm thành viên dựa vào họ tên hoặc số điện thoại khách hàng.


**Độ phức tạp**:
- Thời gian: O(n), do sử dụng một vòng lặp.
- Không gian: O(n), để lưu danh sách các giá trị.



Tìm kiếm nhị phân:
Đề bài: Tìm kiếm vị trí của một phần tử dựa vào giá trị của nó trên một danh sách đã được sắp xếp.

Thực hiện lặp lại các bước sau: 
- So sánh giá trị ở chính giữa khoảng tìm kiếm với giá trị cần tìm
+ nhỏ hơn: Mọi phần tử bên trái giá trị giữa đều nhỏ hơn giá trị cần tìm. Do đó, ta thu hẹp khoảng tìm kiếm lại thành nửa bên phải khoảng tìm kiếm.
+ lớn hơn:  Mọi phần tử bên phải giá trị giữa đều lớn hơn giá trị cần tìm. Do đó, ta thu hẹp khoảng tìm kiếm lại thành nửa bên trái khoảng tìm kiếm.
+ bằng: kết thúc vòng lặp và trả về giá trị tìm kiếm.


Trường hợp đặc biệt: Vòng lặp kết thúc sau khi khoảng tìm kiếm chỉ còn 1 phần tử và vẫn không thấy giá trị



Đệ quy: 
- Là thuật ngữ chỉ việc một hàm tự gọi chính nó. Thuật toán đệ quy thường dùng để giải quyết những bài toán có thể xử lý bằng cách đưa về các bài toán nhỏ hơn cùng loại.


VD: Bài toán tính giai thừa: n! = 1*2*3*...*n



Đề bài thực hành:
**Yêu cầu 1: Thành phố biển**: Cho danh sách các thành phố biển ở Việt Nam, kiểm tra "Quy Nhơn" có nằm trong danh sách không. Nếu có, trả về vị trí tìm thấy.
sea_cities = ['Hải Phòng', 'Đà Nẵng', 'Quy Nhơn', 'Tuy Hòa', 'Nha Trang', 'Phan Rang', 'Vũng Tàu']


**Yêu cầu 2: Điểm thi**: Ban tổ chức của một cuộc thi công bố kết quả theo thứ tự điểm từ thấp đến cao. Hãy tìm tên của thí sinh đạt được đúng 20 điểm.
contest_result = [('Nam', 10), ('Hải', 13), ('Hoa', 13), ('Tuấn', 20), ('Trung', 20), ('Khải', 23), ('Ly', 30)]
