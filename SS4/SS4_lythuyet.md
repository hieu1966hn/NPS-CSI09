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