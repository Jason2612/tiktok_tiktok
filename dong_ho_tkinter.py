import time
import datetime
from playsound import playsound
import tkinter as tk

def countdown():
    for i in range(int(entry_loop.get())):
        total_seconds = int(entry_hour.get()) * 3600 + int(entry_min.get()) * 60 + int(entry_second.get())
        while total_seconds >= 0:
            minute,second = (total_seconds//60, total_seconds%60)
            hour = 0
            if minute > 60:
                hour , minute = (minute // 60, minute % 60)

            
            mins.set(minute)
            hrs.set(hour)
            sec.set(second)

            entry_frame.update()
            time.sleep(1)
            
            if total_seconds == 0:
                playsound('C:\\Users\\Phong\\Desktop\\PlusPlus code-20220601T152632Z-001\\PlusPlus code\\HomeWork\\bai_tap_dong_ho\\Sounds\\music1.mp3')
                hrs.set('00')
                mins.set('00')
                sec.set('00')
            total_seconds -= 1
        
    
    lbl_notice.config(text = "Xong" + " " + str(i+1) + " " + "round" + " rồi đấy ông cháu")
    lbl_notice.grid(row=0, column=0)
    
        
window = tk.Tk()
window.title("Đồng hồ đếm ngược")
window.geometry("500x300")

entry_frame=tk.Frame(window)
entry_frame.place(
    relx=0.45,
    rely=0.55,
    anchor=tk.CENTER
)

# Tạo đồng hồ đếm ngược
hrs=tk.StringVar()
tk.Entry(entry_frame, textvariable=hrs, width=2, font='arial 12').grid(row=3, column=1,pady=10)
hrs.set('00')

mins = tk.StringVar()
tk.Entry(entry_frame, textvariable=mins, width=2, font='arial 12').grid(row=3,column=2,pady=10)
mins.set('00')

sec = tk.StringVar()
tk.Entry(entry_frame, textvariable=sec, width=2, font="arial 12").grid(row=3,column=3,pady=10)
sec.set('00')



# tạo label và entry
lbl_menu = tk.Label(window, text="Làm việc đi ông cháu êi", font=50)
lbl_time = tk.Label(entry_frame, text="Thời gian\n cho 1 vòng")
entry_hour = tk.Entry(entry_frame, width=5)
entry_min = tk.Entry(entry_frame, width=5)
entry_second = tk.Entry(entry_frame, width=5)
lbl_loop = tk.Label(entry_frame, text="Số lần chạy")
entry_loop = tk.Entry(entry_frame, width= 5)
btn_start = tk.Button(entry_frame, text="Start", command=countdown)




# tạo vị trí trên frame
lbl_menu.pack(pady=15)
lbl_time.grid(row=1,column=0, padx=10)
entry_hour.grid(row=1, column=1)
entry_min.grid(row=1,column=2)
entry_second.grid(row=1,column=3)
lbl_loop.grid(row=2, column=0)
entry_loop.grid(row=2, column=1)
btn_start.grid(row=4,column=2,pady=10)



# Thông báo hiển thị
notice_frame=tk.Frame(window)
notice_frame.pack()

lbl_notice = tk.Label(notice_frame, text='', bg="red", foreground="white")

window.mainloop()

