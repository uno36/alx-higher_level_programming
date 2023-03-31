#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    Args:
        list_of_integers: list --- a list of integers
    Return:
        Return a peak value if found. Otherwise, return None.
    """
    mid = int(len(list_of_integers) / 2)
    if mid - 1 >= 0 and mid + 1 <= len(list_of_integers) - 1:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        elif list_of_integers[len(list_of_integers) - 1] > list_of_integers[
                len(list_of_integers) - 2]:
            return list_of_integers[len(list_of_integers) - 1]
        elif (list_of_integers[mid] == list_of_integers[mid - 1]) and (
                list_of_integers[mid] == list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif (list_of_integers[mid] > list_of_integers[mid - 1]) and (
                list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            return find_peak(list_of_integers[0:mid + 1])
        elif list_of_integers[mid - 1] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid: len(list_of_integers)])
    else:
        return None
