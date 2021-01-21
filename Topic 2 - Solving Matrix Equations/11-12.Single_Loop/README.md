# Nhóm 12 - Người code : Vũ Hoài Nam
# Giải gần đúng phương trình X=Cx+D bằng phương pháp lặp đơn
# Giải gần đúng phương trình AX=B bằng phương pháp jacobi hoặc phương pháp gauss-seidel
## Input, ouput
* Input: File `Equation.inp`
  * Dòng đầu chứa n và eps là kích thước ma trận vuông A (hoặc C) n*n và vector B (hoặc D) n*1 và sai số cho phép của kết quả
  * Dòng từ 2 tới n+1 chứa n số mỗi số miêu tả dòng i cột j của ma trận A (hoặc C với pp lặp đơn)
  * Dòng n+2 chứa n số mỗi số biểu diễn giá trị thứ j của vector B (hoặc D với pp lặp đơn)
  * Dòng n+3 chứa n số mỗi số biểu diễn giá trị thứ j của giá trị lặp ban đầu X0
* Output:File `Equation.out`
  * Trên mỗi dòng chứa n số mỗi số biểu diễn giá trị thứ j của X theo phương pháp lựa chọn.
* Error: Standard error
  * Trả về `MyError` nếu có lỗi input mà người viết kiểm soát được.
  * Nếu không có error :
    * Trên từng dòng ứng với phương pháp sử dụng sẽ in ra `Name, type, normtype, q, loopnumber, w` lần lượt là tên phương pháp,công thức sai số (1 ứng với hậu nghiệm 2 ứng với tiên nghiệm), loại chuẩn (1 ứng với chuẩn vô cùng, 2 và 3 lần ứng với chuẩn 1 và 2 trong sgk), hệ số co, số bước lặp của phương pháp và hệ số của công thức sai số (xuất hiện trong ma trận chéo trội cột trường hợp khác mặc định là 1.0)
* File Mymath.h có nhiệm vụ như một thư viện quy định các class Matrix (ma trận và vector), Equation (các phương pháp giải) hay MyError(lỗi) trong code.    
* File SingleLoop.cpp mang ý nghĩa file main chạy chương trình
## Hướng dẫn sử dụng
* Recomend sử dụng vscode, hoặc codeblocks để sử dụng (nên dùng bộ dịch C++11 trở lên)
* Với codeblocks sau khi clone về project mở file `SingleLoopMethod.cbp`
* Để chạy code sửa file Singleloop.cpp:
  * Bỏ comment từ dòng 36 -> 38 để chạy pp lặp đơn với ct sai số hậu nghiệm.
  * Bỏ comment từ dòng 39 -> 41 để chạy pp lặp đơn với ct sai số tiên nghiệm.
  * Bỏ comment từ dòng 42 -> 44 để chạy pp jacobi với ct sai số hậu nghiệm.
  * Bỏ comment từ dòng 45 -> 47 để chạy pp jacobi với ct sai số tiên nghiệm.
  * Bỏ comment từ dòng 48 -> 50 để chạy pp gauss-seidel với ct sai số hậu nghiệm.
  * Bỏ comment từ dòng 51 -> 53 để chạy pp gauss-seidel với ct sai số tiên nghiệm.
* Để thử các trường hợp test khác hãy sửa file Equation.inp
* Build chương trình thành file có đuôi .exe
* Chạy file có đuôi .exe đã tạo ở trên
## Phân tích ưu nhược điểm chương trình
* Ưu điểm: 
  * Kiểm soát được sai số khi tính toán X
  * Nghiệm X0 đầu vào không bị ràng buộc
  * Tốc độ lặp nhanh hơn đối với jacobi (pp gauss-seidel).
* Nhược điểm: (Ràng buộc)
  * Không thể tính được X khi ma trận C có chuẩn theo cả 3 loại trên lớn hơn 1 (pp lặp đơn).
  * Không thế tính được X khi ma trận A không chéo trội hàng hay cột (pp jacobi và gauss-seidel)
  * Chưa thật sự tối ưu khi tự định nghĩa các biến kiểu ma trận.
