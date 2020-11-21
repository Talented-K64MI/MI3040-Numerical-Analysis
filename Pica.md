Xấp xỉ liên tiếp Pica nhóm 26 - Đỗ Mạnh Dũng

Lưu ý code có sử dụng thư viện sympy và numpy, cần cài đặt trước khi sử dụng code này

2 hàm chính:
Pica(string filename)               # input tên file và output hàm có dạng giải tích x(t) cùng với khoảng xác định t
Pica(string filename, int length)   # input thêm length là số điểm chia cho hàm lưới x(t), output là danh sách gồm các (t,x(t))

input file ví dụ:
#t^2+x^2    # hàm f(t,x)
#-10,10     # khoảng xác định theo t
#-10,10     # khoảng xác định theo x
#0,0        # t0 và x0 = x(t0)
#10^-10     # sai số epslon

3 hàm vẽ đồ thị cho output
#PlotSymbol((function, interval))
#PlotPairs(listOfPairs)
#PlotBoth((function, interval), listOfPairs )


Đã có 1 ví dụ sẵn trong phần code

Happy testing :))
