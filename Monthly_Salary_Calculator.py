# Users can calculate the numbers of days they have worked, their hourly wage, and how much they should be paid.
# If the user's hourly pay changes based on work done, calculate their new pay rate.


def monthly_salary_calculator():
    days_worked = input("How many days have you worked this month: ")
    hours_per_day = input("How many hours do you work a day: ")
    total_hours_worked = int(days_worked) * int(hours_per_day)
    print("You have worked " + str(total_hours_worked) + " hours this month.")
    print("")

    avg_hourly_pay = input("How much are you paid per hour: $")
    hourly_pay_change = input("Does your hourly pay change depending on type of work done (Yes/No): ")
    if hourly_pay_change == "Yes":
        hourly_pay_change = input("What does your hourly pay change to: $")
        avg_hourly_pay_hours_worked = input("How many hours did you work at your average pay rate: ")
        pay_change_hours_worked = input("How many hours have you worked at your changed rate: ")
        adjusted_monthly_pay = int(avg_hourly_pay) * int(avg_hourly_pay_hours_worked) \
                               + int(hourly_pay_change) * int(pay_change_hours_worked)
        print("You will be paid $" + str(adjusted_monthly_pay) + " this month.")

    else:
        avg_monthly_pay = total_hours_worked * int(avg_hourly_pay)
        print("You will be paid " + str(avg_monthly_pay) + " this month.")

monthly_salary_calculator()