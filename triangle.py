for a in range(10):
    for _ in range(a + 1):
        print("#", end=" ")
    for _ in range(10 - a):
        print(" ", end=" ")
    for _ in range(10 - a):
        print("#", end=" ")
    for _ in range(a + 1):
        print(" ", end=" ")
    for _ in range(a + 1):
        print(" ", end=" ")
    for _ in range(10 - a):
        print("#", end=" ")
    for _ in range(10 - a):
        print(" ", end=" ")
    for _ in range(a + 1):
        print("#", end=" ")
    print()
