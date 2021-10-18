listt = [[1, 2], [3, 4], [5, 6, 7]]
newList = []
for i in range(len(listt)):
    if isinstance(listt[i], list):
        newList.append(listt[i][::-1])
    else:
        newList.append(listt[i])
print(newList[::-1])
