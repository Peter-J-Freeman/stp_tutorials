def addodds(A, B):
    if A == B:
        return 0
    else:
        if B % 2 == 0:
            return addodds(A, B-1)
        else:
            return B + addodds(A, B-1)


if __name__ == '__main__':
    print(addodds(50, 100))

