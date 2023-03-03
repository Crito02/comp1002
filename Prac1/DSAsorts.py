

# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods


def bubbleSort(A):
    """
    bubblesort
    args:
        A - an array to be sorted
    returns:
        A - the sorted array
    """
    b_swap = True
    while b_swap:
        b_swap = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                b_swap = True
    return A


def insertionSort(A):
    """
    insertionsort
    args:
        A - an array to be sorted
    returns:
        A - the sorted array
    """
    for i in range(1, len(A-1)):
        k = i
        temp = A[k]
        while k > 0 and A[k-1] > temp:
            A[k] = A[k-1]
            k -= 1
        A[k] = temp
    return A


def selectionSort(A):
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
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...


def mergeSortRecurse(A, leftIdx, rightIdx):
    ...


def merge(A, leftIdx, midIdx, rightIdx):
    ...


def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...


def quickSortRecurse(A, leftIdx, rightIdx):
    ...


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...
