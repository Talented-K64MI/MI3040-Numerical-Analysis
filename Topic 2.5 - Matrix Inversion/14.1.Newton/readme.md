# Phương pháp Newton tìm gần đúng ma trận nghịch đảo - Nhóm 14 - Bùi Tiến Thành
## Input, ouput của chương trình
- Input: Ma trận `A`, kích cỡ `n` và sai số `eps`
- Output: Ma trận nghịch đảo theo PP Newton
## Hướng dẫn sử dụng
### Chú ý trước khi sử dụng
* File `newton_fromfile.py` phải để cùng với file `lib_newton.py` trong cùng 1 thư mục, bởi file này là file thư viện, chứa các lệnh cần thiết để tiến hành thuật toán
* Yêu cầu cài đặt thư viện NumPy

### Cách sử dụng
_Note:_ Để tránh xung đột code, nhóm đã xóa cách nhập trực tiếp từ code
- **Bước 1:** Tạo file `input.txt` và nhập ma trận
**Chú ý:** Không cần nhập kích thước ma trận vì chương trình tự dò kích cỡ ma trận nhập vào và bắt nhập lại nếu ma trận bị sai kích cỡ`
- **Bước 2:** Chạy file `newton_fromfile.py` và làm theo hướng dẫn của chương trình

## Ưu, nhược điểm của thuật toán
- **Ưu điểm:** 
    - Tốc độ hội tụ rất nhanh khi xấp xỉ đầu thỏa mãn.
    - Sai số tính toán được sửa lại sau mỗi bước lặp.
    - Dễ cài đặt, thuật toán đơn giản, dẽ nhớ.
- **Nhược điểm:**
    - ~~Rất khó tìm xấp xỉ đầu cho phương pháp này do yêu cầu của hệ số co q~~. Tuy nhiên nhóm đã phát triển thuật toán cải tiến và có thể chạy trên bất kỳ ma trận nào khả nghịch.
