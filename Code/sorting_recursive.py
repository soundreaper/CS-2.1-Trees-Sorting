#!python
from random import randint


def merge(items1, items2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(m + n) because we have to add the smaller list to the merged array list and the remainder.
    TODO: Memory usage: O(m + n) because we have the length of the two input lists.
    """
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    i = j = 0
    merged_list = []

    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            merged_list.append(items1[i])
            i += 1
        else:
            merged_list.append(items2[j])
            j += 1
    
    while i < len(items1):
        merged_list.append(items1[i])
        i += 1
    
    while j < len(items2):
        merged_list.append(items2[j])
        j += 1

    return merged_list

def merge_sort(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n logn) because merging takes O(n) time and there are a lot of splits.
    TODO: Memory usage: O(n logn) because the merging process creates a new variable each time.
    """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) > 1:
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1


def partition(items, start, end):
    """
    Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (first item in the array) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Best case running time: O(n) when the pivot is the center.
    TODO: Average case running time: O(n logn) when the pivot is sometimes the center.
    TODO: Worst case running time: O(n^2) when the pivot is the lowest or highest element.
    TODO: Memory usage: O(1) since everything is done in place and we don't create a new list.
    """
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_index = randint(start, end)
    items[pivot_index], items[start] = items[pivot_index], items[start]

    pivot = items[start]
    low = start + 1
    high = end

    while True:
        while low <= high and items[high] >= pivot:
            high -= 1
        while low <= high and items[low] <= pivot:
            low += 1
        
        if low <= high:
            items[low], items[high] = items[high], items[low]
        else:
            break
    
    items[start], items[high] = items[high], items[start]
    return high


def quick_sort(items, low=None, high=None):
    """
    Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n) when the pivot is the center.
    TODO: Average case running time: O(n logn) when the pivot is sometimes the center.
    TODO: Worst case running time: O(n^2) when the pivot is the lowest or highest element.
    TODO: Memory usage: O(logn) since everything is done in place however the call stack does use memory.
    """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    
    if low < high:
        p = partition(items, low, high)
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)