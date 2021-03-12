import math


def get_gamma(a, b, c):
    if all(x > 0 for x in (a, b, c)) and a + b >= c and b + c >= a and c + a >= b:
        gamma = math.degrees(math.acos(((a ** 2) + (b ** 2) - (c ** 2))/(2 * a * b)))
        return gamma
    else:
        return -1


def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_gamma() and will completely ignore the main function!
    """

    side_1 = float(input("What is the length of the first side?\n"))
    side_2 = float(input("What is the length of the second side?\n"))
    side_3 = float(input("What is the length of the third side?\n"))

    gamma = get_gamma(side_1, side_2, side_3)

    if gamma != -1:
        print("Side lengths {}, {}, and {} yield a {} value for angle gamma.".format(side_1, side_2, side_3, gamma))
    else:
        print("Side lengths {}, {}, and {} are invalid.".format(side_1, side_2, side_3))


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
