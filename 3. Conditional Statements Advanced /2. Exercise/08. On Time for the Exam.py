"""
A student must go to an exam at a specific time (for example, 9:30 a.m.).
He comes to the exam hall at a given arrival time (eg 9:40).

The student is considered to have arrived on time if he arrived at the time
of the exam or up to half an hour before. If he arrived more than 30 minutes earlier,he was late.
If he came after the exam time, he is late.

Write a program that reads an exam time and an arrival time and prints whether the student was on time,
whether he was early or late, and by how many hours or minutes he was early or late.
"""


exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival = arrival_hour * 60 + arrival_minute

diff = abs(exam_time - arrival)
diff_h = diff // 60
diff_m = diff % 60

if exam_time == arrival:
    print("On time")

elif exam_time > arrival:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif diff < 60:
        print("Early")
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        print("Early")
        print(f"{diff_h}:{diff_m:02d} hours before the start")

elif exam_time < arrival:
    if diff < 60:
        print("Late")
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        print("Late")
        print(f"{diff_h}:{diff_m:02d} hours after the start")

