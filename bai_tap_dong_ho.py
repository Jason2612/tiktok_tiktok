"""
viet 1 chuong trinh noi dung on kien thuc ve datetime

1 chuong trinh mo phong chuong giang duong
trong do cu den dau gio, la hien thi thong bao
vao tiet n, het tiet thi hien thi thong bao la het tiet n

phat 1 doan nhac reng reng - tuong ung nhu chuong giang duong thay vi hien thi thong bao
"""

# Khai bao so tiet hoc
# n = 5
# 1 tiet 45p
# lam 1 counter 45p 
# in ra thong bao luc bat dau tiet hoc 1
# chay counter
# sau 45p in thong bao da het gio hoc tiet 1
# lap tuan tu cho n tiet hoc

# NANG CAP
# lưu giữ các lần chạy quá khứ


import time
import datetime
from playsound import playsound

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
        


print("Đây là chuông báo tiết học 45p\n"
    "1. Ấn phím s để bắt đầu dùng\n"
    "2. Ấn phím e để thoát khỏi chương trình") 


option = input("Nhập lựa chọn: ")

while option.lower() == "s":
    print("\n")
    n = int(input("Nhập số tiết học hôm nay: "))
    print("\n")
    for i in range(n):
        print("Bắt đầu tiết học", str(i+1))
        countdown(0,45,0)
        playsound('C:\\Users\\Phong\\Desktop\\PlusPlus code-20220601T152632Z-001\\PlusPlus code\\HomeWork\\bai_tap_dong_ho\\Sounds\\music1.mp3')
        print("Kết thúc tiết học", str(i+1))
        print("\n")

    
    print("Bạn có muốn dùng tiếp không")
    print(" 1. Ấn phím s để bắt đầu dùng")
    print(" 2. Ấn phím e để thoát khỏi chương trình")
    print("\n")

    option = input("Nhập lựa chọn: ")
    if option.lower() == 'e':
        break


