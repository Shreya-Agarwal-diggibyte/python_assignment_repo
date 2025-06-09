def no_idea(n, m, array, A, B):
    A = set(A)
    B = set(B)
    happiness = 0
    for num in array:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness
