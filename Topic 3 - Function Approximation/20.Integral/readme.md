thay đổi hàm f ở cuối code

Các tham số:
n: cấp của tích phân newton-cotez muốn sử dụng (1 là hình thang, 2 là simpson, 3 đừng dùng, 4 có cấp hội tụ h^5)
M: supremum của đạo hàm cấp n   // ko cần tính chính xác, có chặn trên cho nó là được
epsilon: sai số

a,b: khoảng tính tích phân

// Hàm sử dụng: Integral(f, M, (a,b), epsilon, n)
