#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    items = 0

    while items < list_length:
        quotient = 0
        try:
            quotient = my_list_1[items] / my_list_2[items]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            result_list.append(quotient)
            items = items + 1
    return result_list
