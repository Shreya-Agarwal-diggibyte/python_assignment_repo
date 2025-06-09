def piling_up(a):
    results = []
    for cubes in a:
        last = float('inf')
        l, r = 0, len(cubes) - 1
        possible = True
        while l <= r:
            if cubes[l] >= cubes[r]:
                pick = cubes[l]
                l += 1
            else:
                pick = cubes[r]
                r -= 1
            if pick <= last:
                last = pick
            else:
                possible = False
                break
        results.append("Yes" if possible else "No")

    return results