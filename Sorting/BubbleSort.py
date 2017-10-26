#Bubble Sort

list_Int = [8, 2, 4, 6, 1, 9, 0, 3, 5, 7, 9]
max_Len = len(list_Int)
i = max_Len
list_Index = max_Len

while list_Index > 1:
    for i in range(max_Len - 1, 0, -1):

        if list_Int[i - 1] < list_Int[i]:
            list_Int[i] = list_Int[i -1] + list_Int[i]
            list_Int[i - 1] = list_Int[i] - list_Int[i - 1]
            list_Int[i] = list_Int[i] - list_Int[i - 1]

    list_Index -= 1

print (list_Int)



