from GaussJordan_source import Gauss_Jordan_Algorithms
import numpy as np

# Lưu ý cài thư viện Numpy!!!
# Input_matrix: ma trận đầu vào chương trình
# result: ma trận output
# Gọi ma trận output: RUN.result

# Ví dụ ma trận đầu vào
input_matrix = np.array([[1, 1, -3, 2, 6], [1, -2, 0, -1, -6], [0, 1, 1, 3, 16], [2, -3, 2, 0, 6]])

try:
    RUN = Gauss_Jordan_Algorithms(input_matrix)
    RUN.main()
    print(RUN.result)
except:
    raise ValueError("Da co loi xay ra!")
