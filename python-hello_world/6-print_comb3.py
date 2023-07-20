for el1 in range(0, 10):
    for el2 in range(el1 + 1, 10):
        if el1 == 8 and el2 == 9:
            print("{}{}".format(el1, el2))
        else:
            print("{}{}".format(el1, el2), end=", ")