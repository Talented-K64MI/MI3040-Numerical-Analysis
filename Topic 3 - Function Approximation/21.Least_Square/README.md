# Bình phương cực tiểu

## Input, ouput
* Input: Bộ điểm xi,yi sẽ nhập vào file input.txt
* Output: 1 vecto hệ số của hệ sinh u = [ui] và vẽ đồ thị

## Hướng dẫn sử dụng
* Chọn hệ sinh u = [ui]
* Chạy như file python bình thường.
* Khuyến khích các bạn chuyển về file .ipynb để chạy từng đoạn code

## Phân tích ưu nhược điểm thuật toán
* Ưu điểm: 
	- Phương pháp tốt hơn với bộ dữ liệu lớn, ko overfitting
	- Xấp xỉ tốt nhất của y trong mặt phẳng P sinh bởi hệ sinh u 
* Nhược điểm: 
	- Nhạy cảm với nhiễu 
	- Với bộ dữ liệu có phương sai lớn thì độ lớn hàm mất mát tăng
	- Việc tăng số hàm sử dụng với bộ dữ liệu nhỏ dần đến over fitting không hiệu quả so với nội suy 

