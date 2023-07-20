for el in range(100):
    if el == 99:
        print("{}".format(el))
    else:
        print("{:02}".format(el), end=", ")
