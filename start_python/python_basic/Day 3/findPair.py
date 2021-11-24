def find_pair(A, sum):
    i, j = 0, len(A)-1
    result = []
    while i < j:
        s = A[i] + A[j]
        if s == sum:
            result.append((A[i],A[j]))
            j -= 1
        elif s < sum:
            i += 1
        else:
            j -= 1
    return result