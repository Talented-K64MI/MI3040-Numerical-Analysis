# Tìm Min-Max của hàm f(x) trên đoạn `[a; b]` - Nhóm 7 - Nguyễn Thị Hường-Lê Trung Kiên

## A. ĐỐI VỚI  MIN-MAX.CPP
## Input, output
- **Input:**  `a`, `b`, `f(x)`, (`step` và `eta` nếu lâu quá có thể thay đổi)

- **Output:** Bộ giá trị sau:
    * `XMAX` và `F(XMAX)`
    * `XMIN` và `F(XMIN)` 
    * Các `X*` và `F(X*)`


## Hướng dẫn sử dụng: 
Dịch và chạy file `MIN-MAX.cpp`, với các thay đổi sau:
- Thay đổi [a,b] (dòng 8,9) và hàm `f(x)` (dòng 16)
- Có thể thay đổi eta nhỏ hơn ở dòng 3 và thay đổi khoảng [a,b] nhỏ hơn  trong trường hợp khoảng lớn dễ in thiếu điểm tới hạn.

## Cách sử dụng từng hàm trong chương trình

- Hàm `f(x)`: Nhập hàm
- Hàm `f1(x0)`: Trả về giá trị f'(x0)
- Hàm `gda(x0)`: Trả về giá trị x*>x0 thoa man f'(x*)=0
_(Các giá trị trả về tăng dần do x0 tăng dần (i:=a->b))_
- Hàm `luutru()` không trả về giá trị: Lưu các giá trị x*, f(x*),a, f(a) và b f(b) vào map
- Hàm `xuat1()` không trả về giá trị: Xuất các điểm tới hạn
- Hàm `xuat2()` không trả về giá trị: Tìm và xuất max và min của f(x)

## Cấu trúc dữ liệu `map` - Ánh xạ
`map` giống với mảng nhưng
- chỉ số của map ko nhất thiết là số nguyên dương mà có thể là bất kì kiểu dữ liệu gì.
- Giá trị của `map` tương tự mảng, có thể là bất kì kiểu dữ liệu gì. 

**Ví dụ:** 1 phần tử của map có thể là `A["abc"] = 123` theo dạng `(key) - (value)` hay cặp `(Khóa - Giá trị)`

Nếu dùng map thì chỉ cần 1 map là có thể lưu được thông tin của x và f(x). Trong bài mình lưu theo kiểu `A[1.123] = 6.78` thì 1.123 là x, 6.78 là f(x)

## Hạn chế
- Chỉ làm được với các hàm f(x) liên tục trên [a;b]
- Chỉ làm chính xác với các hàm có f(x) và f'(x) cùng liên tục trên [a;b]
    + Do thuật toán này đi tìm các điểm x* thỏa mãn f'(x*)=0, nhưng các điểm cực trị thì không nhất thiết f(x*)=0
    + f`(x) có thể kxđ miễn là đổi dấu khi đi qua x*, vì thế nếu f'(x) ko liên tục thì nó có thể bỏ sót hoặc ko chạy được
- Có thể in ra nhiều nghiệp xấp xỉ nhau
- Đối với các hàm f(x) có khoảng cách các cực trị quá bé, nhỏ hơn `step` cũng không thể chính xác. Bởi:
    + Các giá trị x* chỉ tìm được xấp xỉ chứ không chính xác
    + Sau khi tìm được x* tạm chấp nhận được, ta sẽ tăng i lên 1 đoạn `step` để nó vượt qua x*, do đó sẽ bị bỏ sót các điểm tới hạn trong khoảng (x*, x* + step)
- Đối với khoảng [a,b] lớn dễ gây ra trường hợp in thiếu điểm tới hạn => Cách khắc phục: QUAY LẠI XEM DÒNG 3 MỤC HDSD VÀ CÓ THỂ SẼ CHẠY HƠI LÂU NÊN MỌI NGƯỜI CỨ BÌNH TĨNH CHỜ NHÉ!!
## B. ĐỐI VỚI MIN-MAX-2.CPP

## Input, Output
 - **Input:**  `a`, `b`, `f(x)`
- **Output:** Bộ giá trị sau:
    * `XMAX` và `F(XMAX)`
    * `XMIN` và `F(XMIN)` 
 
## Hướng dẫn sử dụng: 
Dịch và chạy file `MIN-MAX-2.cpp`, với các thay đổi sau:
- Thay đổi [a,b] (dòng 60) và hàm `f(x)` (dòng 10)
## Ưu điểm:
 Các trường hợp chạy chính xác hơn file `MIN-MAX.cpp`, do không bị ràng buộc bởi hệ số eta và độ lớn của đạo hàm.
 ## Nhược điểm: 
 Chạy lâu hơn.
