# Giải phương trình tuyến tính AX=B - Nhóm 9 - Người code: Tuấn Anh Chí

## Input, ouput
* Input: Ma trận bổ sung [A|B]
* Output: Kết luận nghiệm và biểu diễn (nếu có)

## Hướng dẫn sử dụng
* Yêu cầu cài thư viện *numpy* trước khi sử dụng
* Nhập ma trận bổ sung vào file matrix.txt mỗi số hạng cách nhau bằng 1 khoảng trắng
* Nếu số hạng của 1 phần tử bằng 0 nhập 0 vào vị trí tương ứng
* Chạy và được kết quả

## Phân tích ưu nhược điểm thuật toán
* Ưu điểm: 
  * Giảm thiểu được sai số khi chia cho số gần không
  * Giải được ma trận với kích thước bất kì
  * Biểu diễn được nghiệm trong TH vô số nghiệm
* Nhược điểm: 
  * Code khá phức tạp và cồng kềnh
  * Có thể tốn nhiều thời gian khi kích thước ma trận quá lớn
