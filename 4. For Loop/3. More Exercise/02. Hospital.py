"""
For a given period of time, every day patients arrive at the hospital for examination.
It initially has 7 doctors. Each doctor can only see one patient per day, but sometimes
there is a shortage of doctors, so the remaining patients are sent to other hospitals.

Every third day, the hospital makes calculations, and if the number of unexamined patients
is greater than the number of examined ones, another doctor is appointed.

As the appointment takes place before the admission of patients for the day begins.

Write a program that calculates for the given period the number of examined and unexamined patients
"""


period = int(input())

doctors = 7
treated = 0
untreated = 0

for i in range(1, period + 1):
    patients = int(input())

    if i % 3 == 0 and untreated >= treated:
        doctors += 1
    if patients <= doctors:
        treated += patients
    else:
        treated += doctors
        untreated += patients - doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")

