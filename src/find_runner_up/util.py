def unique_value(arr):
    n = int(input())
    arr = map(int, input().split())
    unique_numbers = list(set(arr))
    b=sort_value(unique_numbers)
    return b

def sort_value(a):
    sorted_num = sorted(a)
    return sorted_num




