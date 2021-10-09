import numpy as np
x = np.array([[14, 96],
               [46, 82],
               [80, 67],
               [77, 91],
               [99, 87]])
 
print("X = ", x)
 
print("Giá trị lớn nhất: ", np.amax(x))
print("Giá trị bé nhất: ", np.amin(x))
 
print("Giá trị lớn nhất (axis = 0): ", np.amax(x, axis=0))
print("Giá trị lớn nhất (axis = 1): ", np.amax(x, axis=1))
#Out: X =  [[14 96]
    # [46 82]
    # [80 67]
    # [77 91]
    # [99 87]]
    #Giá trị lớn nhất:  99
    #Giá trị bé nhất:  14
    #Giá trị lớn nhất (axis = 0):  [99 96]
    #Giá trị lớn nhất (axis = 1):  [96 82 80 91 99]


x = np.array([[14, 96], #bỏ qua các phần tử nan
               [np.nan, 82],
               [80, 67],
               [77, np.nan],
               [99, 87]])
 
 
print("Giá trị lớn nhất: ", np.nanmax(x))
print("Giá trị bé nhất: ", np.nanmin(x)) 
#Out: X =  [[14. 96.]
    # [nan 82.]
    # [80. 67.]
    # [77. nan]
    # [99. 87.]]
    #Giá trị lớn nhất:  99.0
    #Giá trị bé nhất:  14.0


print("Range = ", np.ptp(x)) #Phạm vi giá trị max - min trong một dãy số 
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))
#Out: x =  [[14 96]
    # [46 82]
    # [80 67]
    # [77 91]
    # [99 87]]
    #Range =  85
    #Range (axis = 0) =  [85 29]
    #Range (axis = 1) =  [82 36 13 14 12]