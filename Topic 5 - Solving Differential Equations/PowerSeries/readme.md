# Phương pháp chuỗi lũy thừa giải phương trình vi phân - Nhóm 26 - Đỗ Mạnh Dũng

## Code không cần thư viện ngoài tuy nhiên nếu sử dụng hàm Plot cần sympy

## Hàm chính: Polynomial(string filename)   # input là tên input file, output là (R, mảng kết quả) với R là bán kính hội tụ
Ví dụ output = (3, [1,2,3]) tức là bán kính hội tụ R = 3 và hàm xấp xỉ là f = 1 + 2x**2 + 3x**3
## Input ví dụ:
-1    1  0            # lần lượt f(0), f'(0), f''(0)

3 6 0 0    0 0 0      # khai triển hệ số y', bậc tăng dần (3 + 6x**2 + ...)

2 0 -2 0 0 0 0        # khai triển hệ số y''

1 0 0   -0.666 0 0 0  # khai triển hệ số y'''

## Đã có 1 ví dụ (như trên)

## Happy testing :))
