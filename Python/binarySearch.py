def binarySearchRecursion(list, num, i, j):
    if i > j:
        return -1
    mid =(j+i)//2
    if num == list[mid]:
        return mid
    elif num > list[mid]:
        return binarySearchRecursion(list,num, mid+1, j)
    else:
        return binarySearchRecursion(list, num, i, mid-1)
def binarySearchIterative(list, num, i=0, j=0):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = (end+start)//2
        # print(mid,start,end)
        # if start == end and num != list[mid]:
        #     return -1
        if num == list[mid]:
            return mid
        elif num > list[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

if __name__ == '__main__':
    list = [0,1,2,7,9]

    print(binarySearchRecursion(list, 0, 0, len(list)))
    print(binarySearchRecursion(list, 1, 0, len(list)))
    print(binarySearchRecursion(list, 2, 0, len(list)))
    print(binarySearchRecursion(list, 8, 0, len(list)))
    print(binarySearchRecursion(list, 9, 0, len(list)))

    print(binarySearchIterative(list, 0, 0, len(list)))
    print(binarySearchIterative(list, 1, 0, len(list)))
    print(binarySearchIterative(list, 2, 0, len(list)))
    print(binarySearchIterative(list, 8, 0, len(list)))
    print(binarySearchIterative(list, 9, 0, len(list)))