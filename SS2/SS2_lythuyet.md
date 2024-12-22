Buổi 2: Giới thiệu về thuật toán và Cấu trúc dữ liệu
- Ý nghĩa của thuật toán và cấu trúc dữ liệu
- Mối quan hệ giữa chúng
- Cấu trúc dữ liệu sẵn có trong Python

Skill
- Tính độ phức tạp của thuật toán
- Cách phân tích một bài toán về lập trình



Khái niệm
- Thuật toán: là một tập hữu hạn các bước cần thực hiện để giải quyết một vấn đề nào đó.
- VD: 
+ Bài toán sắp xếp dễ thấy nhất: chức năng sắp xếp file của windows(theo thời gian, theo loại, theo tên,..) 
+ hoặc sắp xếp video trên kênh Youtube (Theo thời gian, lượt view,..)
+ Giả sử cần sắp xếp 1 tỉ (10^9) số, Thuật toán đơn giản nhất: tìm số lớn nhất và đặt lên đầu đến khi hoàn tất, sẽ cần khoảng 10^18 phép tính. Một máy tính hiện tại cần khoảng 1s để xử lý 10^9 câu lệnh => hơn 30 năm để sắp xếp.
+ Với thuật toán hiệu quả hơn (Merge Sort, Quick Sort) thì chỉ cần thực hiện khoảng 10^10 phép tính => 10s để sắp xếp thành công.
+ Máy tính hoạt động cần phần cứng và điện để hoạt động nên thời gian chạy càng lâu thì càng tốn kém, nhất là đối với những hệ thống lớn => thuật toán sinh ra để giải quyết các bài toán theo cách hiệu quả nhất.

Độ phức tạp thuật toán: là thước đo độ hiệu quả của thuật toán dựa theo kích cỡ tập dữ liệu đầu vào.
- Có thể chia thành độ phức tạp về: thời gian (thời gian thi hành của thuật toán) không gian (kích cỡ bộ nhớ mà thuật toán cần để xử lý)
- Thường ký pháp O-lớn để nói về độ phức tạp của thuật toán. Ký pháp này thể hiện độ phức tạp trong trường hợp xấu nhất. Ký pháp này không thể hiện thời gian chạy thực tế của thuật toán, mà thể hiện mức độ thay đổi về thời gian chạy (hoặc bộ nhớ) của thuật toán khi kích cỡ dữ liệu đầu vào thay đổi. Tuy nhiên, ta vẫn có thể sử dụng ký pháp này để ước lượng thời gian chạy thực tế.
- VD: Một thuật toán sx có độ phức tạp về thời gian là O(N^2) thực thi trong 0.1s khi kích cỡ đầu vào là 10^4 số. Như vậy, khi kích cỡ đầu vào tăng gấp đôi 2*10^4, ta có thể ước tính thời gian thực thi sẽ tăng gấp 2^2=4, tức khoảng 0.4s


Khái niệm: lambda được sử dụng để tạo ra "hàm ẩn danh". Đây là các hàm không có tên, được định nghĩa một cách ngắn gọn với cú pháp sau: 

lambda arguments: expression
- arguments: Danh sách các tham số truyền vào
- expression: Biểu thức được tính toán và trả về kết quả (mặc định là trả về giá trị này, không cần từ khóa return).