# Phương pháp Newton tìm gần đúng ma trận nghịch đảo - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Ma trận `A`, kích cỡ `n` và sai số `eps`
- Output: Ma trận nghịch đảo theo PP Newton
## Hướng dẫn sử dụng
### Chú ý trước khi sử dụng
* Các file `newton_fromfile.py` và `newton_terminal.py` phải để cùng với file `lib_newton.py` trong cùng 1 thư mục, bởi file này là file thư viện, chứa các lệnh cần thiết để tiến hành thuật toán
* Yêu cầu cài đặt thư viện NumPy

### Cách sử dụng
_Note:_ Để tránh xung đột code, nhóm đã xóa cách nhập trực tiếp từ code
- **Bước 1:** Chỉnh sửa dòng 11, 12, 13 theo comment trong file `newton_terminal.py`
- **Bước 2:** Chạy file `newton_terminal.py` và làm theo hướng dẫn

## Ưu, nhược điểm của thuật toán
- **Ưu điểm:** 
    - Tốc độ hội tụ rất nhanh khi xấp xỉ đầu thỏa mãn.
    - Sai số tính toán được sửa lại sau mỗi bước lặp.
    - Dễ cài đặt, thuật toán đơn giản, dẽ nhớ.
- **Nhược điểm:**
    - Rất khó tìm xấp xỉ đầu cho phương pháp này do yêu cầu của hệ số co q.
