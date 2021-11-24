### Bài 1: Find pair
# Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
# Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
# vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []

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

find_pair([3, 6, 7, 9, 11, 12], 18)

