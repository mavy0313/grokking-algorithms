def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2 #the floor division // rounds the result down to the nearest whole number
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
my_list2 = [0, 1, 2]

print(binary_search(my_list2, 1))
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

print(17 // 2)
