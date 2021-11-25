# Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
# Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum

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

A = [3, 6, 7, 9, 11, 12]
sum = 18
print(find_pair(A, sum))