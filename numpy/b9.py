import numpy as np
a = np.array([1, np.nan, 3, 4])
print("var = ", np.var(a))
print("std = ", np.std(a))
print("nanvar = ", np.nanvar(a))
print("nanstd = ", np.nanstd(a)) #tương tự mean và median, NumPy cũng cho chúng ta các hàm để bỏ qua các phần tử nan
#Out var =  nan
    #std =  nan
    #nanvar =  1.5555555555555554
    #nanstd =  1.247219128924647