# Phương pháp xấp xỉ liên tiếp giải phương trình vi phân - Nhóm 26 - Đỗ Mạnh Dũng

## Code cần sử dụng thư viện sympy và numpy

## Hàm chính: Pica(filename) nếu làm dạng giải tích, Pica(filename, length) nếu làm dạng mảng.
## Input ví dụ:

```
t*(3-2*x)           # Hàm f(t,x)
-0.5,0.5            # khoảng của t
-1,2                # khoảng của x
0,1                 # t0, x0
10**-5              # sai số epsilon
```

## Output:
Dạng mảng: [ (t_i,x_i) ] ví dụ như [ (-1,2), (0,1), (1,-2) ]
Dạng giải tích: (f, interval) ví dụ như ( sin(t), (-1,1) )
## Đã có 5 ví dụ (1 vd như trên)
## ! Warning: chưa có modun tìm M = supf và L = supf' nên phải nhập tay ( ví dụ Pica(filename, M = 2, L =3) )
## Note: muốn vẽ đồ thị sai số có thể thêm tham số ( Pica(filename, mode = 'test') )
## Happy testing :))
