#Selection Sort

list_Int = [8, 2, 4, 6, 1, 9, 0, 3, 5, 7, 9]
max_Len = len(list_Int)
list_Index = 0
i = 0

while list_Index < max_Len - 1:
    for i in range(list_Index + 1, max_Len, 1):
        if list_Int[list_Index] < list_Int[i]:
            list_Int[i] = list_Int[i] + list_Int[list_Index]
            list_Int[list_Index] = list_Int[i] - list_Int[list_Index]
            list_Int[i] = list_Int[i] - list_Int[list_Index]

    list_Index += 1

print list_Int
