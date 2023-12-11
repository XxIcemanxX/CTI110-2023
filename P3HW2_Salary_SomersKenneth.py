# CTI-110
# P3HW2 - Salary
# Kenneth Somers
# 10/26/2023


employee_name = input("Enter the name of the employee: ")


hours_worked = float(input("Enter the number of hours worked this week: "))


pay_rate = float(input("Enter the employee's pay rate: "))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate


gross_pay = regular_pay + overtime_pay

print("---------------------------")
print("Employee Name:", employee_name)


print("Number of Hours Worked:", hours_worked) 
print("Pay Rate:", pay_rate)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)
