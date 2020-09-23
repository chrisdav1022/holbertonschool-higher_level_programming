#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nml = []
    i = 0

    for j in range(list_length):
        try:
            i = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            i = 0
        except ZeroDivisionError:
            print("division by 0")
            i = 0
        except IndexError:
            print("out of range")
            i = 0
        finally:
            nml.append(i)
    return nml
