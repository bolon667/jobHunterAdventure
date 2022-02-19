import random

def QuickSort(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        splitNum = random.choice(Arr)
        LowArr = []
        MedArr = []
        HighArr = []
        for elem in Arr:
            if elem < splitNum:
                LowArr.append(elem) 
            elif elem > splitNum: 
                HighArr.append(elem) 
            else: 
                MedArr.append(elem)
        return QuickSort(LowArr) + MedArr + QuickSort(HighArr)

print(QuickSort([5,32,123,65,1,2,3,5,5,5,21,1]))