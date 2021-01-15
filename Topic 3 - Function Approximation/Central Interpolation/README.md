# Nhóm 18 - Lê Thị Vân Anh, Lê Nguyên Bách
# Công thức nội suy trung tâm
## Input, output
* Input: 
   * Mảng arr_x (Dòng 174): Chứa các giá trị hoành độ của bảng số liệu
   * Mảng arr_y (Dòng 175): Chứa các giá trị tung độ của bảng số liệu
   * x (Dòng 176): Cần tính giá trị xấp xỉ của f(x) 
* Output: Giá trị xấp xỉ của f(x), in kèm theo sai số của giá trị đó
* Error: Trả về "None" và in ra "Giá trị x nằm ngoài khoảng nội suy" nếu như giá trị x nhập vào không nằm trong khoảng nội suy
## Hướng dẫn sử dụng
* Khuyến khích sử dụng Pycharm
* Thay đổi các mảng arr_x hoặc arr_y hoặc x ở các dòng 182 -> 184 nếu muốn đổi giá trị đầu vào (Lưu ý: độ dài của hai mảng arr_x và arr_y phải bằng nhau, mảng arr_x phải có các phần tử cách đều và tăng dần)
* Để chạy các chương trình nội suy:
   * Với công thức Stirling: 
      * Uncomment dòng 186 để chạy chương trình
      * Uncomment các dòng từ 95 -> 100 để theo dõi các giá trị trung gian
   * Với công thức Bessel: 
      * Uncomment dòng 187 để chạy chương trình
      * Uncomment các dòng từ 168 -> 173 để theo dõi các giá trị trung gian
## Ưu điểm, nhược điểm
* Ưu điểm:
   * Việc lấy một mốc nội suy gần nhất làm mốc đầu tiên, sau đó quét qua các mốc nội suy có tính đối xứng với mốc nội suy trung tâm nên bất cứ giá trị nào cũng có thể được quét qua, tăng độ tin tưởng cho kết quả đầu ra
   * Việc trích ra số lượng mốc nội suy vừa phải (Đối với Stirling tối đa là 9, còn với Bessel tối đa là 8) đã giảm thiểu được phần nào khối lượng tính toán, mà vẫn đem lại kết quả có độ chính xác cao
   * Công thức nội suy trung tâm thường được ưu tiên sử dụng đối với những bài toán xấp xỉ hàm số có mốc cách đều, không như những phương pháp khác, chỉ ưu tiên về một phí
   * Phương pháp đưa về tính toán ma trận giúp cho đa thức nội suy dễ kiểm soát hơn, không như cách tính bằng đệ quy thông thường. Chẳng hạn nếu ta muốn tính gần đúng đạo hàm hoặc tích phân của một hàm số, ta có thể xấp xỉ hàm số đó bằng một đa thức, rồi đạo hàm (tích phân) đa thức đó một cách dễ dàng
* Nhược điểm
   * Công thức nội suy không xử lý được đối với trường hợp giá trị x nằm ở (gần) đầu bảng
   * Phương pháp đưa về ma trận tuy lợi về tính toán nhưng thiệt nhiều về bộ nhớ