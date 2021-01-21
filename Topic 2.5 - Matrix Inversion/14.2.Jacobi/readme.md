# Phương pháp Jacobi tìm gần đúng ma trận nghịch đảo - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Ma trận `A`, kích cỡ `n` và sai số `eps`
- Output: Ma trận nghịch đảo theo PP Jacobi với cả 2 đánh giá tiên nghiệm và hậu nghiệm
## Hướng dẫn sử dụng
### Chú ý trước khi sử dụng
* File `jacobi_fromfile.py` phải để cùng với file `lib_jacobi.py` trong cùng 1 thư mục, bởi file này là file thư viện, chứa các lệnh cần thiết để tiến hành thuật toán
* Yêu cầu cài đặt thư viện NumPy

### Cách sử dụng
_Note:_ Để tránh xung đột code, nhóm đã xóa cách nhập trực tiếp từ code
- **Bước 1:** Tạo file `input.txt` và nhập ma trận
**Chú ý:** Không cần nhập kích thước ma trận vì chương trình tự dò kích cỡ ma trận nhập vào và bắt nhập lại nếu ma trận bị sai kích cỡ
- **Bước 2:** Chạy file `jacobi_fromfile.py` và làm theo hướng dẫn


## Ưu, nhược điểm của thuật toán
- **Ưu điểm:** 
    - Chạy với mọi xấp xỉ đầu
    - Sai số tính toán được sửa lại sau mỗi bước lặp.
- **Nhược điểm:**
    - Thuật toán phức tạp
    - Yêu cầu ma trận phải chéo trội

