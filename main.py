def bubbleSort(aList):
    n = len(aList)

    for i in range(n-1):
        flag = 0

        for j in range(n-1):
            if aList[j] > aList[j+1]:
                tmp = aList[j]
                aList[j] = aList[j+1]
                aList[j+1] = tmp
                flag = 1

        if flag == 0:
            break

    return aList

elements =[26,13,45,8,98,35]
result = bubbleSort(elements)
print("Unsorted Elements")
print(elements)
print()
print("Sorted elements")
print(result)