import random
import time
class helperFunctions:
    def merge(self, arr1, arr2, arr):
        i=j=l=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i] < arr2[j]:
                arr[l] = arr1[i]
                i+=1
            else:
                arr[l] = arr2[j]
                j+=1
            l+=1
        while i<len(arr1):
            arr[l]= arr1[i]
            i,l=i+1,l+1
        while j<len(arr2):
            arr[l]=arr2[j]
            j,l=j+1,l+1
        return arr
    def binarySearch(self, arr:list, num):
        start,end=1,len(arr)-1
        while start < end:
            mid = (start+end)//2
            if num == arr[mid-1]:
                return mid-1
            elif num < arr[mid-1]:
                end = mid
            else:
                start = mid
            if end - start < 2:
                return end if num == arr[end] else start if num == arr[start] else None

class solutionSort(helperFunctions):
    def selectionSort(self, arr):
        start = time.time()
        for i in range(len(arr)):
            min = i
            for j in range(i,len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        print('time selectionSort =', time.time()-start)
        return arr

    def bubbleSort(self, arr):
        start = time.time()
        for i in range(len(arr)-1,0,-1):
            flag = True
            for j in range(0,i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = False
            if flag: break
        print('time BubbleSort =', time.time()-start)
        return arr

    def insertionSort(self, arr:list):
        start = time.time()
        for i in range(1,len(arr)):
            for j in range(0,i):
                if arr[i] < arr[j]:
                    arr.insert(j,arr.pop(i))
        print('time insertionSort =', time.time()-start)
        return arr

    def binaryInsertionSort(self, arr):
        start = time.time()
        for i in range(1,len(arr)):
            arr.insert(self.binarySearch(arr,arr[i]),arr.pop(i))
        print('time insertionSort =', time.time()-start)

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        return self.merge(self.mergeSort(arr[:len(arr)//2]),self.mergeSort(arr[len(arr)//2:]),arr)

    def quickSort(self, arr, st, en):
        # print(st,en)
        if en - st < 1: return
        i,j=st,en
        while i<=j:
            while arr[i] <= arr[st]:
                i+=1
                if i >= len(arr): break
            while arr[j] > arr[st]:
                j-=1
                if j<st: break
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i,j=i+1,j-1
        arr[j],arr[st]=arr[st],arr[j]
        # print(arr[st:j],arr[j],arr[j+1:en])
        self.quickSort(arr,st,j-1)
        self.quickSort(arr,j+1,en)
        return arr

if __name__ == "__main__":
    sort = solutionSort()
    arr:list = random.sample(range(-1000000, 3000000), 100)
    # arr = [6,7,9,7,2,5,5,6,8,0,2,-1,-3,-1,5,10]
    # arr.sort()
    # print(sort.bubbleSort(arr.copy()))
    # print(sort.insertionSort(arr.copy()))
    # print(sort.mergeSort(arr.copy()))

    # sort.selectionSort(arr.copy())
    # sort.bubbleSort(arr.copy())
    # sort.insertionSort(arr.copy())
    # sort.binaryInsertionSort(arr.copy())

    start = time.time()
    arr.sort()
    print('best sort time=',time.time()-start)

    start = time.time()
    sort.mergeSort(arr.copy())
    print('merge sort time=',time.time()-start)

    start = time.time()
    # print(sort.quickSort(arr.copy(), 0, len(arr)-1))
    sort.quickSort(arr.copy(), 0, len(arr)-1)
    print('quick sort time=',time.time()-start)
