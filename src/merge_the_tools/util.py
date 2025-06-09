def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        t = string[i:i + k]
        unique_value = set()
        d_result = []
        for j in t:
            if j not in unique_value:
                d_result.append(j)
                unique_value.add(j)
        result.append(''.join(d_result))
    return result




