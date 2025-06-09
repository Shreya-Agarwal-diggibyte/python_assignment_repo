from itertools import combinations
def iterables():
    string_len = int(input())
    element_of_list = input().split()
    K = int(input())

    Combo = list(combinations(element_of_list, K))
    F = filter(lambda c: 'a' in c, Combo)
    return(len(list(F))/len(Combo))