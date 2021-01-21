# Phương pháp lặp đơn - Nhóm 5 - Đặng Trần Tiến, Vũ Đinh Trường An
    
## Input & output của chương trình
* Input: điểm ban đầu `x0`, sai số mong muốn  `𝜀`, hàm số `g(x)` (sau khi biến đổi từ `f(x) = 0 <=> g(x) = x`)
* Output: nghiệm của phương trình (chính xác hoặc với sai số chấp nhận được `𝜀` ban đầu thỏa mãn điều kiện co)
## Hướng dẫn sử dụng
- Uncomment dòng 10-13, nhập hàm `g(x)` vào sau return (; để kết thúc hàm)
- Dịch chương trình `singleloop.cpp` và làm theo hướng dẫn trong chương trình 
## Phân tích ưu nhược điểm so với các phương pháp khác:
* Ưu điểm : có thể chọn xấp xỉ đầu x_0 bất kì trong `[a,b]`, thuật toán đơn giản
* Nhược điểm : không có phương pháp tổng quát đưa phương trình `f(x) = 0` về phương trình `x = g(x)`. Phương pháp lặp đơn chỉ giải được phương trình có sẵn dạng `x = g(x)` hoặc đưa được về dạng này, thoả mãn điều kiện co. 

## Phụ lục: Hướng dẫn nhập các hàm có dạng (đa thức)^(số thực) 
Ví dụ nhập hàm `g(x)=(3x+2)^(1/3)`


`double g(double x)`
`{`
`double mu=(double) 1/3;			 // nhap so mu`
`double t=3*x+2; 				//nhap co so`
`if (t<0) return -exp((log(-t)*mu));	//tra ve ham` 
`else`	
`return exp((log(t)*mu)); 			//tra ve ham`
`}`

 

