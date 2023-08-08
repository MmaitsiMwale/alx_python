#!/usr/bin/python3

from rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    print(r1.id)

    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()
    print(r1)
