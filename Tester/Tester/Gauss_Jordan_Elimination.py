from GaussJordan_source import Gauss_Jordan_Algorithms

try:
    RUN = Gauss_Jordan_Algorithms()
    RUN.main()
except:
    f = open("GJ_output.txt", "w")
    f.write("Da co loi xay ra!")
    f.close()
