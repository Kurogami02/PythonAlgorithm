import numpy as np

scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])
 
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='lower'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='higher'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='linear'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='nearest'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='midpoint'))
#Out: Bách phân vị thứ 70:  7
    #Bách phân vị thứ 70:  8
    #Bách phân vị thứ 70:  7.299999999999999
    #Bách phân vị thứ 70:  7
    #Bách phân vị thứ 70:  7.5

print("Bách phân vị thứ 50: ", np.percentile(scores, 50)) 
print("Median = ", np.median(scores))
#trung vị là giá trị giữa của dãy số, vì vậy bách phân vị thứ 50 là median của dãy số:
#Out: Bách phân vị thứ 50:  5.5
    #Median =  5.5


print("Q1 = : ", np.quantile(scores, 0.25))
print("Q2 = : ", np.quantile(scores, 0.5))
print("Q3 = : ", np.quantile(scores, 0.75))
#Tứ phân vị (Quartiles) chính là Bách phân vị được chia thành 3 phần (Q1 => Q3) bằng nhau
#Out: Q1 = :  4.0
    #Q2 = :  5.5
    #Q3 = :  8.0