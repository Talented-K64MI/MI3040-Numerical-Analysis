# Giải hệ phương trình tuyến tính bằng phương pháp Cholesky: AX=B - Nhóm ?? - Trần Đắc Dương

## Input, ouput
* Input: Viết input vào một file text dưới dạng ma trận A|B
* Output: Các bước giải và ma trận nghiệm X

## Hướng dẫn sử dụng
* Tạo một file .txt tên text (không có đuôi), sau đó nhập ma trận A|B vào file này.
* Chạy chương trình
* Tìm ma trận A1 đối xứng: 
    * Nếu ma trận A đối xứng thì đặt A1=A
    * Nếu ma trận A bất đối xứng thì A1=A^t*A và B1= A^t*B
* Khi đó phương trình trở thành A1*X=B1
* Tìm ma trận A1 ở hàm `cholesky1()` và tìm ma trận B1 ở hàm `cholesky2()`

Phân tích A1 theo Cholesky: A1=S^t*S
Tìm ra ma trận S ở hàm `cholesky()`, đồng thời kiểm tra định thức ma trận A1 có bằng 0 không? Nếu det(A1)=0 thì kết thúc chương trình
Khi đó phương trình trở thành: S^t*S*X=B1

* Đặt Y=S*X có:  S^t*Y=B1
* Giải phương trình này tìm ma trận Y bằng hàm `cholesky3()`

* Giải phương trình SX=Y ta được nghiệm X của phương trình bằng hàm `cholesky4()`
