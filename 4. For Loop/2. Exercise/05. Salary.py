"""
A company boss notices that more and more employees are spending time on distracting websites.
To prevent this, it implements surprise checks on its employees' open browser tabs.

According to the open site in taba, the following fines are imposed:
• "Facebook" -> BGN 150
• "Instagram" -> BGN 100
• "Reddit" -> BGN 50

Two lines are read from the console:
• Number of open tabs in the browser n - an integer in the interval [1...10]
• Salary - number in the interval [500...1500]
Then n - number of times website name - text is read
"""


count_open_tabs = int(input())
salary = int(input())

for i in range(count_open_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{int(salary)}")

