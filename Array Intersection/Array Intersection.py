def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
 
list1 = [10, 20, 30, 40, 50]
list2 = [5, 40, 15, 25, 10, 20, 5]
print(intersection(list1, list2))