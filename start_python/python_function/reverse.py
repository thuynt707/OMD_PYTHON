# Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). 
# Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. 
# (kết quả là "Chicken The For Coming Is Fox The")
# Cách số 2
def reverse_and_swap(sentence):
    result = ''
    reverseWords = sentence[::-1].split(' ')
    for word in reverseWords:
        result += word[::-1].swapcase() + ' '
    return result.strip()

print(reverse_and_swap("tHE fOX iS cOMING fOR tHE cHICKEN"))   