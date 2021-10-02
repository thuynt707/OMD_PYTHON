
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