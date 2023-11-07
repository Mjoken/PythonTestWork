from math import sqrt


def prime_numbers(low, high):
    try:
        lst = []
        for x in range(low, high):
            if all(x % t for t in range(2, int(sqrt(x)) + 1)):
                lst.append(x)
        return lst
    except NameError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []


if __name__ == '__main__':
    print(prime_numbers(9950, 10001))
