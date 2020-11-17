#!python

from sorting import random_ints
from sorting_recursive import merge_sort, quick_sort
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort

sort = quick_sort


def test_is_sorted_on_sorted_integers():
    # Positive test cases (examples) with lists of sorted integers
    assert is_sorted([]) is True  # Empty lists are vacuously sorted
    assert is_sorted([3]) is True  # Single item is trivially sorted
    assert is_sorted([3, 4]) is True  # Duplicate items are in order
    assert is_sorted([3, 5]) is True
    assert is_sorted([3, 5, 7]) is True

    assert is_sorted([3, 5, 7, 9]) is True


def test_is_sorted_on_unsorted_integers():
    # Negative test cases (counterexamples) with lists of unsorted integers
    assert is_sorted([5, 3]) is False
    assert is_sorted([3, 5, 2]) is False
    assert is_sorted([7, 5, 3]) is False

    assert is_sorted([7, 5, 3, 4]) is False


def test_is_sorted_on_sorted_strings():
    # Positive test cases (examples) with lists of sorted strings
    assert is_sorted(['A']) is True  # Single item is trivially sorted
    assert is_sorted(['A', 'B']) is True  # Duplicate items are in order
    assert is_sorted(['A', 'C']) is True
    assert is_sorted(['A', 'B', 'C']) is True

    assert is_sorted(['A', 'B', 'C', 'D', 'E']) is True


def test_is_sorted_on_unsorted_strings():
    # Negative test cases (counterexamples) with lists of unsorted strings
    assert is_sorted(['B', 'A']) is False
    assert is_sorted(['D', 'A', 'C']) is False
    assert is_sorted(['C', 'B', 'A']) is False

    assert is_sorted(['C', 'B', 'A', 'Z']) is False


def test_sort_on_empty_list():
    items = []
    sort(items)
    assert items == []  # List should not be changed


def test_sort_on_small_lists_of_integers():
    items1 = [3]
    sort(items1)
    assert items1 == [3]  # List should not be changed
    items2 = [5, 3]
    sort(items2)
    assert items2 == [3, 5]  # List should be in sorted order
    items3 = [5, 7, 3]
    sort(items3)
    assert items3 == [3, 5, 7]

    items4 = [6, 2, 7, 8]
    sort(items4)
    assert items4 == [2, 6, 7, 8]


def test_sort_on_lists_of_random_integers():
    # Generate list of 10 random integers from range [1...20]
    items1 = random_ints(10, 1, 20)
    sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
    sort(items1)  # Call mutative sort function to sort list items in place
    assert items1 == sorted_items1

    # Generate list of 20 random integers from range [1...50]
    items2 = random_ints(20, 1, 50)
    sorted_items2 = sorted(items2)  # Copy
    sort(items2)  # Mutate
    assert items2 == sorted_items2

    # Generate list of 30 random integers from range [1...100]
    items3 = random_ints(30, 1, 100)
    sorted_items3 = sorted(items3)  # Copy
    sort(items3)  # Mutate
    assert items3 == sorted_items3

    # Generate list of 100 random integers from range [1...100]
    items4 = random_ints(100, 1, 100)
    sorted_items4 = sorted(items4)  # Copy
    sort(items4)  # Mutate
    assert items4 == sorted_items4


def test_sort_on_small_lists_of_strings():
    items1 = ['A']
    sort(items1)
    assert items1 == ['A']  # List should not be changed
    items2 = ['B', 'A']
    sort(items2)
    assert items2 == ['A', 'B']  # List should be in sorted order
    items3 = ['B', 'C', 'A']
    sort(items3)
    assert items3 == ['A', 'B', 'C']

    items4 = ['B', 'C', 'X', 'A', 'Z']
    sort(items4)
    assert items4 == ['A', 'B', 'C', 'X', 'Z']


def test_sort_on_fish_book_title():
    items = 'one fish two fish red fish blue fish'.split()
    sorted_items = sorted(items)  # Create a copy of list in sorted order
    sort(items)  # Call mutative sort function to sort list items in place
    assert items == sorted_items


def test_sort_on_seven_dwarf_names():
    items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    sorted_items = sorted(items)  # Copy
    sort(items)  # Mutate
    assert items == sorted_items

"""
def test_sort_on_tolstoy_war_and_peace():
    items = But Count Rastopchin, who now shamed those who were leaving, now evacuated government offices, now 
    distributed good-for-nothing weapons among the drunken riffraff, now took up icons, now forbade Augustin to 
    evacuate relics and icons, now confiscated all private carts, now transported the hot-air balloon constructed by 
    Leppich on a hundred and thirty-six carts, now hinted that he would burn Moscow, now told how he had burned his own 
    house and wrote a proclamation to the French in which he solemnly reproached them for destroying his orphanage; 
    now he assumed the glory of having burned Moscow, now he renounced it, now he ordered the people to catch all the 
    spies and bring them to him, now he reproached the people for it, now he banished all the French from Moscow, now 
    he allowed Mme Aubert-Chalmet, the center of all the French population of all Moscow, to remain in the city and 
    ordered the old and venerable postmaster general Klyucharev, who had done nothing particularly wrong, to be 
    arrested and exiled; now he gathered the people on the Three Hills to fight the French, now, in order to be rid of 
    those same people, he turned them loose to murder a man and escaped through a back gate himself; now he said he would 
    not survive the misfortune of Moscow, now he wrote French verses in an album about his part in the affair—this man did 
    not understand the meaning of the event that was taking place, but only wanted to do something himself, to astonish someone 
    or other, to accomplish something patriotically heroic, and, like a boy, frolicked over the majestic and inevitable event 
    of the abandoning and burning of Moscow, and tried with his little hand now to encourage, now to stem the flow of the enormous 
    current of people which carried him along with it.replace(',', '').split()
    # One of the longest sentences ever written, testing just for fun :)
    sorted_items = sorted(items)  # Copy
    sort(items)  # Mutate
    assert items == sorted_items
"""