import n1 as n1


def greater(n1, n2):
    return max(n1, n2)


def maxi(n1, n2, n3, n4):
    maximum = n1
    if n2 > n1:
        maximum = n2
        if n3 > n2:
            maximum = n3
            if n4 > n3:
                maximum = n4
                return maximum


str(n1, n2, n3, n4)

