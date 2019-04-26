def search(item, item_list):
    first = 0
    last = len(item_list) -1

    while first <= last:
        mid = (first + last) // 2
        if item_list[mid] == item:
            return mid
        else:
            if item_list[mid] < item:
                first = mid + 1
            else:
                last = mid - 1

    return -1

items = [11, 24, 45, 77, 88, 100, 115, 125]
item = 25

print(search(item, items))
