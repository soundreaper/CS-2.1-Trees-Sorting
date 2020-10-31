#!python


def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n log()n) in both average and worst case. Python's build in 'sorted' function is called Timsort (adaptive merge sort).
    TODO: Memory usage: Worst case is O(n) and best case is O(1). Timsort uses n//2 pointers and up to 2*n extra bytes which becomes n.
    """
    # TODO: Check that all adjacent items are in order, return early if so
    if items == sorted(items):
        return True
    else:
        return False


def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) in worst case and average case. Bubble sort has to one less than the length of the list each time it does a passthrough.
    It will do n-1, n-2, n-3...which eventually looks like n(n-1)/2 which if infinite summations are done simplifies to n^2.
    TODO: Memory usage: O(1) in all cases because only a single addtional memory space is needed for a temp variable for swapping values.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    n = len(items)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) in worst case and average case. Selection sort has to select the next smallest element and swap it so it 
    has 2 for loops which both access the list n and n-1 times which again leads to n^2 time complexity.
    TODO: Memory usage: O(1) in all cases because only a single addtional memory space is needed for a temp variable for swapping values.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    n = len(items)

    for i in range(n):
        min_element = i
        for j in range(i+1, n):
            if items[min_element] > items[j]:
                min_element = j

        items[i], items[min_element] = items[min_element], items[i]


def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) in worst case and average case BUT O(n) in the best case. Insertion sort selects the index 1 element and compares
    it to the subarray to the left of that index. It continues in this pattern and keeps inserting from the right into the subarray at the left
    until sorted. The reason it is O(n) in the best case is because even if a sorted array is passed in, the outer for loop to look through the
    entire list at least once will execute.
    TODO: Memory usage: O(1) in all cases because only a single addtional memory space is needed for a temp variable for swapping values.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    n = len(items)

    for i in range(1, n):
        key = items[i]

        j = i-1
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key
