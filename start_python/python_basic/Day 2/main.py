
### Bài 1: Tìm số lớn nhất.
# Viết chương trình Python kiểm tra số lớn nhất trong 3 số
# - Khai báo 3 biến `a`, `b`, `c` nhập giá trị số bất kỳ (int)
# - Kiểm tra và in ra số lớn nhất trong 3 số đó
print('\n\nBài 1: Tìm số lớn nhất')
print("Nhập số thứ nhất: ")
a = int(input())
print("Nhập số thứ hai: ")
b = int(input())
print("Nhập số thứ ba: ")
c = int(input())

# Tìm số lớn nhất dùng hàm Max
print(max(a,b,c))

# Tìm số lớn nhất dùng if else
if a >= b:
    if a >= c:
        print("Max is: ", a)
    else:
        print("Max is: ", c)
else:
    if b >= c:
        print("Max is: ", b)
    else:
        print("Max is: ", c)

### Bài 2: Kiểm tra năm nhuận
# Viết chương trình kiểm tra một năm có phải năm nhuận hay không

# Nhập một năm year - int
# Kiểm tra và in ra kết quả year có phải năm nhuận hay không
# Năm nhuận là năm:
# Chia hết cho 400
# Chia hết cho 4 nhưng không chia hết cho 100
print('\n\nBài 2: Kiểm tra năm nhuận')
year = int(input())
if year%400==0: 
    print('Năm ', year, ' là năm nhuận' )
elif (year % 4 == 0) and (year % 100 != 0):
    print('Năm ', year, ' là năm nhuận' )
else:
    print('Năm ', year, ' không phải là năm nhuận' )

### Bài 3: Chỉ số BMI
# Viết chương trình tính chỉ số BMI (Body Mass Index - Chỉ số cơ thể)
# Nhập chiều cao h (đơn vị m) và cân nặng w (đơn vị kg)
# Tính chỉ số BMI: w / (h * h)
# In chỉ số và thông báo kết quả theo quy ước:
# BMI < 17: Gầy độ II
# 17 <= BMI < 18.5: Gầy độ I
# 18.5 <= BMI < 25: Bình thường
# 25 <= BMI < 30: Thừa cân
# 30 <= BMI < 35: Béo phì độ I
# 35 <= BMI: Béo phì độ II
print('\n\nBài 3: Tính chỉ số BMI')
h = float(input("\tNhập chiều cao (m): \t"))
w = float(input("\tNhập cân nặng (kg): \t"))
BMI = round(w / (h * h),2)
if (BMI < 17):
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Gầy độ II')
elif (17 <= BMI < 18.5):
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Gầy độ I')
elif (18.5 <= BMI < 25):
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Bình thường')
elif (25 <= BMI < 30):
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Thừa cân')
elif (30 <= BMI < 35):
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Béo phì độ I')
else:
  print('\t\tChỉ số BMI của bạn: ', BMI, ' - Béo phì độ II')
