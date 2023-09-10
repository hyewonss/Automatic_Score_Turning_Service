import math


def bhattacharyya(a, b):
    """ Bhattacharyya distance between distributions (lists of floats). """
    if not len(a) == len(b):
        raise ValueError("a and b must be of the same size")
    return -math.log(sum((math.sqrt(u * w) for u, w in zip(a, b))))


x = bhattacharyya([0.1, 0.9], [0.1, 0.9])
print(x)

x = bhattacharyya([0.2, 0.8], [0.5, 0.5])
print(x)

x = bhattacharyya([0.1, 0.9], [0.5, 0.5])
print(x)