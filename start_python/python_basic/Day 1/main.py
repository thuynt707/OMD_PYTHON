###Day 1

#Assignment 1:
#Viết chương trình chuyển đổi từ số giây (nguyên dương) thành giờ, phút, giây tương ứng
#step 1: Nhập số giây sec (int)
#step 2: Quy đổi và in ra giá trị giờ phút giây tương ứng
print("-----Convert inputted seconds to hour, minute and second-----")
int_sec = input("Nhập số giây: ")
int_hour = int(int_sec)//3600
int_mins = int(int_sec)%3600//60
int_sec = int(int_sec)%3600%60
print("Số giờ: " , int_hour, "hrs")
print("Số phút: ", int_mins, "mins")
print("Số giây: ", int_sec, "secs")
#Assignment 2:
#Viết chương trình quy đổi độ dài từ đơn vị km sang các đơn vị khác
#Step1: Nhập giá trị độ dài length - float (đơn vị km)
#Step2: Quy đổi sang các đơn vị m, dm, cm, mm, mile, inch và in kết quả (làm tròn đến 2 chữ số thập phân)
# print("-----Convert inputed length km unit to others-----")
# km = input("Nhập số km: ")
# m = round(float(km)*1000,2)
# dm = round(float(km)*10000,2)
# cm = round(float(km)*100000,2)
# mm = round(float(km)*1000000,2)
# mile = round(float(km)*1.609344,2)
# inch = round(float(km)*39370.1,2)
# print("Số m: " , m, "m")
# print("Số dm: " , dm, "dm")
# print("Số cm: " , cm, "cm")
# print("Số mm: " , mm, "mm")
# print("Số mile: " , mile, "mile")
# print("Số inch: " , inch, "inch")
# #Assignment 3:
# #Viết chương trình chuyển đổi nhiệt độ từ thang nhiệt Celcius sang các thang nhiệt Farenheit, Keven và Rankine
# #Step1: Nhập nhiệt độ (°C - float)
# #Step2: Quy đổi và in ra °F tương ứng (°F = °C * 9 / 5 + 32)
# #Step3: Quy đổi và in ra °K tương ứng (°K = °C + 273.15)
# #Step4: Quy đổi và in ra °R tương ứng (°R = (°C + 273.15) * 9 / 5))
# print("-----Convert temperaturs-----")
# temp_C = input("Nhập nhiệt độ °C: ")
# temp_F = float(temp_C)*9/5+32
# temp_K = float(temp_C)+ 273.15
# temp_R = (float(temp_C)+ 273.15)* 9 / 5
# print(temp_C,"°C","=" , temp_F,"°F")
# print(temp_C,"°C","=" , temp_K,"°K")
# print(temp_C,"°C","=" , temp_R,"°R")

# Bài 1: Định dạng thời gian
print("Bạn hãy nhập vào số giây")
second = int(input())
int_hour = int(second)/36000
int_mimute = int((int(second)/36000)/60)
int_second = int(int((int(second)/36000)/60))
if second<0:
    print("Bạn hãy nhập số nguyên dương nhé")
else:
    {
        print("Số giây sau khi chuyển đổi là: ", int_hour ,"giờ",int_mimute,"phút",int_mimute,"giây")
    }

# Bài 2: Chuyển đổi đơn vị độ dài
print("Bạn hãy nhập vào độ dài km")
leght = float(input())
float_m= round(float(leght*1000),2)
float_dm=round(float(leght*10000),2)
float_cm=round(float(leght*100000),2)
float_mm= round(float(leght*1000000),2)
float_mile= round(float(leght/1.609344),2)
float_inch= round(float(leght*1567839370.1),2)
print("Độ dài sau khi quy đổi các đơn vị là:",float_m,"mét,",float_dm,"dm,",float_cm,"cm,",float_mm,"mm,", float_mile, "mile,", float_inch,"ich")

# Bài 3: Chuyển đổi nhiệt độ
print("Bạn hãy nhập vào nhiệt độ")
celcius = float(input())
float_F= float(celcius*9/5+32)
float_K= float(celcius+237.15)
float_R= float((celcius+273.15)*9/5)

print("Nhiệt độ sau khi chuyển đổi là: ",float_F,"độ Farenheit, ",float_K,"độ Kenven,",float_R,"độ Rankine")