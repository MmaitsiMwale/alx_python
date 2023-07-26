
def no_c(my_string):
    return my_string.translate({ord(c): "" for c in "cC"})
