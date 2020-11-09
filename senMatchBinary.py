# merge function to merge 2 sorted lists together, used with mergeSort()
def merge(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    return merged + list1[i:] + list2[j:]

# recursive merge sort algorithm to sort a list in O(nlogn) time
def mergeSort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return merge(left, right)

# binary search function to search the sorted list of sentences
def binarySearch(alist, start, end, val):
    if start >= end:
        return alist[start] == val
    
    mid = (start + end) // 2
    if alist[mid] == val:
        return True
    else:
        if alist[mid] < val:
            return binarySearch(alist, mid+1, end, val)
        else:
            return binarySearch(alist, start, mid-1, val)

# searches for sentence matches using binary search
def getBinarySim(data1, data2):
    # sort data2
    data2 = mergeSort(data2)

    count = 0
    # loop through data1 and use binarySearch() to check for a matching sentence and increment count if a match is found
    for i in data1:
        if binarySearch(data2, 0, len(data2)-1, i):
            count += 1

    sim = count / len(data1) * 100
    return sim