import numpy as np
import Bordering
a = np.loadtxt("test1.txt",dtype='float')
if(Bordering.checkdet(a) <0):
    print("Ma tran khong kha nghich")
else:
    b = np.transpose(a)
    t = b.dot(a)
    n = len(a)
    re = Bordering.bordering(t,n)
    print(re.dot(b))