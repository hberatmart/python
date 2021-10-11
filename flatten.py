listt = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
newFuncList = []

def funcInstance(funcList):
    if len(funcList) == 1 and not isinstance(funcList[0], list):
        newFuncList.append(funcList[0])
        return 1

    for i in range(len(funcList)):

        if isinstance(funcList[i], list):
            funcInstance(funcList[i])

        else:
            newFuncList.append(funcList[i])

funcInstance(listt)
print(newFuncList)