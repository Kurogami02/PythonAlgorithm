import numpy as np
x = np.array([2, np.nan, 5, 9])
print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))
#Out: mean =  5.333333333333333
    #median =  5.0
print("mean = ", np.mean(x))
print("median = ", np.median(x)) #nếu khai báo bình thường thì kq sẽ trả về nan
#Out mean =  nan
    #median =  nan