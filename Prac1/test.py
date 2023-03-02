def selectionsort(A):
    """ selectionsort
    args:
        A - an array to be sorted
    returns:
        A - the sorted array
    """
    for i in range(len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A

def mergeSort(A):
    """ mergesort
    args:
        A - an array to be sorted
    returns:
        A - the sorted array
    """
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A

def mergeSortRecurse(A, leftIdx, rightIdx):
    """ mergeSortRecurse - recursive algorithm for mergeSort
    """
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx+1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    """ merge - merge two sorted sub-arrays into a single sorted array
    """
    L = A[leftIdx:midIdx+1]
    R = A[midIdx+1:rightIdx+1]
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurse(A, 0, len(A)-1)

def quickSortRecurse(A, leftIdx, rightIdx):
    """ quickSortRecurse - recursive algorithm for quickSort
    """
    if leftIdx < rightIdx:
        pivotIdx = doPartition(A, leftIdx, rightIdx)
        quickSortRecurse(A, leftIdx, pivotIdx-1)
        quickSortRecurse(A, pivotIdx+1, rightIdx)

def doPartition(A, leftIdx, rightIdx):
    """ partition - partition the array into two sub-arrays
    """
    pivotIdx = leftIdx
    pivot = A[pivotIdx]
    i = leftIdx + 1
    j = rightIdx
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[pivotIdx], A[j] = A[j], A[pivotIdx]
    return j
