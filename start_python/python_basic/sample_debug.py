# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Viết chương trình Python kiểm tra số lớn nhất trong 3 số
# 
# - Khai báo 3 biến `a`, `b`, `c` nhập giá trị số bất kỳ (int)
# - Kiểm tra và in ra số lớn nhất trong 3 số đó

# %%
a, b, c = 12, 16, 19
print(max(a,b,c))
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

# %% [markdown]
# Viết chương trình kiểm tra một năm có phải năm nhuận hay không
# 
# - Nhập một năm `year` - int
# - Kiểm tra và in ra kết quả `year` có phải năm nhuận hay không
# 
# 💡 Năm nhuận là năm:
# 
# - Chia hết cho 400
# - Chia hết cho 4 **nhưng** không chia hết cho 100

# %%


# %% [markdown]
# Viết chương trình tính chỉ số BMI (Body Mass Index - Chỉ số cơ thể)
# 
# - Nhập chiều cao `h` (đơn vị m) và cân nặng `w` (đơn vị kg)
# - Tính chỉ số BMI: `w / (h * h)`
# - In chỉ số và thông báo kết quả theo quy ước:
#     -  BMI < 17: Gầy độ II
#     - 17 <= BMI < 18.5: Gầy độ I
#     - 18.5 <= BMI < 25: Bình thường
#     - 25 <= BMI < 30: Thừa cân
#     - 30 <= BMI < 35: Béo phì độ I
#     - 35 <= BMI: Béo phì độ II
# %% [markdown]
# 

