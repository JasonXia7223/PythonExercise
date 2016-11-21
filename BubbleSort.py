#Bubble Sort

list_Int = [8, 2, 4, 6, 1, 9, 0, 3, 5, 7]
max_Len = len(list_Int)
i = max_Len
list_Index = max_Len

while list_Index > 0:
    for i in range(max_Len, 5, -1):
        if list_Int[i - 1] < list_Int[i]:
            list_Int[i] = list_Int[i -1] + list_Int[i]
            list_Int[i - 1] = list_Int[i] - list_Int[i - 1]
            list_Int[i] = list_Int[i] - list_Int[i - 1]

    print list_Index, max_Len, list_Int
    list_Index -= 1



