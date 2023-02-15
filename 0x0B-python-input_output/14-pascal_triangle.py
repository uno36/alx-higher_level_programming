#!/usr/bin/python3
def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n
    Args:
        n: the size of triangle
    Return:
        return a matrix of pascal's triangle
    """
    p_tri = [[1]]
    list = [1, 1]

    if n <= 0:
        return []
    for i in range(1, n):
        prev_list = list
        list = [1]
        for j in range(0, i-1):
            list.append(prev_list[j] + prev_list[j + 1])
        list.append(1)
        p_tri.append(list)
    return p_tri
