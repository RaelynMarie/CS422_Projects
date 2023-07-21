# Question 1 Solution
def sequence(m, n):
    solution = []  # holds the solution answer
    tmpList = []  # 
    tmpList.extend(str(m))

    i = 1

    while i <= n:
        tmpCount = 1
        tmpStr = ''
        if len(tmpList) == 1:
            tmpStr = tmpStr + str(tmpCount) + str(m)
            strInt = int(tmpStr)
            solution.append(strInt)
        else:
            for j in range(0, len(tmpList)):
                if j != (len(tmpList) - 1) and tmpList[j + 1] == tmpList[j]:
                    tmpCount += 1
                else:
                    tmpStr = tmpStr + str(tmpCount) + tmpList[j]
            strInt = int(tmpStr)
            solution.append(strInt)
        i += 1
        tmpList.clear()
        tmpList.extend(tmpStr)
    return solution

# Question 2 Solution
def listCompare(listA, listB):
    if listA == listB:
        print("The lists are equal.")
    elif (len(listA) < len(listB)) and all(x in listB for x in listA):
        print("A is the sublist of B.")
    elif (len(listA) > len(listB)) and all(x in listA for x in listB):
        print("A is a superlist of B.")
    else:
        print("A and B are not equal.")

A = [1, 2, 3]
B = [1, 3, 2]
listCompare(A, B)