# -*- coding: cp1251 -*-
import datetime

def sort1(sort_arr1):
    if len(sort_arr1) > 1:
        mid = len(sort_arr1) // 2
        left_half = sort_arr1[:mid]
        right_half = sort_arr1[mid:]

        sort1(left_half)
        sort1(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_arr1[k] = left_half[i]
                i += 1
            else:
                sort_arr1[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            sort_arr1[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            sort_arr1[k] = right_half[j]
            j += 1
            k += 1
            
    return sort_arr1        

def sort2(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    lis_length = max(lis)
    sort_arr = [0] * lis_length
    indx = lis_length - 1

    for i in range(n - 1, -1, -1):
        if lis[i] == lis_length:
            sort_arr[indx] = arr[i]
            indx -= 1
            lis_length -= 1

    return sort_arr

arr = [38, 27, 43, 3, 9, 82, 10, 109, 1, 17, 55, 66, 156, 2,
       37, 26, 42, 8, 7, 81, 100, 108, 200, 16, 54, 65, 155, 300,
       36, 25, 41, 170, 99, 80, 101, 110, 117, 53, 64, 766, 256, 221,
       35, 24, 40, 171, 98, 79, 102, 111, 118, 52, 63, 666, 356, 222,
       34, 23, 39, 172, 97, 78, 103, 112, 119, 51, 62, 566, 456, 223,
       33, 22, 139, 173, 96, 77, 104, 113, 120, 50, 61, 466, 556, 224,
       32, 21, 138, 174, 95, 76, 105, 114, 121, 49, 60, 366, 656, 225,
       31, 20, 137, 175, 94, 75, 106, 115, 122, 47, 59, 266, 756, 226,
       30, 19, 136, 176, 93, 74, 107, 116, 123, 46, 58, 166, 856, 227]
start = datetime.datetime.now()
sort_arr1 = sort1(arr)
end = datetime.datetime.now()
print("Отсортированный массив:", sort_arr1)
print("Время работы:", end.microsecond-start.microsecond)
start = datetime.datetime.now()
sort_arr2 = sort2(arr)
end = datetime.datetime.now()
print("Отсортированныймассив :", sort_arr2)
print("Время работы:", end.microsecond-start.microsecond)