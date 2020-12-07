# Giải gần đúng phương trình tuyến tính AX=B bằng phương pháp lặp đơn - Nhóm 12 - Người code : Vũ Hoài Nam

## Input, ouput
* Input:File Equation.inp
  * Dòng đầu chứa n và eps là kích thước ma trận vuông A n*n và sai số cho phép của kết quả
  * Dòng từ 2 tới n+1 chứa n số mỗi số miêu tả dòng i cột j của ma trận A
  * Dòng n+2 chứa n số mỗi số biểu diễn giá trị thứ j của vector B
  * Dòng n+3 chứa n số mỗi số biểu diễn giá trị thứ j của nghiệm ban đầu X0
* Output:File Equation.out
  * Dòng 1: chứa n số mỗi số biểu diễn giá trị thứ j của X theo phương pháp lặp đơn dùng công thức sai số hậu nghiệm
  * Dòng 2: chứa n số mỗi số biểu diễn giá trị thứ j của X theo phương pháp lặp đơn dùng công thức sai số tiên nghiệm
* Error: Standard error
  * Trả về MyError nếu có
  * Nếu không có error :
    * Dòng 1: in ra bốn số là type, normtype, q, loopnumber lần lượt là công thức sai số, loại chuẩn, hệ số co và số bước lặp của phương pháp
    * Dòng 2: in ra bốn số là type, normtype, q, loopnumber lần lượt là công thức sai số, loại chuẩn, hệ số co và số bước lặp của phương pháp
  * (Chú thích type=1 là ct lặp hậu nghiệm, type=2 là ct lặp tiên nghiệm
	     normtype=(1,2,3) lần lượt là chuẩn vô cùng, chuẩn 1, chuẩn 2 trong sách giáo khoa)
## Hướng dẫn sử dụng
* Recomend sử dụng vscode, hoặc codeblocks để sử dụng
* Để thử các trường hợp test khác hãy sửa file Equation.inp
## Phân tích ưu nhược điểm thuật toán
* Ưu điểm: 
  * Kiểm soát được sai số khi tính toán X
  * Nghiệm X0 đầu vào không bị ràng buộc
* Nhược điểm: 
  * Không thể tính được X khi ma trận có chuẩn theo cả 3 loại trên lớn hơn 1.
