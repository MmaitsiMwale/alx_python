
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("$")
    for i in matrix:
        for j, el in enumerate(i):
            if j == len(i) - 1:
                print("{:d}$".format(el), end="\n")
            else:
                print("{:d} ".format(el), end="")
