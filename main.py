def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not Leap Year"


def happy_ticket(ticket_number):
    sub_first_part = 0
    sub_second_part = 0
    for i in range(6):
        digit_ticket_number = int(ticket_number[i])
        if i < 3:
            sub_first_part += digit_ticket_number
        else:
            sub_second_part += digit_ticket_number
    if sub_first_part == sub_second_part:
        return "Happy ticket"
    else:
        return "Not Happy Ticket"



while True:

    task = input("Chose your task (input 1 or 2): ")

    if task == "1":
        try:
            checked_year = int(input("Enter the year: "))
            if checked_year < 1:
                raise ValueError
            print(leap_year(checked_year))
        except ValueError:
            print("Invalid input, please try again")

    elif task == "2":
        try:
            ticket = input("Enter the ticket: ")
            if len(ticket) != 6:
                raise ValueError
            print(happy_ticket(ticket))
        except ValueError:
            print("Invalid input, please try again")

    else:
        print("Invalid Input")