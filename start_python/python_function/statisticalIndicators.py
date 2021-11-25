
def mean(list_a):
    return sum(list_a)/len(list_a)
    
def median(list_a):
    # Median of list
    # Using loop + "~" operator
    list_a.sort()
    mid = len(list_a) // 2
    res = (list_a[mid] + list_a[~mid]) / 2

    # Printing result
    print("Median of list is : " + str(res))

from collections import Counter
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
                if count == max_count]

A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] 
print(mean(A), median(A), mode(A))
# (6.55, 7.0, [9])                