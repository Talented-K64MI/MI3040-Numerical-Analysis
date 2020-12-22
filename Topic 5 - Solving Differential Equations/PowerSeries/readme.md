# Phương pháp chuỗi lũy thừa giải phương trình vi phân - Nhóm 26 - Đỗ Mạnh Dũng

## Code không cần thư viện ngoài tuy nhiên nếu sử dụng hàm Plot cần sympy

## Hàm chính: `Polynomial(string filename)`  # input là tên input file, output là `(R, mảng kết quả)` với R là bán kính hội tụ
Ví dụ `output = (3, [1,2,3])` tức là bán kính hội tụ R = 3 và hàm xấp xỉ là f = 1 + 2x^2 + 3x^3
## Input ví dụ:

```

0 3                                                                                                                     # f(0), f'(0), f''(0)
9       0     3**2     0        -3**4/3!       0           3**6/5!    0             -3**8/7!   0           3**10/9!     # lần lượt khai triển hệ số y, bậc tăng dần (3 + 6x^2 + ...)
9.5     1     0       -3**2/2    0             3**4/4!     0         -3**6/6!        0         3**8/8!     0            # khai triển hệ số y'
8       3    -3**3     0         3**5/3!       0          -3**7/5!    0              3**9/7!   0          -3**11/9!     # khai triển hệ số f

```
## Output
(R, arr) với R là bán kính hội tụ và arr là mảng hệ số của khai triển, bắt đàu từ x^0
## Đã có 1 ví dụ (như trên)
## Happy testing :))
