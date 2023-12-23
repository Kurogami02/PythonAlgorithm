import csv
import seaborn as sns
import numpy as np
import math

def loadData():
    f = open("D:\Office\Course\ML/BreastsData.csv")
    f2 = open("D:\Office\Course\ML/DataTest.csv")

    data = csv.reader(f) 
    data = np.array(list(data))# Chuyển dataset thành ma trận

    data2 = csv.reader(f2)
    data2 = np.array(list(data2))

    data = np.delete(data, 0, 0)# delete header
    data = np.delete(data, 0, 1) # delete index    
    data2 = np.delete(data, 0, 1)# delete header
    data2 = np.delete(data, 0, 0) # delete index    
    
    #Trộn data của 2 dataset
    np.random.shuffle(data)
    np.random.shuffle(data2) 

    f.close()
    trainSet = data[:150] # Dùng data từ 1-150 để train
    testSet = data2[:10] # Dùng data từ 1-10 để test
    return trainSet, testSet

def calcDistancs(pointA, pointB, numOfFeature=29):
    tmp = 0
    for i in range(numOfFeature):
        tmp += (float(pointA[i]) - float(pointB[i])) ** 2
    return math.sqrt(tmp)

def kNearestNeighbor(trainSet, point, k):
    distances = []
    for item in trainSet:
        distances.append({
            "label": item[-1],
            "value": calcDistancs(item, point)
        })
    distances.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distances]
    return labels[:k]

def findMostOccur(arr):
    labels = set(arr) # set label
    ans = ""
    maxOccur = 0
    for label in labels:
        num = arr.count(label)
        if num > maxOccur:
            maxOccur = num
            ans = label
    return ans

if __name__ == "__main__":
    trainSet, testSet = loadData()
    numOfRightAnwser = 0
    for item in testSet:
        knn = kNearestNeighbor(trainSet, item, 30)
        answer = findMostOccur(knn)
        numOfRightAnwser += item[-1] == answer
        print("label: {} -> predicted: {}".format(item[-1], answer))
    a = numOfRightAnwser/len(testSet)
    
    print(f"Tỉ lệ: {a:.1%}")