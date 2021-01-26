# Phương pháp Runge - Kutta hiện giải bài toán Cauchy cho phương trình vi phân thường - Bùi Tiến Thành


## Bài toán
Giải PTVP sau:
$$ y' = f(x, y), \; y(x_0) = y_0 $$

## Input, ouput
* Input: Hàm $f$, giá trị ban đầu $(x_0, y_0)$, khoảng cách giữa 2 điểm liên tiếp $h$, số mốc của lưới điểm $n$ và số nấc của Runge-Kutta, bao gồm 1, 2, 3, 4 và kiểu hệ số của Heun
* Output: Gồm $n$ dòng gồm 2 giá trị $x_n$ và $y_n$ của hàm $y(x)$ tìm được

## Hướng dẫn sử dụng
Thuật toán này cần thư viện `sympy ` để chạy được chương trình. Có 2 cách chạy như sau:
* **Cách 1:** Chạy file `main_rungekutta.py` và làm theo hướng dẫn.
* **Cách 1:** Chạy file `main_rungekutta.ipynb` và làm theo hướng dẫn.


## Phân tích ưu nhược điểm thuật toán
* Ưu điểm: 
    * Ổn định, dễ cài đặt 
    * Cho ra giá trị tiếp theo từ giá trị ban đầu 
    * Dễ điều chỉnh khoảng cách $h$ giữa 2 điểm liên tiếp hơn phương pháp đa bước
* Nhược điểm: 
    * Tốn nhiều thơì gian để sinh ra nghiệm với cấp chính xác tương đương các phương pháp khác do số lần tính toán nhiều hơn 
    * Khó ước lượng sai số làm tròn