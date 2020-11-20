#!python
from collections import defaultdict
from sorting_iterative import insertion_sort
import math
from random import randint

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    m = max(numbers) + 1
    count = [0] * m
    
    for num in numbers:
        count[num] += 1
    
    write_pos = 0
    for write_val in range(m):
        for _ in range(count[write_val]):
            numbers[write_pos] = write_val 
            write_pos += 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    max_value = max(numbers)
    d_buckets = int(math.sqrt(len(numbers)))

    if num_buckets is None:
        buckets = [[] for _ in range(d_buckets)]
    else:
        buckets = [[] for _ in range(num_buckets)]

    for num in numbers:
        index = int(num / max_value * (d_buckets - 1))
        bucket = buckets[index]
        bucket.append(num)
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    write_index = 0
    for bucket in range(len(buckets)):
        for value in buckets[bucket]:
            numbers[write_index] = value
            write_index += 1