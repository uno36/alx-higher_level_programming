#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result = 0
    tmp = 0
    while True:
        try:
            for i in range(tmp, list_length):
                result = my_list_1[i] / my_list_2[i]
                new.append(result)
            return new
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
            tmp = i + 1
            pass
        except TypeError:
            print("wrong type")
            tmp = i + 1
            new.append(0)
            pass
        except IndexError:
            print("out of range")
            tmp = i + 1
            new.append(0)
            pass
        finally:
            pass
