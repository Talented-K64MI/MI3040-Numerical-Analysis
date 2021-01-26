# Giải phương trình tuyến tính AX=B - Nhóm 9 - Tuấn Anh Chí, Bùi Xuân Thịnh

## Input, Output
* Input: Hệ số ma trận bổ sung [A|B]
* Output: Kết luận nghiệm và biểu diễn qua ma trận
(Chi tiết xem ví dụ ở dưới)

## Hướng dẫn sử dụng
* Yêu cầu cài thư viện `numpy` trước khi sử dụng
* Tạo file GJ_input.txt để cùng thư mục với file code
* Nhập hệ số ma trận bổ sung vào file GJ_input.txt mỗi số hạng cách nhau bằng 1 khoảng trắng " "
* Nếu số hạng của 1 phần tử bằng 0 nhập 0 vào vị trí tương ứng
* Chạy và được kết quả. Kết quả được lưu trong ma trận result và file GJ_output.txt
(Ma trận result có cột đầu là hệ số tự do, các cột sau lần lượt là hệ số biểu diễn
qua các ẩn tương ứng. Chi tiết xem ví dụ ở dưới)
    - Trong trường hợp hệ PT vô nghiệm, chương trình sẽ thông báo ra file GJ_output.txt
    - Trong hai trường hợp còn lại, ma trận biểu diễn nghiệm sẽ được lưu trong file GJ_output.txt 

## Phân tích ưu nhược điểm thuật toán
* Ưu điểm: 
  * Giảm thiểu được sai số khi chia cho số gần không
  * Giải được ma trận với kích thước bất kì
  * Biểu diễn được nghiệm trong trường hợp vô số nghiệm
  
* Nhược điểm: 
  * Code chưa tối ưu
  * Có thể tốn nhiều thời gian khi kích thước ma trận quá lớn  
  
## Ví dụ 1: giải hệ PT
x + y - 3z + 2t = 6
x - 2y     -  t = -6
    y +  z + 3t = 16
2x - 3y +2z     = 6

==> Nhập vào file GJ_input.txt:
```
1 1 -2 2 6
1 -2 0 -1 -6
0 1 1 3 16
2 -3 2 0 6
```

==> Output:
```
8.00000 0.00000 0.00000 0.00000 0.00000
6.00000 0.00000 0.00000 0.00000 0.00000
4.00000 0.00000 0.00000 0.00000 0.00000
2.00000 0.00000 0.00000 0.00000 0.00000
```

- Giải thích: Cột 1 là cột hệ số tự do, cột 2, 3, 4, 5 tương ứng biểu diễn qua các biến x, y, z, t
Trong trường hợp chỉ có một nghiệm duy nhất, trừ cột đầu tiên, các cột còn lại sẽ có giá trị bằng 0

## Ví dụ 2: giải hệ PT
x + 3y + 5z = 7
2x + 4y + 6z =8

==> Nhập vào file GJ_input.txt:
```
1 3 5 7
2 4 6 8
```

==> Output:
```
0.50000 0.00000 -0.50000 0.00000
0.00000 0.00000 1.00000 0.00000
1.50000 0.00000 -0.50000 0.00000
```

- Giải thích: Cột 1 là cột hệ số tự do, cột 2, 3, 4, 5 tương ứng biểu diễn qua các biến x, y, z, t
- Kết quả có ý nghĩa:
x = 0.5 - 0.5y
y = y
z = 1.5 - 0.5 y
==> Ở đây y là tham số, các nghiệm khác biểu diễn qua y


